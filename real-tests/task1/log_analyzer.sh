#!/bin/bash

log_file="app.log"

if [ -f $log_file ]; then
  echo "Log file exists."
else
  echo "Log file does not exist."
fi