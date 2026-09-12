"""Pure command-builders for camera placement and lights."""

VALID_LIGHT_KINDS = {"point", "sun", "spot", "area"}


def build_set_camera(location, look_at) -> dict:
    return {"type": "set_camera", "params": {"location": list(location), "look_at": list(look_at)}}


def build_add_light(kind: str, location, energy: float) -> dict:
    if kind not in VALID_LIGHT_KINDS:
        raise ValueError(f"Unknown light kind '{kind}'. Use one of {sorted(VALID_LIGHT_KINDS)}")
    return {"type": "add_light", "params": {"kind": kind, "location": list(location), "energy": energy}}
