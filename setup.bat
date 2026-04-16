@echo off
REM MBA Dashboard Setup Script for Windows

echo.
echo ============================================
echo  MBA Program KPI Dashboard Setup
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed or not in PATH
    echo Please install Node.js 16+ from https://nodejs.org/
    pause
    exit /b 1
)

echo [OK] Python version:
python --version

echo [OK] Node.js version:
node --version

echo.
echo ============================================
echo  Setting up Backend
echo ============================================
echo.

cd backend

if not exist venv (
    echo [INFO] Creating virtual environment...
    python -m venv venv
)

echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

echo [INFO] Installing Python dependencies...
pip install -r requirements.txt

echo.
echo ============================================
echo  Setting up Frontend
echo ============================================
echo.

cd ..\frontend

echo [INFO] Installing Node dependencies...
call npm install

echo.
echo ============================================
echo  Setup Complete!
echo ============================================
echo.
echo Next steps:
echo.
echo 1. Open two terminals/command prompts
echo.
echo Terminal 1 - Backend:
echo   cd backend
echo   venv\Scripts\activate.bat
echo   python app.py
echo.
echo Terminal 2 - Frontend:
echo   cd frontend
echo   npm run dev
echo.
echo The dashboard will automatically open at http://localhost:3000
echo.
echo ============================================
echo.
pause
