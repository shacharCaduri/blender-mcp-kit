"""Placeholder for future Unreal Engine support.

Not implemented yet - this file exists so `tools/` can already depend on
the SceneEngine interface without caring which engine is behind it.
See docs/ROADMAP.md.
"""

from ..core.interfaces import SceneEngine


class UnrealEngineAdapter(SceneEngine):
    _NOT_READY = "Unreal support is planned but not implemented yet (see docs/ROADMAP.md)"

    def connect(self):
        raise NotImplementedError(self._NOT_READY)

    def add_primitive(self, kind, location, scale, name=None):
        raise NotImplementedError(self._NOT_READY)

    def set_material(self, object_name, color, metallic, roughness):
        raise NotImplementedError(self._NOT_READY)

    def set_camera(self, location, look_at):
        raise NotImplementedError(self._NOT_READY)

    def add_light(self, kind, location, energy):
        raise NotImplementedError(self._NOT_READY)

    def render_still(self, output_path):
        raise NotImplementedError(self._NOT_READY)

    def export_scene(self, path, file_format):
        raise NotImplementedError(self._NOT_READY)

    def get_scene_info(self):
        raise NotImplementedError(self._NOT_READY)
