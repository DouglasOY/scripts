FOR /L %i IN (1,1,60) DO ping -n 1 192.168.0.%i | FIND /i "TTL"

