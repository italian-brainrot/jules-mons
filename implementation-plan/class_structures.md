# Core Class Structures

This document describes the Python classes that will represent the game's entities and how they will interact.

## `Creature`

The `Creature` class represents a single creature in the game.

**Attributes:**

*   `id` (str): The unique identifier for the creature.
*   `name` (str): The display name of the creature.
*   `description` (str): A brief description of the creature.
*   `types` (list of `Type`): A list of `Type` objects that the creature belongs to.
*   `stats` (dict): A dictionary of the creature's current stats (e.g., `{'hp': 80, 'attack': 90, 'defense': 70, 'speed': 100}`).
*   `moves` (list of `Move`): A list of `Move` objects that the creature can use.
*   `current_hp` (int): The creature's current health points.

**Methods:**

*   `is_alive()`: Returns `True` if the creature's `current_hp` is greater than 0, `False` otherwise.
*   `take_damage(damage)`: Reduces the creature's `current_hp` by the given amount.
*   `use_move(move, target)`: Uses a move on a target creature.

## `Move`

The `Move` class represents a move that a creature can use.

**Attributes:**

*   `id` (str): The unique identifier for the move.
*   `name` (str): The display name of the move.
*   `description` (str): A brief description of the move.
*   `type` (`Type`): The `Type` object of the move.
*   `power` (int): The power of the move.
*   `accuracy` (int): The accuracy of the move (0-100).
*   `pp` (int): The power points of the move.
*   `current_pp` (int): The current power points of the move.

## `Type`

The `Type` class represents a type in the game.

**Attributes:**

*   `id` (str): The unique identifier for the type.
*   `name` (str): The display name of the type.
*   `strengths` (list of `str`): A list of type IDs that this type is strong against.
*   `weaknesses` (list of `str`): A list of type IDs that this type is weak against.
*   `immunities` (list of `str`): A list of type IDs that this type is immune to.

**Methods:**

*   `get_damage_multiplier(target_type)`: Calculates the damage multiplier against a target type.

## `Game`

The `Game` class is the main class that manages the game state.

**Attributes:**

*   `creatures` (dict): A dictionary of all creatures in the game, keyed by their ID.
*   `moves` (dict): A dictionary of all moves in the game, keyed by their ID.
*   `types` (dict): A dictionary of all types in the game, keyed by their ID.
*   `player_party` (list of `Creature`): The player's current party of creatures.

**Methods:**

*   `load_data()`: Loads all the game data from the YAML files.
*   `start_battle(opponent_party)`: Starts a battle with an opponent's party.

## `Battle`

The `Battle` class manages the state of a battle between two trainers (or a wild creature).

**Attributes:**

*   `player_party` (list of `Creature`): The player's party.
*   `opponent_party` (list of `Creature`): The opponent's party.
*   `player_active_creature` (`Creature`): The player's currently active creature.
*   `opponent_active_creature` (`Creature`): The opponent's currently active creature.
*   `turn` (int): The current turn number.

**Methods:**

*   `start()`: Starts the battle.
*   `get_turn_order()`: Determines the turn order based on the active creatures' speed.
*   `execute_turn(player_move, opponent_move)`: Executes a turn of the battle.
*   `is_over()`: Returns `True` if the battle is over, `False` otherwise.
