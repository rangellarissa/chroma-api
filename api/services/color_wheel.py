from api.schemas import ColorWheelCreate, ColorWheelChange
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

def change(wheel_id: int, data: ColorWheelChange) -> dict:
    old_wheel = get(wheel_id)
    if old_wheel is None:
        return None
    
    if data.name != old_wheel["name"]:
        supabase.table("color_wheel").update({"name": data.name}).eq("id", wheel_id).execute()
    
    desired = dict(enumerate(data.colors_ids))
    rows = supabase.table("color_wheel_color").select("color_id, position").eq("color_wheel_id", wheel_id).execute().data
    old = {r["position"]: r["color_id"] for r in rows}

    for position, color_id in desired.items():
        if position not in old:
            supabase.table("color_wheel_color").insert(
                {
                    "color_wheel_id": wheel_id,
                    "position": position,
                    "color_id": color_id,
                }
            ).execute()
        elif old[position] != color_id:
            supabase.table("color_wheel_color").update({"color_id": color_id}).eq("color_wheel_id", wheel_id) \
                .eq("position", position).execute()

    for position in old.keys() - desired.keys():
        supabase.table("color_wheel_color").delete().eq("color_wheel_id", wheel_id).eq("position", position).execute()

    return get(wheel_id)

def delete(wheel_id: int) -> dict | None:
    rows = supabase.table("color_wheel").delete().eq("id", wheel_id).execute().data
    return rows[0] if rows else None