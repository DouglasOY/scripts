#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 config"
    exit 1
else
    CFGFILE=$1
    CFGFILE_tmp1=${CFGFILE}.tmp1
    CFGFILE_tmp2=${CFGFILE}.tmp2
    CFGFILE_tmp3=${CFGFILE}.tmp3
    CFGFILE_tmp4=${CFGFILE}.tmp4
    CFGFILE_c=${CFGFILE}.c
fi

rm -f ${CFGFILE_tmp1} ${CFGFILE_tmp2} ${CFGFILE_tmp3} ${CFGFILE_tmp4} ${CFGFILE_c} 

sed -n '/^CONFIG_[^=]\+=y$/p' ${CFGFILE} > ${CFGFILE_tmp1}
sed -n '/^CONFIG_[^=]\+=m$/p' ${CFGFILE} > ${CFGFILE_tmp2}
sed -n '/^CONFIG_[^=]\+=[^ym]/p' ${CFGFILE} > ${CFGFILE_tmp3}
sed -n '/# CONFIG_[^ ]\+ is not set/p' ${CFGFILE} > ${CFGFILE_tmp4}


sed -e 's/\(CONFIG_[^=]\+\)=y/#define \1                  \/* y *\//' ${CFGFILE_tmp1} >> ${CFGFILE_c}
sed -e 's/\(CONFIG_[^=]\+\)=m/#define \1                  \/* m *\//' ${CFGFILE_tmp2} >> ${CFGFILE_c}
sed -e 's/\(CONFIG_[^=]\+\)=\(.*\)/#define \1        \2/' ${CFGFILE_tmp3} >> ${CFGFILE_c}
sed -e 's/# \(CONFIG_[^ ]\+\) is not set/\/* #undef \1 *\//' ${CFGFILE_tmp4} >> ${CFGFILE_c}

rm -f ${CFGFILE_tmp1} ${CFGFILE_tmp2} ${CFGFILE_tmp3} ${CFGFILE_tmp4} 

