#!/bin/bash

SEARCH_ROOTS=("/home" "/tmp" "/var" "/srv" "/opt" "/media")

remove_files() {
    local file_path=""

    for file_path in "$@"; do
        if [[ -f "$file_path" ]]; then
            rm -f -- "$file_path"
            echo "Removed file: $file_path"
        fi
    done
}

remove_dirs_reverse() {
    local dirs=("$@")
    local i=0

    for (( i=${#dirs[@]}-1; i>=0; i-- )); do
        if [[ -d "${dirs[i]}" ]]; then
            rmdir -- "${dirs[i]}" 2>/dev/null && echo "Removed dir: ${dirs[i]}"
        fi
    done
}

clean_by_log() {
    local log_path=""
    local files=()
    local dirs=()

    read -r -p "Enter log file path: " log_path
    check_log_file "$log_path"

    mapfile -t files < <(sed -n 's/^\[FILE\] [0-9-]* [0-9:]* \(.*\) size: .*$/\1/p' "$log_path")
    mapfile -t dirs < <(sed -n 's/^\[DIR\] [0-9-]* [0-9:]* \(.*\)$/\1/p' "$log_path")

    remove_files "${files[@]}"
    remove_dirs_reverse "${dirs[@]}"
}

clean_by_time() {
    local start_time=""
    local end_time=""
    local root=""
    local path=""
    local files=()
    local dirs=()

    read -r -p "Enter start time (YYYY-MM-DD HH:MM): " start_time
    read -r -p "Enter end time (YYYY-MM-DD HH:MM): " end_time

    check_datetime "$start_time"
    check_datetime "$end_time"

    for root in "${SEARCH_ROOTS[@]}"; do
        while read -r path; do
            files+=("$path")
        done < <(find "$root" \
            \( -path "*bin*" -o -path "*sbin*" \) -prune -o \
            -type f -newermt "$start_time" ! -newermt "$end_time" \
            -name '*_[0-9][0-9][0-9][0-9][0-9][0-9]*.*' -print 2>/dev/null)

        while read -r path; do
            dirs+=("$path")
        done < <(find "$root" \
            \( -path "*bin*" -o -path "*sbin*" \) -prune -o \
            -type d -newermt "$start_time" ! -newermt "$end_time" \
            -name '*_[0-9][0-9][0-9][0-9][0-9][0-9]' -print 2>/dev/null)
    done

    remove_files "${files[@]}"
    remove_dirs_reverse "${dirs[@]}"
}

clean_by_mask() {
    local mask=""
    local root=""
    local path=""
    local files=()
    local dirs=()

    read -r -p "Enter name mask (example: az*_070426): " mask
    check_mask "$mask"

    for root in "${SEARCH_ROOTS[@]}"; do
        while read -r path; do
            files+=("$path")
        done < <(find "$root" \
            \( -path "*bin*" -o -path "*sbin*" \) -prune -o \
            -type f -name "${mask}.*" -print 2>/dev/null)

        while read -r path; do
            dirs+=("$path")
        done < <(find "$root" \
            \( -path "*bin*" -o -path "*sbin*" \) -prune -o \
            -type d -name "$mask" -print 2>/dev/null)
    done

    remove_files "${files[@]}"
    remove_dirs_reverse "${dirs[@]}"
}
