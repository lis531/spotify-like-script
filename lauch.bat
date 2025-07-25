@echo off
cd /d "%~dp0"

if not exist "venv" (
    echo Environment not found. Run install.bat first.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
python spotify_like.py