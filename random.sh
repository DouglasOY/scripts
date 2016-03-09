#!/bin/bash

od --output-duplicates --address-radix=n --read-bytes=4 --format=u4  < /dev/urandom

dd if=/dev/urandom of=~/urandom_test count=4 bs=1024

cat /dev/urandom > ~/urandom_test2 

head -30 /dev/urandom > ~/urandom_test3

