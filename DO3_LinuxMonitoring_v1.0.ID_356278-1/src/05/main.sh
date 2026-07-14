#!/bin/bash

start_time=$(date +%s)

source ./check.sh
source ./analyze.sh

end_time=$(date +%s)
execution_time=$((end_time - start_time))
echo "Execution time: $execution_time seconds"


