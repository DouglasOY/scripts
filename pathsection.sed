
=======samba========
[a]
printinfo = yes
path = /root/
location = 

[b]
printinfo = yes
path = /home/
location = 

[c]
printinfo = yes
path = /root/
location = 

[d]
printinfo = yes
path = /home/
location = 

[e]
printinfo = yes
path = /root/
location = 

======sed script=========

sed -n '/\[.\+\]/{
    :a; 
    H; 
    n; 
    $!{
        /\[.\+\]/!ba; 
        x; 
        /path\s*=\s*\/home/p; 
        s/.*//; 
        x; 
        s/.*/aa\n&/; 
        D; 
    };
    H;
    x;
    /path\s*=\s*\/home/p;
}' samba 

