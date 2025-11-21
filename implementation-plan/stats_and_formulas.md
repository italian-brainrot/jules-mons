# Stats and Formulas

This document provides a detailed description of all the stats for creatures and moves, as well as the formulas used in the game's mechanics.

## Creature Stats

Creature stats are the primary attributes that determine a creature's performance in battle. All stats are unbounded.

*   **HP (Health Points):** Represents the creature's health. When a creature's HP reaches 0, it faints and can no longer battle.
*   **HP Regen:** The amount of HP regenerated per second.
*   **ST (Stamina):** The resource used to perform moves. A creature cannot use a move if it doesn't have enough ST.
*   **ST Regen:** The amount of ST regenerated per second.
*   **Attack:** The creature's physical and special attack power. This stat is used in the damage formula.
*   **Defense:** The creature's physical and special defense. This stat is used in the damage formula to mitigate incoming damage.
*   **Speed:**  Determines how quickly a creature can act. It's a multiplier that affects the cooldown time after using a move. A higher speed means a shorter cooldown.
*   **Accuracy:** The creature's ability to hit a target.
*   **Evasion:** The creature's ability to evade an attack.

## Move Stats

Move stats define the properties of a move.

*   **Damage:** The base damage of the move.
*   **Penetration:** The amount of the target's defense that the move ignores.
*   **Cost:** The amount of ST (or other resource) required to use the move. The resource type can be defined in the YAML file (e.g., `cost: {stamina: 20}`).
*   **Cooldown:** The base time in seconds a creature has to wait before it can perform another action. This is divided by the creature's speed.
*   **Accuracy:** The base accuracy of the move.

## Formulas

### Damage Formula

The damage formula is designed to be strategic and account for various factors.

`damage = (attacker.attack * move.damage) / (2 ** ((receiver.defense - move.penetration) / 100)) * type_multiplier * other_multipliers`

*   **`attacker.attack`**: The attack stat of the attacking creature.
*   **`move.damage`**: The base damage of the move.
*   **`receiver.defense`**: The defense stat of the receiving creature.
*   **`move.penetration`**: The penetration stat of the move.
*   **`type_multiplier`**: Calculated based on the move's type and the receiver's types.
    *   Multiplied by 2 for each effective type match.
    *   Divided by 2 for each inefficient type match.
    *   Multiplied by 0 if there is an immune type match.
*   **`other_multipliers`**:  A placeholder for other potential multipliers, such as status effects (e.g., 'buffed', 'debuffed') or critical hits.

### Type Effectiveness

Type effectiveness will be defined in the `types.yaml` file.

**Example `types.yaml`:**

```yaml
- id: electric
  name: Electric
  effectiveness:
    - water: effective
    - grass: ineffective
    - ground: immune
```

### Accuracy/Evasion Formula

The formula for determining if a move hits is as follows:

`hit_chance = move.accuracy * (attacker.accuracy / receiver.evasion)`

The hit chance is a percentage. A random number between 0 and 100 is generated, and if it's less than or equal to the `hit_chance`, the move hits.

### Cooldown Formula

The cooldown after a move determines when the creature can act again.

`cooldown = move.cooldown / attacker.speed`

This means that creatures with higher speed will have shorter cooldowns and can attack more frequently.

## Other Considerations

### Status Effects

Status effects (e.g., poison, paralysis, burn) can temporarily alter a creature's stats or inflict damage over time. These will be defined in a new `effects.yaml` file and can be applied by moves.

### Critical Hits

A critical hit is a random chance to deal extra damage. The probability of a critical hit and the damage multiplier will be defined as global game settings, but could be modified by creature abilities or items in the future.

### Resources for Moves

While ST (Stamina) is the primary resource, the system will be flexible enough to support other resources like Mana. The cost of a move will be defined in the move's data, specifying the resource and the amount.

**Example `moves.yaml` entry:**

```yaml
- id: fireball
  name: Fireball
  # ... other stats
  cost:
    mana: 20
```

This allows for different types of creatures and moves with unique resource management.
