import unittest
from src.core import Creature, Move, Type

class TestCore(unittest.TestCase):

    def setUp(self):
        # Create some dummy data for testing
        self.normal_type = Type(id='normal', name='Normal', strengths=[], weaknesses=[], immunities=[])
        self.mammal_type = Type(id='mammal', name='Mammal', strengths=['insect'], weaknesses=['poison'], immunities=[])

        self.bite_move = Move(id='bite', name='Bite', description='A powerful bite.', type=self.normal_type, power=60, accuracy=100, pp=25)

        self.lion = Creature(
            id='lion',
            name='Lion',
            description='A large cat.',
            types=[self.mammal_type],
            base_stats={'hp': 80, 'attack': 90, 'defense': 70, 'speed': 100},
            moves=[self.bite_move]
        )

        self.snake = Creature(
            id='snake',
            name='Snake',
            description='A long reptile.',
            types=[Type(id='reptile', name='Reptile', strengths=[], weaknesses=[], immunities=[])],
            base_stats={'hp': 60, 'attack': 80, 'defense': 50, 'speed': 70},
            moves=[self.bite_move]
        )

    def test_creature_is_alive(self):
        self.assertTrue(self.lion.is_alive())
        self.lion.take_damage(100)
        self.assertFalse(self.lion.is_alive())

    def test_creature_take_damage(self):
        initial_hp = self.lion.current_hp
        self.lion.take_damage(20)
        self.assertEqual(self.lion.current_hp, initial_hp - 20)

    def test_type_damage_multiplier(self):
        insect_type = Type(id='insect', name='Insect', strengths=[], weaknesses=[], immunities=[])
        poison_type = Type(id='poison', name='Poison', strengths=[], weaknesses=[], immunities=[])

        self.assertEqual(self.mammal_type.get_damage_multiplier(insect_type), 2.0)
        self.assertEqual(self.mammal_type.get_damage_multiplier(poison_type), 0.5)
        self.assertEqual(self.normal_type.get_damage_multiplier(insect_type), 1.0)

    def test_move_use(self):
        initial_hp = self.snake.current_hp
        self.lion.use_move(self.bite_move, self.snake)
        self.assertLess(self.snake.current_hp, initial_hp)

    def test_zero_defense(self):
        self.snake.stats['defense'] = 0
        initial_hp = self.snake.current_hp
        self.lion.use_move(self.bite_move, self.snake)
        self.assertLess(self.snake.current_hp, initial_hp)

if __name__ == '__main__':
    unittest.main()
