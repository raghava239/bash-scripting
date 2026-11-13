#!/bin/bash
log_file="app.log"
ERROR_COUNT=$(grep -iE "error" app.log | wc -l)

if [ -f  $log_file ]; then
    echo "Log file found"
    echo "number of error entries $ERROR_COUNT"
    
    if [ $ERROR_COUNT -gt 5 ]; then
        echo "CRITICAL: High error count"
    else
        echo "Application error count is normal"
    fi

else
  echo "log file not found"
fi

