@echo off
cd /d "%~dp0"

REM Check for Python
where python >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install it from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Create virtualenv if missing
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
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

REM Save to .env
echo Writing to .env file...
(
  echo CLIENT_ID=%CLIENT_ID%
  echo CLIENT_SECRET=%CLIENT_SECRET%
) > .env

echo.
echo Setup complete. You can now run launch.bat to start the program.
pause
