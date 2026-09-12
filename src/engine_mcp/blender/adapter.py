"""Implements SceneEngine by sending built commands over a BlenderConnection.

This is the only file that wires 'command builders' to 'transport'.
"""

from ..core.errors import EngineCommandError
from ..core.interfaces import SceneEngine
from .commands import camera_light, materials, primitives, render_export, scene_query
from .connection import BlenderConnection


class BlenderEngineAdapter(SceneEngine):
    def __init__(self, connection: BlenderConnection | None = None):
        self._conn = connection or BlenderConnection()

    def connect(self) -> bool:
        self._conn.connect()
        return True

    def _send(self, command: dict) -> dict:
        response = self._conn.send_json(command)
        if not response.get("ok", False):
            raise EngineCommandError(command["type"], response.get("error", "unknown error"))
        return response.get("result", {})

    def add_primitive(self, kind, location, scale, name=None):
        return self._send(primitives.build_add_primitive(kind, location, scale, name))

    def set_material(self, object_name, color, metallic=0.0, roughness=0.5):
        return self._send(materials.build_set_material(object_name, color, metallic, roughness))

    def set_camera(self, location, look_at):
        return self._send(camera_light.build_set_camera(location, look_at))

    def add_light(self, kind, location, energy=1000.0):
        return self._send(camera_light.build_add_light(kind, location, energy))

    def render_still(self, output_path):
        return self._send(render_export.build_render_still(output_path))

    def export_scene(self, path, file_format):
        return self._send(render_export.build_export_scene(path, file_format))

    def get_scene_info(self):
        return self._send(scene_query.build_get_scene_info())
