from supabase import create_client, Client

# Replace with your Supabase project credentials
SUPABASE_URL = "https://pqicqomvsigqxumnhlak.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBxaWNxb212c2lncXh1bW5obGFrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDkyMDI1NDIsImV4cCI6MjA2NDc3ODU0Mn0.vP1dZI9kRiMxnK5eaTOwrkW9WtDmRRyywOUxdFS5Vuw"

def init_supabase() -> Client:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase
