import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Read the OMDb API key
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")