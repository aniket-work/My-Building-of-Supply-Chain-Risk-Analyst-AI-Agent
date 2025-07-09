# config.py
# Handles configuration management for the application.
# It loads API keys from a .env file into the environment.

import os
from dotenv import load_dotenv

def load_config():
    """
    Loads environment variables from a .env file.
    This is where you should store your API keys securely.
    Create a file named '.env' in the same directory with the following content:
    
    OPENAI_API_KEY="your_openai_api_key_here"
    TAVILY_API_KEY="your_tavily_api_key_here"
    """
    # Load the .env file from the current directory
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path=dotenv_path)
    
    # Check if the keys are loaded
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not found in .env file.")
    if not os.getenv("TAVILY_API_KEY"):
        print("Warning: TAVILY_API_KEY not found in .env file.")

