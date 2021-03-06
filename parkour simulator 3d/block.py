from ursina import *
from ursina import curve

# Normal Block Class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (1, 0.8, 1)):
        super().__init__(
            model = "untitled.obj",
            scale = scale,
            collider = "box",
            texture = "dream.png",
            position = position,
            rotation = rotation,
        )

# Jump Block Class
class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "jump.obj",
            scale = Vec3(1, 0.8, 1),
            collider = "box",
            texture = "dream2.jpg",
            position = position,
            rotation = rotation
        )

# Speed Block Class
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (1, 0.5, 10)):
        super().__init__(
            model = "Speed.obj",
            scale = scale,
            color = "#53FFF5",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class EndBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = (1, 1, 4),
            color = "#2D49FB",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

# Sky Normal Block Class
class SkyNormalBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (1, 1, 1)):
        super().__init__(
            model = "normalBlock",
            collider = "mesh",
            texture = "normalBlock",
            position = position,
            rotation = rotation,
            scale = scale
        )

# Sky Jump Block Class
class SkyJumpBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "normalBlock",
            collider = "mesh",
            texture = "jumpBlock",
            position = position,
            rotation = rotation,
        )

# Sky Speed Block Class
class SkySpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "speedBlock",
            collider = "mesh",
            texture = "speedBlock",
            position = position,
            rotation = rotation,
        )
