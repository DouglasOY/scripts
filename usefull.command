# get the audio, video duration.
mplayer.exe -vo null -ao null -frames 0 -identify *.(mp3|mp4|avi| wma|swf|...) | grep  "ID_LENGTH="
