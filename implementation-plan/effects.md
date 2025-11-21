# Battle Effects

This document describes various effects that can occur during a battle, influencing creature stats and the overall outcome. These effects are applied by moves or other game mechanics.

## 1. Status Effects

Status effects are persistent conditions that affect a creature over time or until they are cured. They will be defined in a new `data/effects.yaml` file.

**Common Status Effects:**

*   **Poison:** Deals a fixed amount of damage to the creature at the end of each turn (or every few seconds in a real-time system). The damage amount can be a flat value or a percentage of the creature's max HP.
*   **Burn:** Similar to poison, but typically deals more damage. May also lower the creature's Attack stat.
*   **Paralysis:** Has a chance to prevent the creature from using a move on its turn. It may also reduce the creature's Speed stat.
*   **Freeze:** Prevents the creature from acting until it thaws. There's a chance to thaw on each turn.
*   **Sleep:** Prevents the creature from acting for a certain number of turns or until it's attacked.

**YAML Schema for Effects:**

```yaml
- id: poison
  name: Poison
  description: "Deals damage over time."
  type: status_effect
  effects:
    on_turn_end: # Or on_tick for real-time
      - type: damage
        target: self
        amount:
          percentage_of_max_hp: 6.25 # 1/16th of max HP
```

## 2. Volatile Battle Effects

These are temporary effects that are only active while the creature is in battle and can be stacked or overwritten.

*   **Stat Modifiers (Buffs/Debuffs):** Moves can temporarily increase or decrease a creature's stats (e.g., Attack, Defense, Speed). These will be implemented as multipliers.
    *   Example: An "Attack Up" buff might multiply the Attack stat by 1.5. A "Defense Down" debuff might multiply the Defense stat by 0.75.
*   **Flinch:** If a creature is made to flinch, it is prevented from using its move on that turn. This is usually caused by fast moves.
*   **Confusion:** A confused creature has a chance to attack itself instead of the intended target.

## 3. Critical Hits

A critical hit is a random chance for a move to deal extra damage.

*   **Base Critical Hit Chance:** A global game setting, e.g., 6.25% (1 in 16).
*   **Critical Hit Damage Multiplier:** A global game setting, e.g., 1.5x the normal damage.
*   **High Critical Hit Moves:** Some moves will have a higher-than-normal chance to land a critical hit.

## 4. Other Effects

*   **HP Drain / Lifesteal:** Some moves will heal the attacker for a percentage of the damage dealt.
*   **Recoil:** Some powerful moves will deal a portion of the damage dealt back to the attacker as recoil damage.
*   **Trapping:** Prevents the target creature from switching out for a certain number of turns.

These effects will be associated with moves in the `moves.yaml` files, referencing the effect by its ID.

**Example `moves.yaml` entry with an effect:**

```yaml
- id: poison-sting
  name: Poison Sting
  # ... other move stats
  effect:
    id: poison
    chance: 30 # 30% chance to apply the poison effect
```
