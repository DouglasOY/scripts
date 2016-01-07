#!/bin/bash

root=$(pwd)

# services/memorymap.h
# services/stacktrace.h
# services/memorymap.c
# services/memoryservice.c
# services/stacktrace-ext.h

for i in `cat chlist`
do
    name=$(basename $i)
    dir=$(dirname $i)
    new=${name}.new
    cd ${dir}
    unifdef -U_WIN32 -U__CYGWIN__ -U__SYMBIAN32__ -U__FreeBSD__ -U__NetBSD__ -DENABLE_AIO=0 -DENABLE_SSL=0 -DUSE_uuid_generate=0 -t ${name} -o${new}
    rm $name
    mv ${new} $name
    cd ${root}
done

