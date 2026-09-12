"""Pure command-builder for assigning a simple material/color."""


def build_set_material(object_name: str, color, metallic: float, roughness: float) -> dict:
    return {
        "type": "set_material",
        "params": {
            "object_name": object_name,
            "color": list(color),
            "metallic": metallic,
            "roughness": roughness,
        },
    }
