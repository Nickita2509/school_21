#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Error: script must be run with exactly 1 parameter."
    exit 1
fi

dir="$1"

if [[ "${dir: -1}" != "/" ]]; then
    echo "Error: parameter must end with '/'."
    exit 1
fi

if [[ ! -d "$dir" ]]; then
    echo "Error: directory does not exist."
    exit 1
fi