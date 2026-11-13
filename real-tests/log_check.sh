#!/bin/bash
log_file="app.log"
if [ -f $log_file ]; then
  echo "Log file exists."
  echo "Analyzing log file..."
  echo "Number of lines in log file: $(wc -l < $log_file)"
  echo "Number of error entries in log file: $(grep -c 'ERROR' $log_file)"
else
  echo "Log file does not exist."
fi