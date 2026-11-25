import random
from flask import Flask, request, redirect, url_for, render_template_string
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client()
game_ref = db.collection("games").document("secret-santa-2026")

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Secret Santa 2026</title>
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; font-family: Arial, sans-serif;
           background: linear-gradient(135deg,#102b46,#1d5360); color: #fff;
           display: flex; align-items: center; justify-content: center; padding: 24px; }
    .card { width: 100%; max-width: 480px; background: #fff; color: #182433;
            border-radius: 20px; padding: 30px; box-shadow: 0 18px 50px #0004; }
    h1 { text-align: center; margin: 0 0 8px; }
    .sub { text-align: center; color: #64748b; margin: 0 0 24px; }
    label { display:block; font-weight: bold; margin: 16px 0 8px; }
    input { width:100%; padding:14px; border:1px solid #cbd5e1; border-radius:10px; font-size:16px; }
    button { width:100%; border:0; border-radius:10px; padding:14px; margin-top:12px;
             background:#c62828; color:white; font-size:16px; font-weight:bold; cursor:pointer; }
    button:hover { background:#a91f1f; }
    .count { background:#eff6ff; padding:14px; border-radius:10px; text-align:center; margin:18px 0; }
    .message { background:#fff7ed; color:#9a3412; padding:12px; border-radius:10px; margin:14px 0; }
    .result { background:#ecfdf5; border:1px solid #86efac; padding:20px; border-radius:12px;
              text-align:center; margin-top:18px; }
    .result strong { display:block; font-size:26px; color:#166534; margin-top:8px; }
    .small { color:#64748b; font-size:13px; text-align:center; margin-top:20px; }
    .divider { border:0; border-top:1px solid #e2e8f0; margin:24px 0; }
  </style>
</head>
<body>
  <main class="card">
    <h1>🎅 Secret Santa 2026</h1>
    <p class="sub">20 members · One surprise recipient each</p>

    <div class="count"><b>{{ count }} / 20</b> members registered</div>

    {% if message %}<div class="message">{{ message }}</div>{% endif %}

    {% if count < 20 %}
      <form method="post" action="/register">
        <label for="register_name">Join the game — enter your name</label>
        <input id="register_name" name="name" maxlength="50" required
               placeholder="Enter your full name">
        <button type="submit">JOIN SECRET SANTA</button>
      </form>
    {% else %}
      <div class="message">All 20 members have registered. Registration is closed!</div>
    {% endif %}

    <hr class="divider">

    <form method="post" action="/spin">
      <label for="spin_name">Already registered? Enter your name to spin</label>
      <input id="spin_name" name="name" maxlength="50" required
             placeholder="Enter your registered name" value="{{ name or '' }}">
      <button type="submit">🎁 SPIN & REVEAL</button>
    </form>

    {% if recipient %}
      <div class="result">
        Your Secret Santa recipient is:
        <strong>{{ recipient }}</strong>
        <p>Keep it a secret! 🤫</p>
      </div>
    {% endif %}

    <p class="small">Your assignment is permanent. Spinning again will show the same person.</p>
  </main>
</body>
</html>
"""

def normalized(value):
    return " ".join(value.strip().split()).casefold()

def read_game():
    snapshot = game_ref.get()
    if not snapshot.exists:
        game_ref.set({"members": [], "assignments": {}})
        return {"members": [], "assignments": {}}
    return snapshot.to_dict()

def create_derangement(members):
    # Shuffle until nobody is assigned themselves.
    while True:
        recipients = members[:]
        random.shuffle(recipients)
        if all(normalized(giver) != normalized(recipient)
               for giver, recipient in zip(members, recipients)):
            return dict(zip(members, recipients))

@app.get("/")
def home():
    data = read_game()
    return render_template_string(
        PAGE, count=len(data.get("members", [])), message=request.args.get("message"),
        name=request.args.get("name", ""), recipient=request.args.get("recipient")
    )

@app.post("/register")
def register():
    name = " ".join(request.form.get("name", "").strip().split())
    if not name or len(name) > 50:
        return redirect(url_for("home", message="Please enter a valid name (up to 50 characters)."))

    transaction = db.transaction()

    @firestore.transactional
    def add_member(txn):
        snapshot = game_ref.get(transaction=txn)
        data = snapshot.to_dict() if snapshot.exists else {"members": [], "assignments": {}}
        members = data.get("members", [])
        if len(members) >= 20:
            return "The game is full. All 20 places are taken."
        if any(normalized(existing) == normalized(name) for existing in members):
            return "That name is already registered. Please use your registered name."
        members.append(name)
        txn.set(game_ref, {"members": members, "assignments": data.get("assignments", {})})
        return "OK"

    result = add_member(transaction)
    if result != "OK":
        return redirect(url_for("home", message=result))
    return redirect(url_for("home", message=f"Welcome, {name}! You are registered.",
                            name=name))

@app.post("/spin")
def spin():
    name = " ".join(request.form.get("name", "").strip().split())
    if not name:
        return redirect(url_for("home", message="Enter your registered name first."))

    transaction = db.transaction()

    @firestore.transactional
    def get_assignment(txn):
        snapshot = game_ref.get(transaction=txn)
        if not snapshot.exists:
            return ("Please register all 20 members first.", None)
        data = snapshot.to_dict()
        members = data.get("members", [])
        if not any(normalized(member) == normalized(name) for member in members):
            return ("Name not found. Please enter the name you registered with.", None)
        if len(members) != 20:
            return (f"Only {len(members)} of 20 members have registered. Please wait.", None)

        assignments = data.get("assignments", {})
        if not assignments:
            assignments = create_derangement(members)
            txn.update(game_ref, {"assignments": assignments})

        registered_name = next(m for m in members if normalized(m) == normalized(name))
        return (None, assignments[registered_name])

    message, recipient = get_assignment(transaction)
    if message:
        return redirect(url_for("home", message=message, name=name))
    return redirect(url_for("home", name=name, recipient=recipient))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
