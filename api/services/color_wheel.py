from api.schemas import ColorWheelCreate
from api.db import supabase

WHEEL_SELECT = "id, name, user_id, color_wheel_color(color_id, position, color(*))"

def _wheel_with_colors(response: dict) -> dict:
    rows = sorted(response["color_wheel_color"], key=lambda r: r["position"])
    colors = [r["color"] for r in rows]
    result = {
        "id": response["id"],
        "name": response["name"],
        "colors": colors,
        "user_id": response["user_id"]
    }
    return result

def get(wheel_id: int) -> dict | None:
    response = supabase.table("color_wheel").select(WHEEL_SELECT).eq("id", wheel_id).execute().data[0]
    return _wheel_with_colors(response)

def get_by_user(user_id: int) -> list:
    result = []
    response_list = supabase.table("color_wheel").select(WHEEL_SELECT).eq("user_id", user_id).execute().data
    for response in response_list:
        result.append(_wheel_with_colors(response))
    return result

def create(data: ColorWheelCreate) -> dict:
    wheel_id = supabase.rpc("create_color_wheel", {"p_name": data.name, "p_user_id": data.user_id, "p_colors_ids": data.color_ids}).execute().data
    response = supabase.table("color_wheel").select(WHEEL_SELECT).eq("id", wheel_id).execute().data[0]
    return _wheel_with_colors(response)