#!/bin/bash

# updprj:
# 	@echo
# 	@echo
# 
# else
#
# ... 
# ...
#
# endif



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
sed -i -e '/^updprj:/{ N; N; N; x; :loop; N; /\nendif/! b loop; s/.*\nendif/endif/; H; x; } ' aa.mk

