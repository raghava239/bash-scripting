#!/bin/bash

log_file = "app.log"
error_count = $(grep -i "error" app.log)
warning_count = $(grep -i "warnings" app.log)
last_5_errors = $(tail -f 5 app.log | grep -i "error") 

if [ -f $log_file ]; then
   echo "log file exists"
   echo "All error counts are : $error_count "
   echo " all warning counts are : $warning_count "
   if ( $last_5_errors -lt 5 ); then
      echo "Last 5 errors are : $last_5_errors"
   else 
      echo "CRITICAL"
   fi
   
else 
  echo "file not exists"