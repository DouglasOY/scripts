
awk '
{
    str=str"\n"$0; 
    if(match($0, /HOLD:/)) {
        if(matchcomm == 1) { 
            matchcomm = 0; 
            print str"\n\n"; 
            str=""; 
        }
    } else if (match($0, /COMM:/)) {
        matchcomm = 1;
    }
}' aaa > aaa.txt

