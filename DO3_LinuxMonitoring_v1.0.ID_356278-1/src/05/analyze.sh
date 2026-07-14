#!/bin/bash

format_size() {
    numfmt --to=iec-i --suffix=B --format="%.1f" "$1" 2>/dev/null \
    | sed 's/iB/ B/' \
    | sed 's/K B/KB/' \
    | sed 's/M B/MB/' \
    | sed 's/G B/GB/' \
    | sed 's/T B/TB/'
}

get_file_type() {
    local file="$1"

    if [[ "$file" == *.conf ]]; then
        echo "conf"
    elif [[ "$file" == *.log ]]; then
        echo "log"
    elif file -b --mime-type "$file" 2>/dev/null | grep -q '^text/'; then
        echo "text"
    elif [[ -x "$file" ]]; then
        echo "exe"
    elif file -b "$file" 2>/dev/null | grep -qi 'archive\|compressed'; then
        echo "archive"
    else
        file -b "$file" 2>/dev/null | cut -d',' -f1
    fi
}

total_folders=$(find "$dir" -type d 2>/dev/null | wc -l)

echo "Total number of folders (including all nested ones) = $total_folders"
echo "TOP 5 folders of maximum size arranged in descending order (path and size):"

find "$dir" -type d -print0 2>/dev/null | while IFS= read -r -d '' folder
do
    size=$(du -sb "$folder" 2>/dev/null | awk '{print $1}')
    echo -e "${size}\t${folder}"

done | sort -rn | head -n 5 | awk '
{
    size=$1

    $1=""

    sub(/^\t/, "", $0)

    cmd="numfmt --to=iec-i --suffix=B --format=\"%.1f\" " size
    cmd | getline human
    close(cmd)

    gsub(/iB/, " B", human)
    gsub(/K B/, "KB", human)
    gsub(/M B/, "MB", human)
    gsub(/G B/, "GB", human)
    gsub(/T B/, "TB", human)

}
'

total_files=$(find "$dir" -type f 2>/dev/null | wc -l)

conf_files=$(find "$dir" -type f -name "*.conf" 2>/dev/null | wc -l)

text_files=$(find "$dir" -type f -exec file -b --mime-type {} + 2>/dev/null | grep -c '^text/')

exec_files=$(find "$dir" -type f -executable 2>/dev/null | wc -l)

log_files=$(find "$dir" -type f -name "*.log" 2>/dev/null | wc -l)

archive_files=$(find "$dir" -type f -exec file -b {} + 2>/dev/null | grep -ci 'archive\|compressed')

sym_links=$(find "$dir" -type l 2>/dev/null | wc -l)

echo "Total number of files = $total_files"
echo "Number of:"
echo "Configuration files (with the .conf extension) = $conf_files"
echo "Text files = $text_files"
echo "Executable files = $exec_files"
echo "Log files (with the extension .log) = $log_files"
echo "Archive files = $archive_files"
echo "Symbolic links = $sym_links"


echo "TOP 10 files of maximum size arranged in descending order (path, size and type):"

find "$dir" -type f -printf '%s\t%p\n' 2>/dev/null | sort -rn | head -n 10 | while IFS=$'\t' read -r size file
do
    type=$(get_file_type "$file")
    human_size=$(format_size "$size")
    echo "$file"$'\t'"$human_size"$'\t'"$type"


done | awk -F '\t' '{print NR " - " $1 ", " $2 ", " $3}'

echo "TOP 10 executable files of the maximum size arranged in descending order (path, size and MD5 hash of file):"

find "$dir" -type f -executable -printf '%s\t%p\n' 2>/dev/null | sort -rn | head -n 10 | while IFS=$'\t' read -r size file
do
    human_size=$(format_size "$size")
    hash=$(md5sum "$file" 2>/dev/null | awk '{print $1}')
    echo "$file"$'\t'"$human_size"$'\t'"$hash"

done | awk -F '\t' '{print NR " - " $1 ", " $2 ", " $3}'