#!/bin/bash

config_file="config.conf"

if [ ! -f "$config_file" ]; then
    echo "Error: config.conf file not found."
    exit 1
fi

source "$config_file"

raw_column1_background="$column1_background"
raw_column1_font_color="$column1_font_color"
raw_column2_background="$column2_background"
raw_column2_font_color="$column2_font_color"

column1_background=${column1_background:-$default_column1_background}
column1_font_color=${column1_font_color:-$default_column1_font_color}
column2_background=${column2_background:-$default_column2_background}
column2_font_color=${column2_font_color:-$default_column2_font_color}

for param in "$column1_background" "$column1_font_color" "$column2_background" "$column2_font_color"
do
    if ! [[ "$param" =~ ^[1-6]$ ]]; then
        echo "Error: color parameters must be numbers from 1 to 6."
        exit 1
    fi
done

if [[ "$column1_background" -eq "$column1_font_color" || "$column2_background" -eq "$column2_font_color" ]]; then
    echo "Error: background and font colors of one column must not match."
    exit 1
fi