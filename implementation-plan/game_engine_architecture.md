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

The `Battle` class manages the state of a single battle, including the parties, the active creatures, and the turn number.

### Turn-Based Mechanics

The battle is turn-based. In each turn:

1.  The player is prompted to choose a move for their active creature.
2.  The opponent's move is determined by a simple AI (for now, it will choose a random move).
3.  The turn order is determined by the speed of the active creatures. The creature with the higher speed goes first.
4.  The moves are executed, and the damage is calculated.
5.  The game state is updated, and the results of the turn are displayed to the player.

### Damage Calculation

The damage calculation formula will be a simplified version of the one used in Pokémon:

`damage = (((2 * level / 5 + 2) * power * attack / defense) / 50 + 2) * type_multiplier`

For the initial version, we will simplify this to:

`damage = (power * attack / defense) * type_multiplier`

The `type_multiplier` is determined by the move's type and the target creature's types.

### Battle End

A battle ends when all the creatures in one of the parties have fainted (i.e., their `current_hp` is 0). The winner is announced, and the game returns to the main menu.

## 5. Player Input

In the terminal version, player input will be handled through the command line. The game will prompt the player for input (e.g., "Choose a move:") and wait for them to enter a command.

## 6. Rendering

The game will be rendered in the terminal using `print()` statements. The display will be text-based and will show the battle scene, including the active creatures, their stats, and the available moves.
