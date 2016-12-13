#!/bin/bash

sed -n '/^updprj:/{
N
N
N
x
:loop
n
/^endif/! b loop
H
x
p
q
} ' aa.mk

sed -n '/^updprj:/{ N; N; N; x; :loop; n; /^endif/! b loop; H; x; p; q; } ' aa.mk

