#!/bin/bash

# Display script name and first two arguments
echo "Script and first two args: $0 $1 $2"

# Note: The single quotes in your original prevented variable expansion
# Corrected to show the flow of arguments
echo "Reordered: $2 $1 $3"

# Store all arguments in an array
var=("$@")

# Display all elements in the array
echo "All arguments: ${var[@]}"

# Display the total count of arguments
echo "Total count: $#"