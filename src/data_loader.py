import yaml
from typing import Dict, List
from src.core import Creature, Move, Type

class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.types: Dict[str, Type] = {}
        self.moves: Dict[str, Move] = {}
        self.creatures: Dict[str, Creature] = {}

    def load_all(self):
        self.load_types()
        self.load_moves()
        self.load_creatures()

    def load_types(self):
        with open(f"{self.data_path}/types.yaml", 'r') as f:
            types_data = yaml.safe_load(f)
            for type_data in types_data:
                self.types[type_data['id']] = Type(**type_data)

    def load_moves(self):
        with open(f"{self.data_path}/moves.yaml", 'r') as f:
            moves_data = yaml.safe_load(f)
            for move_data in moves_data:
                move_data['type'] = self.types[move_data['type']]
                self.moves[move_data['id']] = Move(**move_data)

    def load_creatures(self):
        with open(f"{self.data_path}/creatures.yaml", 'r') as f:
            creatures_data = yaml.safe_load(f)
            for creature_data in creatures_data:
                creature_data['types'] = [self.types[type_id] for type_id in creature_data['types']]
                creature_data['moves'] = [self.moves[move_id] for move_id in creature_data['moves']]
                self.creatures[creature_data['id']] = Creature(**creature_data)
