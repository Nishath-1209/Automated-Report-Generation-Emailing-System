import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = st.secrets["SUPABASE"]["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE"]["SUPABASE_KEY"]

sb: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase() -> Client:
    return sb

SMTP_SERVER = st.secrets["SMTP"]["SMTP_SERVER"]
SMTP_PORT = st.secrets["SMTP"]["SMTP_PORT"]
SMTP_USER = st.secrets["SMTP"]["SMTP_USER"]
SMTP_PASS = st.secrets["SMTP"]["SMTP_PASS"]
