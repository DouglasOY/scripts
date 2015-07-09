
@echo off
SETLOCAL 
call env.bat
@echo off

set IMAGESDIR=images
if not exist  %IMAGESDIR%  md %IMAGESDIR%

set OBJDIR=%envbase%\obj

set index=1

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: clean
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
set target=make first=arg1 second=arg2 clean 
call :maketarget  %target%
set /a index+=1

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: rm obj
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
call :rmobjdir

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: make
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

set target=make first=arg1 second=arg2 
call :maketarget  %target%
IF %ERRORLEVEL%==67 goto :eof
set /a index+=1

set elfpath=%OBJDIR%\first\arg1\xx.elf
call :elfexist %elfpath% xyz
IF %ERRORLEVEL%==67 goto :eof
COPY /Y %elfpath% %IMAGESDIR%\xx.elf

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::  end
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

goto :eof


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::  maketarget
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:maketarget

echo.
echo.
echo ======================     test %index%   ============================
echo.
echo.

set localcmd=%1 %2=%3  %4=%5 %6
%localcmd%

IF ERRORLEVEL 1 (
    echo.
    echo    ------------------------------------------------------------   
    echo    %localcmd%
    echo    -------------------     Failed     -------------------------
    echo.
    exit /b  67
) else (
    echo.
    echo    ------------------------------------------------------------   
    echo    %localcmd%
    echo    -------------------    Succeeded  --------------------------
    echo.
    exit /b  0
)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::  elfexist
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:elfexist

if not exist %1 (
    echo.
    echo ------------------------------------------------------------   
    echo failed to build %2 ! 
    echo ------------------------------------------------------------   
    echo.
    exit /b  67
) else (
    echo.
    echo ------------------------------------------------------------   
    echo build %2 successfully.
    echo ------------------------------------------------------------   
    echo.
    exit /b  0
)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::  rmobjdir 
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:rmobjdir 
rm -rf obj
del  /F /S /Q obj

echo.
echo ================================
echo ===========      rm -rf obj
echo ================================
echo.

exit /b 0

goto :eof




