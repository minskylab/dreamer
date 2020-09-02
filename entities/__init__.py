import uuid
from dataclasses import dataclass


@dataclass
class Dreamer:
    name: str
    id: str
    age: int


@dataclass
class Dream:
    id: str
    dreamer: Dreamer
    date: str
    registered_at: str


@dataclass
class DreamerDraft:
    name: str
    id: str = "anonymous"
    age: int = -1


@dataclass
class DreamDraft:
    dreamer: DreamerDraft
    dream: str
    date: str
