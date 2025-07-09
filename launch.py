#!/usr/bin/env python3
"""
Launch script for the Supply Chain Risk Analyst AI Streamlit app
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_streamlit():
    """Run the Streamlit application"""
    print("Starting Supply Chain Risk Analyst AI...")
    print("Open your browser and navigate to: http://localhost:8501")
    print("Press Ctrl+C to stop the application")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port=8501",
            "--server.address=localhost",
            "--browser.gatherUsageStats=false"
        ])
    except KeyboardInterrupt:
        print("\nApplication stopped by user")
    except Exception as e:
        print(f"Error running application: {e}")

def main():
    """Main function"""
    print("=" * 60)
    print("Supply Chain Risk Analyst AI - Streamlit Launcher")
    print("=" * 60)
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("WARNING: .env file not found!")
        print("Please create a .env file with your API keys:")
        print("OPENAI_API_KEY=your_openai_key_here")
        print("TAVILY_API_KEY=your_tavily_key_here")
        return
    
    # Install requirements
    install_requirements()
    
    # Run the app
    run_streamlit()

if __name__ == "__main__":
    main()
