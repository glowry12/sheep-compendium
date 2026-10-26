from models.models import Sheep
from typing import Dict

class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep] = {}

    def get_sheep(self, id:int) -> Sheep:
        return self.data.get(id)

    def add_sheep(self, sheep: Sheep) -> Sheep:
        if sheep.id in self.data:
            raise ValueError("Sheep with this ID already exists")
        self.data[sheep.id] = sheep
        return sheep

db = FakeDB()
db.data = {
    1: Sheep(id=1, name="Spice", species="Gotland", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Blondie", species="Gotland", breed="Gotland", sex="ewe"),
    3: Sheep(id=3, name="Deedee", species="Gotland", breed="Gotland", sex="ewe"),
    4: Sheep(id=4, name="Rommy", species="Gotland", breed="Gotland", sex="ram"),
    5: Sheep(id=5, name="Vala", species="Gotland", breed="Gotland", sex="ewe"),
    6: Sheep(id=6, name="Esther", species="Gotland", breed="Gotland", sex="ewe"),
}

