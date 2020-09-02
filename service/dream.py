import uuid
from dataclasses import dataclass


@dataclass
class Dreamer:
    id: str = str(uuid.uuid4())
    name: str = ""
    age: int = -1


@dataclass
class Dream:
    id: str = str(uuid.uuid4())
    dreamer: Dreamer = Dreamer()
    date: str = ""


@dataclass
class DreamerDraft:
    name: str
    age: int


@dataclass
class DreamDraft:
    dreamer: DreamerDraft
    dream: str
    date: str
