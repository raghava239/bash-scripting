echo -e "Enter the file name: \c"
read filename

if [ -f "$filename" ]; then
    if [ -w "$filename" ]; then
        echo "Write permissions exist. Type your text and press Ctrl+D to save:"
        cat >> "$filename"
    else
        echo "File $filename does not have write permissions."
    fi
else
    echo "File $filename does not exist."
fi