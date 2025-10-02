import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env
load_dotenv()

# Supabase configuration
SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
sb: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase() -> Client:
    return sb

# SMTP / Email Configuration
SMTP_SERVER: str = os.getenv("SMTP_SERVER")
SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
SMTP_USER: str = os.getenv("SMTP_USER")
SMTP_PASS: str = os.getenv("SMTP_PASS")
