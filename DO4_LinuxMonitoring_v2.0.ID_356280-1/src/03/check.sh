#!/bin/bash

count_args() {
    if [[ $# -ne 1 ]]; then
        echo "Usage: main.sh <1|2|3>"
        exit 1
    fi
}

check_mode() {
    if [[ ! "$1" =~ ^[123]$ ]]; then
        echo "Mode must be 1, 2 or 3."
        exit 1
    fi
}

check_log_file() {
    if [[ ! -f "$1" ]]; then
        echo "Log file does not exist: $1"
        exit 1
    fi
}

check_datetime() {
    if [[ ! "$1" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}$ ]]; then
        echo "Datetime must be in format: YYYY-MM-DD HH:MM"
        exit 1
    fi
}

check_mask() {
    if [[ -z "$1" || "$1" == */* ]]; then
        echo "Mask must not be empty and must not contain '/'."
        exit 1
    fi
}
