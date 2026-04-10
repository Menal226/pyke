from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int


@dataclass(slots=True, frozen=True)
class ChampionStatsDto:
    abilityHaste: int = 0
    abilityPower: int = 0
    armor: int = 0
    armorPen: int = 0
    armorPenPercent: int = 0
    attackDamage: int = 0
    attackSpeed: int = 0
    bonusArmorPenPercent: int = 0
    bonusMagicPenPercent: int = 0
    ccReduction: int = 0
    cooldownReduction: int = 0
    health: int = 0
    healthMax: int = 0
    healthRegen: int = 0
    lifesteal: int = 0
    magicPen: int = 0
    magicPenPercent: int = 0
    magicResist: int = 0
    movementSpeed: int = 0
    omnivamp: int = 0
    physicalVamp: int = 0
    power: int = 0
    powerMax: int = 0
    powerRegen: int = 0
    spellVamp: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ChampionStatsDto":
        payload = dict(data or {})
        return cls(
            abilityHaste=to_int(payload.get("abilityHaste")),
            abilityPower=to_int(payload.get("abilityPower")),
            armor=to_int(payload.get("armor")),
            armorPen=to_int(payload.get("armorPen")),
            armorPenPercent=to_int(payload.get("armorPenPercent")),
            attackDamage=to_int(payload.get("attackDamage")),
            attackSpeed=to_int(payload.get("attackSpeed")),
            bonusArmorPenPercent=to_int(payload.get("bonusArmorPenPercent")),
            bonusMagicPenPercent=to_int(payload.get("bonusMagicPenPercent")),
            ccReduction=to_int(payload.get("ccReduction")),
            cooldownReduction=to_int(payload.get("cooldownReduction")),
            health=to_int(payload.get("health")),
            healthMax=to_int(payload.get("healthMax")),
            healthRegen=to_int(payload.get("healthRegen")),
            lifesteal=to_int(payload.get("lifesteal")),
            magicPen=to_int(payload.get("magicPen")),
            magicPenPercent=to_int(payload.get("magicPenPercent")),
            magicResist=to_int(payload.get("magicResist")),
            movementSpeed=to_int(payload.get("movementSpeed")),
            omnivamp=to_int(payload.get("omnivamp")),
            physicalVamp=to_int(payload.get("physicalVamp")),
            power=to_int(payload.get("power")),
            powerMax=to_int(payload.get("powerMax")),
            powerRegen=to_int(payload.get("powerRegen")),
            spellVamp=to_int(payload.get("spellVamp")),
        )
