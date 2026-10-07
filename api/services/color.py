from api.schemas import ColorCreate
from api.db import supabase

def get(color_id: int) -> dict | None:
    rows = supabase.table("color").select().eq("id", color_id).execute().data
    return rows[0] if rows else None

def get_by_user(user_id: int) -> list:
    rows = supabase.table("color").select().eq("user_id", user_id).execute().data
    return rows

def create(data: ColorCreate) -> dict:
    response = supabase.table("color").insert(data.model_dump()).execute()
    return response.data[0]

def change(color_id: int, data: dict) -> dict:
    rows = supabase.table("color").update(data).eq("id", color_id).execute().data
    return rows[0] if rows else None

def delete(color_id: int) -> dict | None:
    rows = supabase.table("color").delete().eq("id", color_id).execute().data
    return rows[0] if rows else None
