
servers=("web01" "web02" "app01" "app02" "db01")
count=1
upper_server=$(echo "$server" | tr '[:lower:]' '[:upper:]')

echo "Server $count: $upper_server"

echo "First server is: ${servers[0]}"
echo "Last server is: ${servers[4]}"
echo "Total number of servers is: ${#servers[@]}"
echo "------------Server inventory------------"


for server in "${servers[@]}"; do
  upper_server=$(echo "$server" | tr '[:lower:]' '[:upper:]')
  echo "Server $count: $upper_server"
  ((count++))
done