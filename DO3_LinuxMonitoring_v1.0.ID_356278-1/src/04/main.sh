#!/bin/bash

if [ $# -ne 0 ]; then
    echo "Error: script must be run without parameters."
    exit 1
fi

source color.sh
source check.sh
source inf.sh