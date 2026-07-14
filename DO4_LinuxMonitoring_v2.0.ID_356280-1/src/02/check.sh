#!/bin/bash

count_args() {
    if [ $# -ne 3 ]; then
        echo "Usage: script with <param1> <param2> <param3>"
        exit 1
    fi
}

check_folder() {
    if [[ ! "$1" =~ ^[a-zA-Z]{1,7}$ ]]; then
        echo "Not a valid folder name: $1"
        exit 1
    fi
    
}

check_files() {
    if [[ ! "$1" =~ ^[a-zA-Z]{1,7}\.[a-zA-Z]{1,3}$ ]]; then
        echo "Not a valid file name: $1"
        exit 1
    fi
}

check_size() {
    if [[ ! "$1" =~ ^[1-9][0-9]*Mb$ ]];
    then
        echo "Size number must be a positive integer less than or equal to 100 followed by 'Mb'"
        exit 1
    fi

    local num=${1%Mb}
    
    if [[ "$num" -gt 100 ]]
    then
        echo "Size number must be less than or equal to 100"
        exit 1
    fi

}