#!/bin/bash

source ./check.sh
source ./create_files.sh

count_args "$@"
check_path "$1"
check_numbers "$2"
check_numbers "$4"
check_folder "$3"
check_files "$5"
check_size "$6"
create_dir_files "$1" "$2" "$3" "$4" "$5" "$6"


