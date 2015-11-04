@ECHO OFF
SETLOCAL
SETLOCAL ENABLEDELAYEDEXPANSION
CALL setenv.bat
@ECHO OFF

::::  -------------------------------------------------------------------------------
::::  execfuntion      ARGA                    ARGB                         ARGC
::::  -------------------------------------------------------------------------------
CALL :execfuntion      aaaaaaaa                bbbbbb                       n
IF %ERRORLEVEL% EQU 67 GOTO :EOF
CALL :execfuntion      aaaaaaaa                bbbbbb                       y
IF %ERRORLEVEL% EQU 67 GOTO :EOF

GOTO :EOF

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: execfuntion
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:execfuntion

SET arganame=%1
SET argbname=%2
SET flag=%3

IF [%flag%] == [] (
    ECHO.
    ECHO ------------------------------------------------------------
    ECHO Please specify "flag" to n or y !
    ECHO ------------------------------------------------------------
    ECHO.
    EXIT /B  67
)

IF [%flag%] == [y] (
    SET projectpath=second_!arganame!_!argbname!
    SET libpath=first_!arganame!_!argbname!
    SET makeimage=make ARGA=!arganame! PRJPATH=!projectpath! ARGB=!argbname! ARGC=!flag! LIBPATH=!libpath!
) ELSE (
    SET projectpath=first_!arganame!_!argbname!
    SET makeimage=make ARGA=!arganame! PRJPATH=!projectpath! ARGB=!argbname!
)

SET makedefconfig=!makeimage! defconfig

::::::::::::::: defconfig :::::::::::::::
ECHO.
ECHO.
ECHO - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ECHO !makedefconfig!
ECHO - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ECHO.
ECHO.
!makedefconfig!
IF %ERRORLEVEL% GEQ 1 (
    ECHO.
    ECHO ################################################################################
    ECHO failed to !makedefconfig!
    ECHO ################################################################################
    ECHO.
    EXIT /B 67
)

::::::::::::::: image :::::::::::::::
ECHO.
ECHO.
ECHO - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ECHO !makeimage!
ECHO - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ECHO.
ECHO.
!makeimage!
IF %ERRORLEVEL% GEQ 1 (
    ECHO.
    ECHO ################################################################################
    ECHO failed to !makeimage!
    ECHO ################################################################################
    ECHO.
    EXIT /B 67
)

EXIT /B  0

GOTO :EOF

