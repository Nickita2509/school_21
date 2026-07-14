#!/bin/bash

host=$(hostname)
zone=$(timedatectl | awk -F ': ' '/Time zone/ {print $2}')
user=$(whoami)
os=$(grep PRETTY_NAME /etc/os-release | cut -d '"' -f2)
date=$(date "+%d %B %Y %T")
uptime=$(uptime -p)
uptimesec=$(awk '{print int($1)}' /proc/uptime)
ip=$(hostname -I | awk '{print $1}')
mask=$(ifconfig | head -2 | awk -F ' ' '/netmask/ {print $4}')
gateway=$(ip r | grep default | awk '{print $3}')
totalm=$(free -b | awk '/Mem:/ {printf "%.3f GB", $2/1024/1024/1024}')
usedm=$(free -b | awk '/Mem:/ {printf "%.3f GB", $3/1024/1024/1024}')
freem=$(free -b | awk '/Mem:/ {printf "%.3f GB", $4/1024/1024/1024}')
space=$(df / | awk 'NR==2 {printf "%.2f MB", $2/1024}')
spaceuse=$(df / | awk 'NR==2 {printf "%.2f MB", $3/1024}')
spacefree=$(df / | awk 'NR==2 {printf "%.2f MB", $4/1024}')

print_row() {
    local name="$1"
    local value="$2"
    echo -e "\033[${txt_colors[$column1_font_color]};${back_colors[$column1_background]}m${name} =\033[0m\033[${txt_colors[$column2_font_color]};${back_colors[$column2_background]}m ${value}\033[0m"
}

print_row "HOSTNAME" "$host"
print_row "TIMEZONE" "$zone"
print_row "USER" "$user"
print_row "OS" "$os"
print_row "DATE" "$date"
print_row "UPTIME" "$uptime"
print_row "UPTIME_SEC" "$uptimesec"
print_row "IP" "$ip"
print_row "MASK" "$mask"
print_row "GATEWAY" "$gateway"
print_row "RAM_TOTAL" "$totalm"
print_row "RAM_USED" "$usedm"
print_row "RAM_FREE" "$freem"
print_row "SPACE_ROOT" "$space"
print_row "SPACE_ROOT_USED" "$spaceuse"
print_row "SPACE_ROOT_FREE" "$spacefree"

echo

if [ -n "$raw_column1_background" ]; then
    echo "Column 1 background = $column1_background (${color_names[$column1_background]})"
else
    echo "Column 1 background = default (${color_names[$default_column1_background]})"
fi

if [ -n "$raw_column1_font_color" ]; then
    echo "Column 1 font color = $column1_font_color (${color_names[$column1_font_color]})"
else
    echo "Column 1 font color = default (${color_names[$default_column1_font_color]})"
fi

if [ -n "$raw_column2_background" ]; then
    echo "Column 2 background = $column2_background (${color_names[$column2_background]})"
else
    echo "Column 2 background = default (${color_names[$default_column2_background]})"
fi

if [ -n "$raw_column2_font_color" ]; then
    echo "Column 2 font color = $column2_font_color (${color_names[$column2_font_color]})"
else
    echo "Column 2 font color = default (${color_names[$default_column2_font_color]})"
fi