# get the audio, video duration.
mplayer.exe -vo null -ao null -frames 0 -identify *.(mp3|mp4|avi| wma|swf|...) | grep  "ID_LENGTH="

# the double quote is essential.
while read line ; do   mplayer.exe -vo null -ao null -frames 0 -identify  "${line}"  | grep "ID_LENGTH" ; done < list    >> durations

# 
astyle --style=linux  --indent=spaces=4 -f -p -U  -n  send.c
astyle --style=ansi --indent=spaces=4 --indent-switches --pad-oper --pad-header --add-brackets --suffix=none receive.c 

