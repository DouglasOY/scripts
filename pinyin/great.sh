#!/bin/bash


for  i in `seq 1 2`
do
    randnum=$( od -vAn -N2 -tu2 < /dev/urandom )
    line=$(( ${randnum} % 410 + 1))
    # echo  "${randnum}   ${line} "
    sed -n "${line}p" dat
done


