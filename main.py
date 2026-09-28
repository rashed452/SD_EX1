import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY not found. Copy .env.example to .env and add your key.")

# Never print the full key
print(f"API key loaded: {API_KEY[:4]}...{API_KEY[-4:]}")
