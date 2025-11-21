# Data Schemas

This document outlines the structure of the YAML files for the game's data.

## Creatures

Creatures are the main entities in the game that players will collect and battle with.

- `id` (string, required): A unique identifier for the creature (e.g., `lion`).
- `name` (string, required): The display name of the creature (e.g., `Lion`).
- `description` (string, required): A brief description of the creature.
- `types` (list of strings, required): A list of type IDs that the creature belongs to (e.g., `['mammal', 'carnivore']`).
- `base_stats` (object, required): The base statistics of the creature.
  - `hp` (integer, required): The base health points.
  - `attack` (integer, required): The base attack power.
  - `defense` (integer, required): The base defense power.
  - `speed` (integer, required): The base speed.
- `moves` (list of strings, required): A list of move IDs that the creature can learn.

**Example:**

```yaml
- id: lion
  name: Lion
  description: A large cat of the genus Panthera native to Africa and India.
  types:
    - mammal
    - carnivore
  base_stats:
    hp: 80
    attack: 90
    defense: 70
    speed: 100
  moves:
    - roar
    - bite
    - scratch
```

## Moves

Moves are the actions that creatures can perform in battle.

- `id` (string, required): A unique identifier for the move (e.g., `bite`).
- `name` (string, required): The display name of the move (e.g., `Bite`).
- `description` (string, required): A brief description of the move.
- `type` (string, required): The type ID of the move (e.g., `normal`).
- `power` (integer, required): The power of the move.
- `accuracy` (integer, required): The accuracy of the move (0-100).
- `pp` (integer, required): The power points of the move (how many times it can be used).
- `effect` (string, optional): Any special effect the move has (e.g., `poison`).

**Example:**

```yaml
- id: bite
  name: Bite
  description: A powerful bite attack.
  type: normal
  power: 60
  accuracy: 100
  pp: 25
```

## Types

Types define the elemental properties of creatures and moves, determining their strengths and weaknesses.

- `id` (string, required): A unique identifier for the type (e.g., `mammal`).
- `name` (string, required): The display name of the type (e.g., `Mammal`).
- `strengths` (list of strings, optional): A list of type IDs that this type is strong against.
- `weaknesses` (list of strings, optional): A list of type IDs that this type is weak against.
- `immunities` (list of strings, optional): A list of type IDs that this type is immune to.

**Example:**

```yaml
- id: mammal
  name: Mammal
  strengths:
    - insect
  weaknesses:
    - poison
  immunities: []
```
