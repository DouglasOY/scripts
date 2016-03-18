#!/bin/bash

for ((i = 0; i < 100; i++))
do
    life=life_${i}
    echo ${life}
    rm -f p5000
    head -500000 /dev/urandom > p5000
    ./life.elf  >  ${life}
done

rm -f full.dat
for ((i = 0; i < 100; i++))
do
    life=life_${i}
    echo ${life}
    cat ${life} >> full.dat
done

rm -f sum.dat sort.dat
awk '{a[$1]+=1;} END { for (x in a) { print x"    "a[x] }}' full.dat  >> sum.dat
sort -n -k 1 sum.dat  >> sort.dat



