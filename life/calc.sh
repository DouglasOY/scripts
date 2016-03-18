#!/bin/bash

if [ $# -eq 1 ]
then
    bound=$1
    nbound=$((0 - bound))
    portion=` awk '{ if (($1 >= '${nbound}') && ($1 <= '${bound}')) t+=$2; } END {print t; }' sort.dat  `
    total=` awk '{ sum+=$2; } END {print sum }' sort.dat `
    echo " ${portion} / ${total} = "
    echo " ${portion} / ${total} " | bc -l
else
    echo "Usage: calc.sh <NUMBER>"
fi


