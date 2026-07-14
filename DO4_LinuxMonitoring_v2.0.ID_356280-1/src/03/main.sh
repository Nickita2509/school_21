#!/bin/bash

source ./check.sh
source ./clean.sh

count_args "$@"
check_mode "$1"

case "$1" in
    1) clean_by_log ;;
    2) clean_by_time ;;
    3) clean_by_mask ;;
esac
