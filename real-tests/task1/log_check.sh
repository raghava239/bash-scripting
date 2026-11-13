#!/bin/bash
log_file="app.log"

if [ -f "$log_file" ]; then
	echo "file exists"
	echo "echo total log entries:"
	wc -l < "$log_file"
	echo "connection timeout errors:"
	grep -i "timeout" $log_file | wc -l 
else
	echo "file doesnt exists"
fi
