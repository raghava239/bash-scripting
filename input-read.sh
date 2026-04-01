#!/bin/bash

# echo "Enter name: "
# read name1 name2 name3
# echo "Entered names: $name1 $name2 $name3"

## To ask the input in same line

#read -p "Enter name: " username
#read -sp "Enter password: " password

#echo "Entered names: $username"
#echo "Entered password: $password"

# Using -p allows you to put the prompt and input on the same line
read -p "Please enter the names: " -a names

# Using printf for better control over alignment and spacing
#printf "Entered names: %s %s %s \n" "${names[0]}" "${names[1]}" "${names[2]}"

echo "Entered names: ${names[@]}"