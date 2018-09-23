:: D:
:: cd Program Files\Oracle\VirtualBox

cd ..\VirtualBox

set OSNAME=ubuntu1604
set SUFFIX=%OSNAME%_start.log
set SCRIPTDIR=vmscript
:: set logfile=%date:~0,4%_%date:~5,2%_%date:~8,2%_%time:~0,2%_%time:~3,2%_%time:~6,2%

VBoxManage.exe controlvm %OSNAME% poweroff

ping 123.45.67.89 -n 1 -w 3000 > nul

VBoxManage.exe showvminfo  %OSNAME%

del /f ..\%SCRIPTDIR%\%SUFFIX%

