#!/bin/bash

function person
{
    local sum=0
    
    for i in `seq 1 1000`
    do
        local lottery=$(od --output-duplicates --address-radix=n --read-bytes=1 --format=u1  < /dev/urandom )
        if (( lottery <= 25 ))
        then
            ((sum = sum - 1))
        fi
    
        if (( lottery >= 230 ))
        then
            ((sum = sum + 1))
        fi
    done
    
    echo "${sum}"  >> result.txt
}

rm -f result.txt

for ((j=0; j<1000; j++))
do
    person
done

