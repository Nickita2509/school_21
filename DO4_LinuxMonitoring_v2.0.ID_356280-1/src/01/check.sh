#!/bin/bash

count_args() {
    if [ $# -ne 6 ]; then
        echo "Usage: script with <param1> <param2> <param3> <param4> <param5> <param6>"
        exit 1
    fi
}

check_path() {
    if [[ ! "$1" =~ ^/ ]];then
        echo "Path isn't absolute: $1"
        exit 1
    fi
    if [[ ! -d "$1" ]]; then
        echo "Directory does not exist: $1"
        exit 1
    fi
}

check_numbers() {
    if [[ ! "$1" =~ ^[1-9][0-9]*$ ]]; then
        echo "Not a positive integer: $1"
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
    if [[ ! "$1" =~ ^[1-9][0-9]*kb$ ]];
    then
        echo "Size number must be a positive integer less than or equal to 100 followed by 'kb'"
        exit 1
    fi

    local num=${1%kb}
    
    if [[ "$num" -gt 100 ]]
    then
        echo "Size number must be less than or equal to 100"
        exit 1
    fi

}
