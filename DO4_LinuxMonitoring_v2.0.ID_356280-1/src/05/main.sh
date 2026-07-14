#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Usage: main.sh <1/2/3/4>"
    exit 1
fi

if [[ ! "$1" =~ ^[1-4]$ ]]; then
    echo "Mode must be 1, 2, 3 or 4."
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$SCRIPT_DIR/../04/logs"

shopt -s nullglob
log_files=("$LOG_DIR"/log_file_*.log)
shopt -u nullglob

if [[ ${#log_files[@]} -eq 0 ]]; then
    echo "No log files found."
    exit 1
fi

case "$1" in
    1)
        awk '{print $0}' "${log_files[@]}" | sort -k9,9n
        ;;
    2)
        awk '{print $1}' "${log_files[@]}" | sort -u
        ;;
    3)
        awk '$9 ~ /^[45][0-9][0-9]$/ { print $0 }' "${log_files[@]}"
        ;;
    4)
        awk '$9 ~ /^[45][0-9][0-9]$/ { print $1 }' "${log_files[@]}" | sort -u
        ;;
esac
