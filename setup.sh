#!/bin/bash

# MBA Dashboard Setup Script for Linux/Mac

echo ""
echo "============================================"
echo "  MBA Program KPI Dashboard Setup"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/downloads/"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "[ERROR] Node.js is not installed"
    echo "Please install Node.js 16+ from https://nodejs.org/"
    exit 1
fi

echo "[OK] Python version:"
python3 --version

echo "[OK] Node.js version:"
node --version

echo ""
echo "============================================"
echo "  Setting up Backend"
echo "============================================"
echo ""

cd backend

if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv venv
fi

echo "[INFO] Activating virtual environment..."
source venv/bin/activate

echo "[INFO] Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "============================================"
echo "  Setting up Frontend"
echo "============================================"
echo ""

cd ../frontend

echo "[INFO] Installing Node dependencies..."
npm install

echo ""
echo "============================================"
echo "  Setup Complete!"
echo "============================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Open two terminals"
echo ""
echo "Terminal 1 - Backend:"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   python app.py"
echo ""
echo "Terminal 2 - Frontend:"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "The dashboard will automatically open at http://localhost:3000"
echo ""
echo "============================================"
echo ""
