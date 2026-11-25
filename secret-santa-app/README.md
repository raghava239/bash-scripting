# Secret Santa 2026 — App Engine

A small Flask application for exactly 20 participants. It stores registrations and assignments in
Cloud Firestore. Once all 20 people have registered, the first spin creates a random derangement:
nobody gets themselves, and every recipient is assigned exactly once. Each participant sees the
same result every time they spin again.

## 1. Prerequisites

- A Google Cloud project with billing enabled
- Google Cloud CLI (`gcloud`) installed and authenticated
- App Engine application created in your chosen region
- Firestore database created in **Native mode**

## 2. Enable APIs

```bash
gcloud config set project YOUR_PROJECT_ID
gcloud services enable appengine.googleapis.com firestore.googleapis.com
```

Create the App Engine app if it does not already exist:

```bash
gcloud app create --region=YOUR_APP_ENGINE_REGION
```

Create a Firestore database in Native mode in a suitable location using the Google Cloud Console.

## 3. Grant Firestore access to App Engine

Find the App Engine default service account:

```text
YOUR_PROJECT_ID@appspot.gserviceaccount.com
```

Grant it the **Cloud Datastore User** role (`roles/datastore.user`) on the project.
Firestore in Native mode uses this role for the app's database operations.

## 4. Deploy

From this project directory:

```bash
gcloud app deploy
```

Open the deployed application:

```bash
gcloud app browse
```

## 5. How to run the game

1. Share the App Engine URL with the 20 participants.
2. Each person registers using their name.
3. When the count reaches 20/20, registration closes.
4. Each participant enters their registered name and clicks **SPIN & REVEAL**.
5. The assignment is fixed; spinning again does not change it.

## Important privacy note

This starter version uses names as the participant lookup. It is suitable for a trusted small group,
but it does not authenticate a person: someone who knows another participant's registered name
could reveal that person's assignment. For a real workplace game, add a unique private PIN or
individual invitation token before sharing the app widely.

## Reset for a new game

The game document is `games/secret-santa-2026` in Firestore. To start another game, delete that
document in the Firestore Console before registrations begin. Do not reset it after people have
started revealing assignments.
