# Roadmap

- [x] Phase 1 - static scenes: primitives, materials, camera, lights, render/export
- [ ] Phase 2 - animation: keyframes, actions, simple rigging tools
- [ ] Phase 3 - asset pipeline: import meshes/textures, organize collections
- [ ] Phase 4 - Unreal Engine adapter: implement `SceneEngine` for Unreal
      (likely via Unreal's Python API + its own small socket bridge,
      mirroring `blender_addon/`)
- [ ] Phase 5 - 2D: sprite/texture generation tools, separate from the
      3D `SceneEngine` interface (own interface, e.g. `SpriteEngine`)

Each phase should stay inside the file-size and SOLID rules already in
place - see [Architecture](ARCHITECTURE.md).
