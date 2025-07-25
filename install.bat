@echo off
cd /d "%~dp0"

REM Check for Python
where py >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install it from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Create virtualenv if missing
if not exist "venv" (
    echo Creating virtual environment...
    py -m venv venv
)

REM Activate venv
call venv\Scripts\activate.bat

REM Install pip packages
echo Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt

REM Prompt for Spotify client ID/secret
echo.
set /p CLIENT_ID=Enter your Spotify Client ID: 
set /p CLIENT_SECRET=Enter your Spotify Client Secret:
set /p ENABLE_NOTIFICATIONS=Do you want to enable notifications? (Y/n):
if /i "%ENABLE_NOTIFICATIONS%"=="Y" (
    set ENABLE_NOTIFICATIONS=true
) else if /i "%ENABLE_NOTIFICATIONS%"=="y" (
    set ENABLE_NOTIFICATIONS=true
) else (
    set ENABLE_NOTIFICATIONS=false
)

REM Save to .env
echo Writing to .env file...
(
  echo SPOTIFY_CLIENT_ID=%CLIENT_ID%
  echo SPOTIFY_CLIENT_SECRET=%CLIENT_SECRET%
  echo NOTIFICATIONS_ENABLED=%ENABLE_NOTIFICATIONS%
) > .env

echo.
echo Setup complete. You can now run launch.bat to start the program.
pause
