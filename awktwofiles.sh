#!/bin/bash

awk '
NR == FNR 
{
    a[$1]=$2;
    b[$1]=$3;
    c[$1]=$4;
}

NR > FNR
{
    for (x in a) if (x == $1) { a[$1] = a[$1] / $2; }
    for (x in b) if (x == $1) { b[$1] = b[$1] / $3; }
    for (x in c) if (x == $1) { c[$1] = c[$1] / $4; }
}

END
{
    for (x in a) {print a[x]}
    for (x in b) {print b[x]}
    for (x in c) {print c[x]}
}
'
file1 file2


awk '
NR == FNR 
{
    a[$1]=$2;
    b[$1]=$3;
    c[$1]=$4;
    standard[$1]=$0;
}

NR > FNR
{
    compare[$1]=$0;
    same[$1] = 1;
    tmp1 = 1;
    tmp2 = 1;
    tmp3 = 1;
    for (x in a) 
    {
        if (x == $1) 
        { 
            if ($2 == 0)
            {
                a[$1] = 1;
            }
            else
            {
                a[$1] = a[$1] / $2; 
            }
            if ((a[x] < 0.8) || (a[x] > 1.2)) 
            {
                tmp1 = 0;
            } 
        }
    }

    for (x in b)
    {
        if (x == $1) 
        { 
            if ($3 == 0)
            {
                b[$1] = 1;
            }
            else
            {
                b[$1] = b[$1] / $3; 
            }
            if ((b[x] < 0.8) || (b[x] > 1.2)) 
            {
                tmp2 = 0;
            }
        }
    }

    for (x in c) 
    {
        if (x == $1) 
        { 
            if ($4 == 0)
            {
                c[$1] = 1;
            }
            else
            {
                c[$1] = c[$1] / $4; 
            }
            if ((c[x] < 0.8) || (c[x] > 1.2)) 
            {
                tmp3 = 0;
            }
        }
    }

    if ((tmp1 == 0) && (tmp2 == 0) && (tmp3 == 0))
    {
        same[$1] = 0;
    }
}

END
{
    for (x in same) 
    { 
        if ( same[x] == 0 ) 
        {
            print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -";
            print compare[x];
            print standard[x];
        }
    }
}
'
compare standard
 



awk ' NR == FNR { a[$1]=$2; b[$1]=$3; c[$1]=$4; standard[$1]=$0; } NR > FNR { compare[$1]=$0; same[$1] = 1; tmp1 = 1; tmp2 = 1; tmp3 = 1; for (x in a) { if (x == $1) { if ($2 == 0) { a[$1] = 1; } else { a[$1] = a[$1] / $2; } if ((a[x] < 0.8) || (a[x] > 1.2)) { tmp1 = 0; } } } for (x in b) { if (x == $1) { if ($3 == 0) { b[$1] = 1; } else { b[$1] = b[$1] / $3; } if ((b[x] < 0.8) || (b[x] > 1.2)) { tmp2 = 0; } } } for (x in c) { if (x == $1) { if ($4 == 0) { c[$1] = 1; } else { c[$1] = c[$1] / $4; } if ((c[x] < 0.8) || (c[x] > 1.2)) { tmp3 = 0; } } } if ((tmp1 == 0) && (tmp2 == 0) && (tmp3 == 0)) { same[$1] = 0; } } END { for (x in same) { if ( same[x] == 0 ) { print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"; print compare[x]; print standard[x]; } } } ' compare standard
 
