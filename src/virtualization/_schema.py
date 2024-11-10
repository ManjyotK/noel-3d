import pydantic

class Color(pydantic.BaseModel):
    r: int
    g: int
    b: int

class Frame(pydantic.RootModel[dict[int, Color | None]]):
    pass

class Animation(pydantic.BaseModel):
    fps: int
    frames: list[Frame]
