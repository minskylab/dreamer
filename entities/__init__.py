import uuid
from dataclasses import dataclass


@dataclass
class Case:
    id: str
    client_name: str
    observations: str
    house_photo: str
    headband_photo: str

