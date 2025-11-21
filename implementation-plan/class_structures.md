# Core Class Structures

This document describes the Python classes that will represent the game's entities and how they will interact.

## `Creature`

The `Creature` class represents a single creature in the game.

**Attributes:**

*   `id` (str): The unique identifier for the creature.
*   `name` (str): The display name of the creature.
*   `description` (str): A brief description of the creature.
*   `types` (list of `Type`): A list of `Type` objects that the creature belongs to.
*   `stats` (dict): A dictionary of the creature's current stats (e.g., `{'hp': 100, 'hp_regen': 1, 'st': 100, 'st_regen': 5, 'attack': 90, 'defense': 70, 'speed': 100, 'accuracy': 100, 'evasion': 100}`).
*   `moves` (list of `Move`): A list of `Move` objects that the creature can use.
*   `current_hp` (int): The creature's current health points.
*   `current_st` (int): The creature's current stamina.

**Methods:**

*   `is_alive()`: Returns `True` if the creature's `current_hp` is greater than 0, `False` otherwise.
*   `take_damage(damage)`: Reduces the creature's `current_hp` by the given amount.
*   `use_move(move, target)`: Uses a move on a target creature.
*   `regenerate()`: Regenerates HP and ST based on regen stats.

## `Move`

The `Move` class represents a move that a creature can use.

**Attributes:**

*   `id` (str): The unique identifier for the move.
*   `name` (str): The display name of the move.
*   `description` (str): A brief description of the move.
*   `type` (`Type`): The `Type` object of the move.
*   `damage` (int): The base damage of the move.
*   `penetration` (int): The amount of defense the move ignores.
*   `accuracy` (int): The base accuracy of the move.
*   `cost` (dict): The resource cost of the move (e.g., `{'st': 25}`).
*   `cooldown` (int): The base cooldown of the move in seconds.
*   `effect` (str): The ID of a status effect to apply.

## `Type`

The `Type` class represents a type in the game.

**Attributes:**

*   `id` (str): The unique identifier for the type.
*   `name` (str): The display name of the type.
*   `effective_against` (list of `str`): A list of type IDs that this type is strong against.
*   `ineffective_against` (list of `str`): A list of type IDs that this type is weak against.
*   `immune_against` (list of `str`): A list of type IDs that this type is immune to.

**Methods:**

*   `get_damage_multiplier(target_types)`: Calculates the damage multiplier against a list of target types.

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
*   `timeline` (list): A timeline of events in the battle, used to manage turns and cooldowns.

**Methods:**

*   `start()`: Starts the battle.
*   `calculate_damage(attacker, receiver, move)`: Calculates the damage of a move.
*   `calculate_hit_chance(attacker, receiver, move)`: Calculates the chance of a move hitting.
*   `execute_turn()`: Executes the next event on the timeline.
*   `is_over()`: Returns `True` if the battle is over, `False` otherwise.
