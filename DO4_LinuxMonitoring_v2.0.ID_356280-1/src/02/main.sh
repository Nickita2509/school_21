#!/bin/bash

SECONDS=0
start_time=$(date "+%Y-%m-%d %H:%M:%S")

echo "Script started"
source ./check.sh
source ./create_files.sh


log_file="./log_file_$(date +%Y%m%d_%H%M%S).log"

count_args "$@"
check_folder "$1"
check_files "$2"
check_size "$3"

echo "Creating directories and files..."

create_dir_files "$1" "$2" "$3"

echo "Script completed."

end_time=$(date "+%Y-%m-%d %H:%M:%S")
execution_time=$SECONDS

echo "Script start time: $start_time"
echo "Script end time: $end_time"
echo "Script execution time: $execution_time seconds"

echo "Script start time: $start_time" >> "$log_file"
echo "Script end time: $end_time" >> "$log_file"
echo "Script execution time: $execution_time seconds" >> "$log_file"