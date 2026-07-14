#!/bin/bash

execution_letters() {
    local letters="$1"
    local name=""

    for (( i=0; i<${#letters}; i++ )); do
        local char="${letters:i:1}"
        name+="$char"
    done

    if [[ ${#name} -lt 4 ]]; then
        while [[ ${#name} -lt 4 ]]; do
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
    local folder_base="$(execution_letters "$3")"
    local current_date="$(date +%d%m%y)"

    local file_mask_name="${5%.*}"
    local file_ext="${5#*.}"
    local file_base="$(execution_letters "$file_mask_name")"
    local size_kb="${6%kb}"
    local folder_path="${1}"

    local current_folder_base="$folder_base"
    local current_folder_path="$folder_path"
    log_file="${folder_path}/log_$(date +%d%m%y_%H%M%S).txt"

    for ((i=0; i<$2; i++)); do
        local folder_name="${current_folder_base}_${current_date}"
        current_folder_path+="/${folder_name}"
        mkdir -p "$current_folder_path"
        echo "[DIR] $(date "+%Y-%m-%d %H:%M:%S") $current_folder_path" >> "$log_file"
        local current_file_base="$file_base"

        for ((j=0; j<$4; j++)); do
            local file_name="${current_file_base}_${current_date}.${file_ext}"
            local file_path="${current_folder_path}/${file_name}"
            local size_free=$(df -k / | awk 'NR==2 {print $4}')
            if [[ $size_free -le 1048576 ]]; then
                echo "Not enough free space to create file: $file_path"
                exit 1
            fi
            dd if=/dev/zero of="$file_path" bs=1k count="$size_kb" > /dev/null 2>&1
            echo "[FILE] $(date "+%Y-%m-%d %H:%M:%S") $file_path size: ${size_kb}KB" >> "$log_file"
            current_file_base="$(create_new_name "$current_file_base")"
        done
        
        current_folder_base="$(create_new_name "$current_folder_base")"
        
    done
}