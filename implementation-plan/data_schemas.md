# Data Schemas

This document outlines the structure of the YAML files for the game's data.

## Creatures

Creatures are the main entities in the game that players will collect and battle with.

- `id` (string, required): A unique identifier for the creature (e.g., `lion`).
- `name` (string, required): The display name of the creature (e.g., `Lion`).
- `description` (string, required): A brief description of the creature.
- `types` (list of strings, required): A list of type IDs that the creature belongs to (e.g., `['mammal', 'carnivore']`).
- `base_stats` (object, required): The base statistics of the creature. May contain additional stats such as `MP`, `MP_regen`.
  - `HP` (float, required): The base health points.
  - `HP_regen` (float, required): The base health points regenerated per second.
  - `ST` (float, required): The base stamina.
  - `ST_regen` (float, required): The base stamina regenerated per second.
  - `attack` (float, required): The base attack power.
  - `defense` (float, required): The base defense power.
  - `speed` (float, required): The base speed.
  - `accuracy` (float, required): The base accuracy.
  - `evasion` (float, required): The base evasion.
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
    HP: 100
    HP_regen: 0.5
    ST: 100
    ST_regen: 5
    attack: 90
    defense: 70
    speed: 100
    accuracy: 100
    evasion: 100
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
- `damage` (float, required): The base damage of the move.
- `penetration` (float, required): The amount of defense the move ignores.
- `accuracy` (float, required): The base accuracy of the move.
- `cost` (object, required): The resource cost of the move.
  - `<resource_name>` (float): The amount of the resource (e.g. stamina, mana, health) the move costs.
- `cooldown` (float, required): The base cooldown of the move in seconds.
- `effect` (string, optional): Any special effect the move has (e.g., `poison`).

**Example:**

```yaml
- id: bite
  name: Bite
  description: A powerful bite attack.
  type: normal
  damage: 60
  penetration: 10
  accuracy: 100
  cost:
    ST: 25
  cooldown: 5
```

## Types

Types define the elemental properties of creatures and moves, determining their strengths and weaknesses.

- `id` (string, required): A unique identifier for the type (e.g., `mammal`).
- `name` (string, required): The display name of the type (e.g., `Mammal`).
- `effectiveness` (object, optional): maps types to effectiveness values (effective, ineffective or immune)

**Example:**

```yaml
- id: electric
  name: Electric
  effectiveness:
    - water: effective
    - grass: ineffective
    - ground: immune
```

