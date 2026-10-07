from api.config import settings
from supabase import create_client

supabase = create_client(settings.supabase_url, settings.supabase_key)
