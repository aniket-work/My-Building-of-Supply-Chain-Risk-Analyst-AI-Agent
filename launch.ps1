# PowerShell script to launch the Supply Chain Risk Analyst AI Streamlit app

Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host "Supply Chain Risk Analyst AI - Streamlit Launcher" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan

# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: Python not found. Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "WARNING: .env file not found!" -ForegroundColor Yellow
    Write-Host "Please create a .env file with your API keys:" -ForegroundColor Yellow
    Write-Host "OPENAI_API_KEY=your_openai_key_here" -ForegroundColor Yellow
    Write-Host "TAVILY_API_KEY=your_tavily_key_here" -ForegroundColor Yellow
    exit 1
}

# Install requirements
Write-Host "Installing requirements..." -ForegroundColor Blue
try {
    python -m pip install -r requirements.txt
    Write-Host "Requirements installed successfully!" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: Failed to install requirements. Please check your Python installation." -ForegroundColor Red
    exit 1
}

# Launch the Streamlit app
Write-Host "Starting Supply Chain Risk Analyst AI..." -ForegroundColor Blue
Write-Host "Open your browser and navigate to: http://localhost:8501" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Yellow
Write-Host ""

try {
    python -m streamlit run app.py --server.port=8501 --server.address=localhost --browser.gatherUsageStats=false
}
catch {
    Write-Host "Application stopped by user" -ForegroundColor Yellow
}
