from typing import List, Dict
import random

class Type:
    def __init__(self, id: str, name: str, strengths: List[str], weaknesses: List[str], immunities: List[str]):
        self.id = id
        self.name = name
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.immunities = immunities

    def get_damage_multiplier(self, target_type: 'Type') -> float:
        if target_type.id in self.strengths:
            return 2.0
        elif target_type.id in self.weaknesses:
            return 0.5
        elif target_type.id in self.immunities:
            return 0.0
        return 1.0

class Move:
    def __init__(self, id: str, name: str, description: str, type: Type, power: int, accuracy: int, pp: int, effect: str = None):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.current_pp = pp
        self.effect = effect

class Creature:
    def __init__(self, id: str, name: str, description: str, types: List[Type], base_stats: Dict[str, int], moves: List[Move]):
        self.id = id
        self.name = name
        self.description = description
        self.types = types
        self.stats = base_stats
        self.moves = moves
        self.current_hp = self.stats['hp']

    def is_alive(self) -> bool:
        return self.current_hp > 0

    def take_damage(self, damage: int):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0

    def use_move(self, move: Move, target: 'Creature'):
        print(f"{self.name} used {move.name}!")

        # Simple accuracy check
        if random.randint(1, 100) > move.accuracy:
            print(f"{self.name}'s attack missed!")
            return

        type_multiplier = 1.0
        for target_type in target.types:
            type_multiplier *= move.type.get_damage_multiplier(target_type)

        defense = target.stats['defense'] if target.stats['defense'] > 0 else 1
        damage = int((move.power * self.stats['attack'] / defense) * type_multiplier)
        target.take_damage(damage)
        print(f"It dealt {damage} damage.")
