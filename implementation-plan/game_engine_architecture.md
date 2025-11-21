# Game Engine Architecture

This document outlines the overall architecture of the game engine, including the game loop, battle mechanics, and how it will interact with the data.

## 1. Overview

The game engine is the core of the game, responsible for managing the game state, handling player input, and rendering the output. It is designed to be data-driven, meaning that all the game's content (creatures, moves, types, etc.) is loaded from external data files (YAML).

## 2. Data Loading and Management

At the start of the game, the `Game` class will be responsible for loading all the data from the YAML files in the `data` directory. The data will be parsed and stored in dictionaries within the `Game` object, using the `id` of each item as the key.

This approach allows for easy access to the game data and makes it simple to add new content without changing the code.

## 3. Game Loop

The game will run in a main loop that will handle the game's flow. For the initial terminal-based version, the loop will be focused on the battle system.

1.  **Initialization:** The game is initialized, and all the data is loaded.
2.  **Main Menu:** The player is presented with a main menu with options like "Start Battle" and "Quit".
3.  **Battle:** If the player chooses to start a battle, a `Battle` object is created and the battle loop begins.
4.  **Game Over:** If the player loses a battle, they are returned to the main menu.

## 4. Battle System

The battle system is the core of the game. It is managed by the `Battle` class.

### Battle Initiation

A battle is initiated by calling the `Game.start_battle()` method, which creates a `Battle` object with the player's and the opponent's parties.

### The `Battle` Class

The `Battle` class manages the state of a single battle, including the parties, the active creatures, and a timeline of events.

### Timeline-Based Mechanics

Instead of a traditional turn-based system, the battle will use a timeline to manage actions. This creates a more dynamic, continuous-time feel.

1.  At the start of the battle, both active creatures are able to act immediately.
2.  When a creature uses a move, an "action_ready" event for that creature is added to the timeline. The time of this event is calculated based on the move's cooldown and the creature's speed (`current_time + move.cooldown / creature.speed`).
3.  The game loop continuously checks the timeline for the next event.
4.  If an event is due, it is executed. For an "action_ready" event, the creature is allowed to choose its next move.
5.  Other events, such as status effect damage (e.g., poison ticks) and HP/ST regeneration, will also be added to the timeline.

This system allows faster creatures to act multiple times before a slower creature can act once.

### Damage Calculation

The damage formula is designed to be strategic and account for various factors.

`damage = (attacker.attack * move.damage) / (2 ** ((receiver.defense - move.penetration) / 100)) * type_multiplier * other_multipliers`

*   **`type_multiplier`**: Calculated based on the move's type and the receiver's types (2x for effective, 0.5x for ineffective, 0x for immune).
*   **`other_multipliers`**:  Includes effects like critical hits (1.5x damage) and status effect modifiers.

### Hit Chance Calculation

Whether a move hits is determined by the following formula:

`hit_chance = move.accuracy * (attacker.accuracy / receiver.evasion)`

A random number is generated to see if the attack is successful based on this percentage.

### Battle Effects

The engine will support various battle effects as defined in `implementation-plan/effects.md`, including:
*   **Status Effects:** Poison, burn, etc.
*   **Stat Modifiers:** Buffs and debuffs.
*   **Critical Hits:** Random chance for extra damage.

### Battle End

A battle ends when all the creatures in one of the parties have fainted (i.e., their `current_hp` is 0). The winner is announced, and the game returns to the main menu.

## 5. Player Input

In the terminal version, player input will be handled through the command line. The game will prompt the player for input when one of their creatures is ready to act.

## 6. Rendering

The game will be rendered in the terminal using `print()` statements. The display will be text-based and will show the battle scene, including the active creatures, their stats, and the available moves.
