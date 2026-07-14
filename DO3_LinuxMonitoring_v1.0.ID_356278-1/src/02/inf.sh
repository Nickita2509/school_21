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
totalm=$(free -b | awk '/Mem:/ {printf "%.3f GB\n", $2/1024/1024/1024}')
usedm=$(free -b | awk '/Mem:/ {printf "%.3f GB\n", $3/1024/1024/1024}')
freem=$(free -b | awk '/Mem:/ {printf "%.3f GB\n", $4/1024/1024/1024}')
space=$(df / | awk 'NR==2 {printf "%.2f MB", $2/1024}')
spaceuse=$(df / | awk 'NR==2 {printf "%.2f MB", $3/1024}')
spacefree=$(df / | awk 'NR==2 {printf "%.2f MB", $4/1024}')



info="HOSTNAME = $host
TIMEZONE = $zone
USER = $user
OS = $os
DATE = $date
UPTIME = $uptime
UPTIME_SEC = $uptimesec
IP = $ip
MASK = $mask
GATEWAY = $gateway
RAM_TOTAL = $totalm
RAM_USED = $usedm
RAM_FREE = $freem
SPACE_ROOT = $space
SPACE_ROOT_USED = $spaceuse
SPACE_ROOT_FREE = $spacefree"

echo "$info"

