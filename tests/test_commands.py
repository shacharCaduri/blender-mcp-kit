"""Unit tests for the pure command-builder functions (no Blender needed)."""

import pytest

from engine_mcp.blender.commands import camera_light, materials, primitives, render_export, scene_query


def test_add_primitive_builds_expected_shape():
    cmd = primitives.build_add_primitive("cube", (0, 0, 0), (1, 1, 1), "Box")
    assert cmd == {
        "type": "add_primitive",
        "params": {"kind": "cube", "location": [0, 0, 0], "scale": [1, 1, 1], "name": "Box"},
    }


def test_add_primitive_rejects_unknown_kind():
    with pytest.raises(ValueError):
        primitives.build_add_primitive("teapot", (0, 0, 0), (1, 1, 1), None)


def test_set_material_builds_expected_shape():
    cmd = materials.build_set_material("Box", (1, 0, 0, 1), 0.2, 0.8)
    assert cmd["type"] == "set_material"
    assert cmd["params"]["object_name"] == "Box"


def test_add_light_rejects_unknown_kind():
    with pytest.raises(ValueError):
        camera_light.build_add_light("laser", (0, 0, 0), 1000)


def test_export_scene_rejects_unknown_format():
    with pytest.raises(ValueError):
        render_export.build_export_scene("out.xyz", "xyz")


def test_get_scene_info_has_no_params():
    assert scene_query.build_get_scene_info() == {"type": "get_scene_info", "params": {}}
