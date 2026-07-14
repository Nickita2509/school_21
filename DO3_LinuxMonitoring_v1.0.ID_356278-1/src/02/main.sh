#!/bin/bash


if [ $# -ne 0 ]
then
	echo "Must be no parametrs"
	exit 1
fi

source inf.sh

file=$(date +"%d_%m_%y_%H_%M_%S").status

read -p "Save it?(Y?n)" answer
if [[ "$answer" == 'Y' || "$answer" == "y" ]];then
	echo "$info" > $file
	echo "Data is saved"
else
	echo "Data isn't saved"
fi
