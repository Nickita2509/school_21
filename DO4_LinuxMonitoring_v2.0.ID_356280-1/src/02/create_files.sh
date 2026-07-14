#!/bin/bash

execution_letters() {
    local letters="$1"
    local name=""

    for (( i=0; i<${#letters}; i++ )); do
        local char="${letters:i:1}"
        name+="$char"
    done

    if [[ ${#name} -lt 5 ]]; then
        while [[ ${#name} -lt 5 ]]; do
            local last_char="${name: -1}"
            name+="$last_char"
        done
    fi
    echo "$name"
}

create_new_name() {
    local new_name="$1"
    
    local last_char="${new_name: -1}"
    new_name+="$last_char"

    echo "$new_name"
} 

create_dir_files() {

    local folder_base="$(execution_letters "$1")"
    local current_date="$(date +%d%m%y)"

    local file_mask_name="${2%.*}"
    local file_ext="${2#*.}"
    local file_base="$(execution_letters "$file_mask_name")"
    local size_mb="${3%Mb}"

    local search_roots=("/home" "/tmp" "/var" "/srv" "/opt" "/media")
    local valid_dirs=()
    local root=""
    local dir=""

    for root in "${search_roots[@]}"; do
        while read -r dir; do
            if [[ "$dir" != *bin* && -w "$dir" ]]; then
                valid_dirs+=("$dir")
            fi
        done < <(find "$root" -type d 2>/dev/null)
    done

    local count_dirs=${#valid_dirs[@]}
    if [[ $count_dirs -eq 0 ]]; then
        echo "No valid directories found to create files."
        exit 1
    fi

    
    local current_folder_base="$folder_base"
    local num_dirs=$((RANDOM % 100 + 1))

    local i=0
    local j=0
    local num_files=0
    local current_folder_name=""
    local folder_path=""
    local current_file_base=""
    local file_name=""
    local file_path=""
    local size_free=0

    for (( i=0; i<num_dirs; i++ )); do
        local random_index=$((RANDOM % count_dirs))
        local current_path="${valid_dirs[random_index]}"
        current_folder_name="${current_folder_base}_${current_date}"
        folder_path="${current_path}/${current_folder_name}"

        mkdir -p "$folder_path"
        echo "[DIR] $(date "+%Y-%m-%d %H:%M:%S") $folder_path" >> "$log_file"

        current_file_base="$file_base"
        num_files=$((RANDOM % 30 + 1))

        for (( j=0; j<num_files; j++ )); do
            size_free=$(df -h / | awk 'NR==2 {print $4}')
            if [[ "$size_free" == *K* || "$size_free" == *M* ]]; then
                echo "Not enough free space to create file"
                exit 1
            fi
            if [[ $size_free = "1G" || $size_free = "1Gi" ]]; then
                echo "Not enough free space to create file"
                exit 1
            fi

            file_name="${current_file_base}_${current_date}.${file_ext}"
            file_path="${folder_path}/${file_name}"

            dd if=/dev/zero of="$file_path" bs=1M count="$size_mb" > /dev/null 2>&1
            echo "[FILE] $(date "+%Y-%m-%d %H:%M:%S") $file_path size: ${size_mb}Mb" >> "$log_file"

            current_file_base="$(create_new_name "$current_file_base")"
        done

        current_folder_base="$(create_new_name "$current_folder_base")"
    done

}
