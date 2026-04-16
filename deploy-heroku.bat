@echo off
REM Heroku Deployment Script for Windows

echo.
echo ============================================
echo  Preparing for Heroku Deployment
echo ============================================
echo.

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

REM Check if Heroku CLI is installed
heroku --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Heroku CLI is not installed
    echo Please install from https://devcenter.heroku.com/articles/heroku-cli
    pause
    exit /b 1
)

echo [OK] Node.js version:
node --version

echo [OK] Heroku CLI version:
heroku --version

echo.
echo ============================================
echo  Step 1: Building Frontend
echo ============================================
echo.

cd frontend
call npm run build

if %errorlevel% neq 0 (
    echo [ERROR] Frontend build failed
    pause
    exit /b 1
)

cd ..

echo [OK] Frontend built successfully

echo.
echo ============================================
echo  Step 2: Initializing Git
echo ============================================
echo.

if not exist ".git" (
    echo [INFO] Initializing Git repository...
    call git init
    call git add .
    call git commit -m "Initial commit: MBA KPI Dashboard ready for Heroku"
) else (
    echo [INFO] Git repository already exists
    call git add .
    call git commit -m "Update: MBA KPI Dashboard" || echo [INFO] No changes to commit
)

echo [OK] Git ready

echo.
echo ============================================
echo  Step 3: Ready for Heroku Deployment
echo ============================================
echo.

echo To deploy:
echo.
echo 1. Login to Heroku:
echo    heroku login
echo.
echo 2. Create app:
echo    heroku create your-app-name
echo.
echo 3. Deploy:
echo    git push heroku main
echo.
echo 4. Open app:
echo    heroku open
echo.

pause
