#!/bin/bash

echo -e "Enter the name of the file/directory: \c"
read filename

# Checking for existence based on flags
if [ -e "$filename" ]; then
    echo "Success: $filename exists."
    
    # Check if it is a directory
    if [ -d "$filename" ]; then
        echo "- It is a directory."
    fi

    # Check if it is a regular file
    if [ -f "$filename" ]; then
        echo "- It is a regular file."
    fi

    # Check if the file is NOT empty (has size > 0)
    if [ -s "$filename" ]; then
        echo "- The file is not empty."
    else
        echo "- The file is empty."
    fi

    # Check Permissions
    [ -r "$filename" ] && echo "- Read permission: Yes" || echo "- Read permission: No"
    [ -w "$filename" ] && echo "- Write permission: Yes" || echo "- Write permission: No"
    [ -x "$filename" ] && echo "- Execute permission: Yes" || echo "- Execute permission: No"

else
    echo "Error: $filename does not exist."
fi