import sys
import os
import subprocess
import getpass

# Function to install dependencies
def install_dependencies():
    dependencies = ['openai', 'tkinter', 'Pillow']

    for package in dependencies:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Function to set OPENAI_API_KEY
def set_api_key():
    try:
        api_key = getpass.getpass("Enter your OpenAI API key: ")
        if api_key:
            os.environ['OPENAI_API_KEY'] = api_key
            print("API key has been set successfully.")
        else:
            print("Invalid API key.")

    except Exception as e:
        print(f"Error: {e}")

# Install dependencies
install_dependencies()

# Set OpenAI API Key
set_api_key()