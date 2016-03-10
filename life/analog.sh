#!/bin/bash

for ((i = 0; i < 100; i++))
do
    life=life_${i}
    echo ${life}
    rm -f p5000
    head -500000 /dev/urandom > p5000
    ./life.elf  >  ${life}
done


for ((i = 0; i < 100; i++))
do
    life=life_${i}
    echo ${life}
    cat ${life} >> full.dat
done


