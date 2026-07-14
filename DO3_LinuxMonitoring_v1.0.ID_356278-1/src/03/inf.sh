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

echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mHOSTNAME =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $host\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mTIMEZONE =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $zone\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mUSER =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $user\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mOS =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $os\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mDATE =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $date\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mUPTIME =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $uptime\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mUPTIME_SEC =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $uptimesec\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mIP =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $ip\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mMASK =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $mask\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mGATEWAY =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $gateway\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mRAM_TOTAL =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $totalm\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mRAM_USED =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $usedm\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mRAM_FREE =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $freem\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mSPACE_ROOT =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $space\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mSPACE_ROOT_USED =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $spaceuse\033[0m"
echo -e "\033[${txt_colors[$2]};${back_colors[$1]}mSPACE_ROOT_FREE =\033[0m\033[${txt_colors[$4]};${back_colors[$3]}m $spacefree\033[0m"
