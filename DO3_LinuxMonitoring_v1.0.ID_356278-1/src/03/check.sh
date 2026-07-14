#!/bin/bash

for param in "$1" "$2" "$3" "$4"
do
    if ! [[ "$param" =~ ^[1-6]$ ]]; then
        echo "Error: parameters must be numbers from 1 to 6. Please run the script again."
        exit 1
    fi
done

if [[ $1 -eq $2 || $3 -eq $4 ]]
then
	echo "Error: background and font colors of one column must not match. Please run the script again."
	exit 1
fi
