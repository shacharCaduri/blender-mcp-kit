"""Pure functions that build the JSON command for primitive shapes.

No I/O here - see adapter.py for the code that actually sends these.
"""

VALID_KINDS = {"cube", "sphere", "cylinder", "cone", "plane"}


def build_add_primitive(kind: str, location, scale, name: str | None) -> dict:
    if kind not in VALID_KINDS:
        raise ValueError(f"Unknown primitive '{kind}'. Use one of {sorted(VALID_KINDS)}")
    return {
        "type": "add_primitive",
        "params": {
            "kind": kind,
            "location": list(location),
            "scale": list(scale),
            "name": name,
        },
    }
