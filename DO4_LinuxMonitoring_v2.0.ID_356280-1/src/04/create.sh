#!/bin/bash

source data.sh

day_offset=0
mkdir -p ./logs
log_base_name="./logs/log_file"

for (( i=0; i<5; i++ )); do
    file_date=$(date -d "$day_offset day ago" '+%Y%m%d')
    log_date=$(date -d "$day_offset day ago" '+%d/%b/%Y')
    log_file="${log_base_name}_${file_date}.log"
    current_seconds=0
    count_lines=$((RANDOM % 901 + 100))
    base_step=$((86400 / count_lines))

    for (( j=0; j<$count_lines; j++ )); do
        offset=$(((RANDOM % 11) - 5 ))
        step_seconds=$((base_step + offset))
        current_seconds=$((current_seconds + step_seconds))
        if [[ $current_seconds -ge 86400 ]]; then
            echo "$counts"
            break
        fi
        ip="$((RANDOM % 256 + 1)).$((RANDOM % 256)).$((RANDOM % 256)).$((RANDOM % 256))"
        log_time=$(printf "%02d:%02d:%02d" $((current_seconds/3600)) $(((current_seconds%3600)/60)) $((current_seconds%60)))
        method="${methods[RANDOM % ${#methods[@]}]}"
        url="${urls[RANDOM % ${#urls[@]}]}"
        status_code="${status_codes[RANDOM % ${#status_codes[@]}]}"
        agent="${agents[RANDOM % ${#agents[@]}]}"

        echo "$ip - - [$log_date:$log_time "$(date '+%z')"] \"$method $url HTTP/1.1\" $status_code - \"$agent\"" >> "$log_file"
        
    done

    day_offset=$((day_offset + 1))
done