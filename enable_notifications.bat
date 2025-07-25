@echo off
cd /d "%~dp0"
set /p ENABLE_NOTIFICATIONS=Do you want to enable notifications? (Y/n):

if /i "%ENABLE_NOTIFICATIONS%"=="Y" (
    set NEWLINE=NOTIFICATIONS_ENABLED=true
) else if /i "%ENABLE_NOTIFICATIONS%"=="y" (
    set NEWLINE=NOTIFICATIONS_ENABLED=true
) else (
    set NEWLINE=NOTIFICATIONS_ENABLED=false
)

findstr /v /i "NOTIFICATIONS_ENABLED=" .env > .env.tmp

echo %NEWLINE% >> .env.tmp

move /y .env.tmp .env

echo Writing to .env file...
echo.