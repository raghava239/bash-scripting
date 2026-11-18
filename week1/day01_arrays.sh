#!/bin/bash

servers=("web01" "web02" "db01" "app01")
count=1
echo "List of servers are : ${servers[0]}"
echo "List of servers are : ${servers[2]}"
echo "List of servers are : ${servers[3]}"
echo "List of servers are : ${servers[@]}"
echo "Total number of servers are : ${#servers[@]}"


for server in "${servers[@]}"; do
   echo "Server name is : $server"
   ((count++))
done