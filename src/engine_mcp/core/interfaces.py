"""The one contract every engine adapter (Blender, Unreal, ...) must meet.

Adding a new engine = implementing this class. Nothing else in the
`tools/` layer needs to change. See docs/ARCHITECTURE.md.
"""

from abc import ABC, abstractmethod
from typing import Any


class SceneEngine(ABC):
    @abstractmethod
    def connect(self) -> bool: ...

    @abstractmethod
    def add_primitive(self, kind: str, location, scale, name: str | None) -> dict[str, Any]: ...

    @abstractmethod
    def set_material(self, object_name: str, color, metallic: float, roughness: float) -> dict[str, Any]: ...

    @abstractmethod
    def set_camera(self, location, look_at) -> dict[str, Any]: ...

    @abstractmethod
    def add_light(self, kind: str, location, energy: float) -> dict[str, Any]: ...

    @abstractmethod
    def render_still(self, output_path: str) -> dict[str, Any]: ...

    @abstractmethod
    def export_scene(self, path: str, file_format: str) -> dict[str, Any]: ...

    @abstractmethod
    def get_scene_info(self) -> dict[str, Any]: ...
