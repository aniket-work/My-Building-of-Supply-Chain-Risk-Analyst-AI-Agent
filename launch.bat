@echo off
cls
echo ============================================================
echo Supply Chain Risk Analyst AI - Streamlit Launcher
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Please create a .env file with your API keys:
    echo OPENAI_API_KEY=your_openai_key_here
    echo TAVILY_API_KEY=your_tavily_key_here
    pause
    exit /b 1
)

REM Install requirements
echo Installing requirements...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install requirements.
    pause
    exit /b 1
)

REM Launch the Streamlit app
echo.
echo Starting Supply Chain Risk Analyst AI...
echo Open your browser and navigate to: http://localhost:8501
echo Press Ctrl+C to stop the application
echo.

python -m streamlit run app.py --server.port=8501 --server.address=localhost --browser.gatherUsageStats=false

pause
