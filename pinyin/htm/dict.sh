#!/bin/bash


# for line in `cat dat`
# do
#     wget -c http://zd.diyifanwen.com/zidian/py/${line}.htm -O ${line}.htmbak
#     iconv -f gb18030 -t utf8  ${line}.htmbak -o ${line}.htm
#     elinks -dump ${line}.htm > ${line}.txt
# done


# for line in `cat dat`
# do
#     sed -n -e '/           \[[[:digit:]]\{1\}\]/p' -e '/           \[[[:digit:]]\{2\}\]/p' -e '/           \[[[:digit:]]\{3\}\]/p' txt/${line}.txt > dict0/${line}.dict
# done


# for line in `cat dat`
# do
#     sed -n -e 's/           \[[[:digit:]]\{1\}\]/  /p' dict0/${line}.dict >  dict1/${line}.txt
#     sed -n -e 's/           \[[[:digit:]]\{2\}\]/  /p' dict0/${line}.dict >> dict1/${line}.txt
#     sed -n -e 's/           \[[[:digit:]]\{3\}\]/  /p' dict0/${line}.dict >> dict1/${line}.txt
# done


# for line in `cat dat`
# do
#     cat dict1/${line}.txt | tr -d '\n' > dict2/${line}.txt
# done


for line in `cat dat`
do
    characters=$(cat dict2/${line}.txt )
    echo "${line}    | ${characters}" >> dat1
done


