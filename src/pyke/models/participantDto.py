from dataclasses import dataclass, field
from typing import Any, Mapping

from ..enums.champion_transform import ChampionTransform
from ._coerce import to_bool, to_dict, to_int, to_str
from .challengesDto import ChallengesDto
from .missionsDto import MissionsDto
from .perksDto import PerksDto

@dataclass(slots=True, frozen=True)
class ParticipantDto:
    allInPings: int = 0
    """Yellow crossed swords"""
    assistMePings: int = 0
    """Green flag"""
    assists: int = 0
    baronKills: int = 0
    bountyLevel: int = 0
    champExperience: int = 0
    champLevel: int = 0
    championId: int = 0
    """Prior to patch 11.4, on Feb 18th, 2021, this field returned invalid championIds. We recommend determining the champion based on the championName field for matches played prior to patch 11.4."""
    championName: str = ""
    commandPings: int = 0
    """Blue generic ping (ALT+click)"""
    championTransform: ChampionTransform = ChampionTransform.NONE
    """This field is currently only utilized for Kayn's transformations. (Legal values: 0 - None, 1 - Slayer, 2 - Assassin)"""
    consumablesPurchased: int = 0
    challenges: ChallengesDto = field(default_factory=ChallengesDto)
    damageDealtToBuildings: int = 0
    damageDealtToObjectives: int = 0
    damageDealtToTurrets: int = 0
    damageSelfMitigated: int = 0
    deaths: int = 0
    detectorWardsPlaced: int = 0
    doubleKills: int = 0
    dragonKills: int = 0
    eligibleForProgression: bool = False
    enemyMissingPings: int = 0
    """Yellow questionmark"""
    enemyVisionPings: int = 0
    """Red eyeball"""
    firstBloodAssist: bool = False
    firstBloodKill: bool = False
    firstTowerAssist: bool = False
    firstTowerKill: bool = False
    gameEndedInEarlySurrender: bool = False
    """This is an offshoot of the OneStone challenge. The code checks if a spell with the same instance ID does the final point of damage to at least 2 Champions. It doesn't matter if they're enemies, but you cannot hurt your friends."""
    gameEndedInSurrender: bool = False
    holdPings: int = 0
    getBackPings: int = 0
    """Yellow circle with horizontal line"""
    goldEarned: int = 0
    goldSpent: int = 0
    individualPosition: str = ""
    """Both individualPosition and teamPosition are computed by the game server and are different versions of the most likely position played by a player. The individualPosition is the best guess for which position the player actually played in isolation of anything else. The teamPosition is the best guess for which position the player actually played if we add the constraint that each team must have one top player, one jungle, one middle, etc. Generally the recommendation is to use the teamPosition field over the individualPosition field."""
    inhibitorKills: int = 0
    inhibitorTakedowns: int = 0
    inhibitorsLost: int = 0
    item0: int = 0
    item1: int = 0
    item2: int = 0
    item3: int = 0
    item4: int = 0
    item5: int = 0
    item6: int = 0
    itemsPurchased: int = 0
    killingSprees: int = 0
    kills: int = 0
    lane: str = ""
    largestCriticalStrike: int = 0
    largestKillingSpree: int = 0
    largestMultiKill: int = 0
    longestTimeSpentLiving: int = 0
    magicDamageDealt: int = 0
    magicDamageDealtToChampions: int = 0
    magicDamageTaken: int = 0
    missions: MissionsDto = field(default_factory=MissionsDto)
    neutralMinionsKilled: int = 0
    """neutralMinionsKilled = mNeutralMinionsKilled, which is incremented on kills of kPet and kJungleMonster"""
    needVisionPings: int = 0
    """Green ward"""
    nexusKills: int = 0
    nexusTakedowns: int = 0
    nexusLost: int = 0
    objectivesStolen: int = 0
    objectivesStolenAssists: int = 0
    onMyWayPings: int = 0
    """Blue arrow pointing at ground"""
    participantId: int = 0
    playerScore0: int = 0
    playerScore1: int = 0
    playerScore2: int = 0
    playerScore3: int = 0
    playerScore4: int = 0
    playerScore5: int = 0
    playerScore6: int = 0
    playerScore7: int = 0
    playerScore8: int = 0
    playerScore9: int = 0
    playerScore10: int = 0
    playerScore11: int = 0
    pentaKills: int = 0
    perks: PerksDto = field(default_factory=PerksDto)
    physicalDamageDealt: int = 0
    physicalDamageDealtToChampions: int = 0
    physicalDamageTaken: int = 0
    placement: int = 0
    playerAugment1: int = 0
    playerAugment2: int = 0
    playerAugment3: int = 0
    playerAugment4: int = 0
    playerSubteamId: int = 0
    pushPings: int = 0
    """Green minion"""
    profileIcon: int = 0
    puuid: str = ""
    quadraKills: int = 0
    riotIdGameName: str = ""
    riotIdTagline: str = ""
    role: str = ""
    sightWardsBoughtInGame: int = 0
    spell1Casts: int = 0
    spell2Casts: int = 0
    spell3Casts: int = 0
    spell4Casts: int = 0
    subteamPlacement: int = 0
    summoner1Casts: int = 0
    summoner1Id: int = 0
    summoner2Casts: int = 0
    summoner2Id: int = 0
    summonerId: str = ""
    summonerLevel: int = 0
    summonerName: str = ""
    teamEarlySurrendered: bool = False
    teamId: int = 0
    teamPosition: str = ""
    """Both individualPosition and teamPosition are computed by the game server and are different versions of the most likely position played by a player. The individualPosition is the best guess for which position the player actually played in isolation of anything else. The teamPosition is the best guess for which position the player actually played if we add the constraint that each team must have one top player, one jungle, one middle, etc. Generally the recommendation is to use the teamPosition field over the individualPosition field."""
    timeCCingOthers: int = 0
    timePlayed: int = 0
    totalAllyJungleMinionsKilled: int = 0
    totalDamageDealt: int = 0
    totalDamageDealtToChampions: int = 0
    totalDamageShieldedOnTeammates: int = 0
    totalDamageTaken: int = 0
    totalEnemyJungleMinionsKilled: int = 0
    totalHeal: int = 0
    """Whenever positive health is applied (which translates to all heals in the game but not things like regeneration), totalHeal is incremented by the amount of health received. This includes healing enemies, jungle monsters, yourself, etc"""
    totalHealsOnTeammates: int = 0
    """Whenever positive health is applied (which translates to all heals in the game but not things like regeneration), totalHealsOnTeammates is incremented by the amount of health received. This is post modified, so if you heal someone missing 5 health for 100 you will get +5 totalHealsOnTeammates"""
    totalMinionsKilled: int = 0
    """totalMillionsKilled = mMinionsKilled, which is only incremented on kills of kTeamMinion, kMeleeLaneMinion, kSuperLaneMinion, kRangedLaneMinion and kSiegeLaneMinion"""
    totalTimeCCDealt: int = 0
    totalTimeSpentDead: int = 0
    totalUnitsHealed: int = 0
    tripleKills: int = 0
    trueDamageDealt: int = 0
    trueDamageDealtToChampions: int = 0
    trueDamageTaken: int = 0
    turretKills: int = 0
    turretTakedowns: int = 0
    turretsLost: int = 0
    unrealKills: int = 0
    visionScore: int = 0
    visionClearedPings: int = 0
    visionWardsBoughtInGame: int = 0
    wardsKilled: int = 0
    wardsPlaced: int = 0
    win: bool = False

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ParticipantDto":
        payload = dict(data or {})

        champion_transform_value = to_int(payload.get("championTransform"))
        try:
            champion_transform = ChampionTransform(champion_transform_value)
        except ValueError:
            champion_transform = ChampionTransform.NONE

        return cls(
            allInPings=to_int(payload.get("allInPings")),
            assistMePings=to_int(payload.get("assistMePings")),
            assists=to_int(payload.get("assists")),
            baronKills=to_int(payload.get("baronKills")),
            bountyLevel=to_int(payload.get("bountyLevel")),
            champExperience=to_int(payload.get("champExperience")),
            champLevel=to_int(payload.get("champLevel")),
            championId=to_int(payload.get("championId")),
            championName=to_str(payload.get("championName")),
            commandPings=to_int(payload.get("commandPings")),
            championTransform=champion_transform,
            consumablesPurchased=to_int(payload.get("consumablesPurchased")),
            challenges=ChallengesDto.from_dict(to_dict(payload.get("challenges"))),
            damageDealtToBuildings=to_int(payload.get("damageDealtToBuildings")),
            damageDealtToObjectives=to_int(payload.get("damageDealtToObjectives")),
            damageDealtToTurrets=to_int(payload.get("damageDealtToTurrets")),
            damageSelfMitigated=to_int(payload.get("damageSelfMitigated")),
            deaths=to_int(payload.get("deaths")),
            detectorWardsPlaced=to_int(payload.get("detectorWardsPlaced")),
            doubleKills=to_int(payload.get("doubleKills")),
            dragonKills=to_int(payload.get("dragonKills")),
            eligibleForProgression=to_bool(payload.get("eligibleForProgression")),
            enemyMissingPings=to_int(payload.get("enemyMissingPings")),
            enemyVisionPings=to_int(payload.get("enemyVisionPings")),
            firstBloodAssist=to_bool(payload.get("firstBloodAssist")),
            firstBloodKill=to_bool(payload.get("firstBloodKill")),
            firstTowerAssist=to_bool(payload.get("firstTowerAssist")),
            firstTowerKill=to_bool(payload.get("firstTowerKill")),
            gameEndedInEarlySurrender=to_bool(payload.get("gameEndedInEarlySurrender")),
            gameEndedInSurrender=to_bool(payload.get("gameEndedInSurrender")),
            holdPings=to_int(payload.get("holdPings")),
            getBackPings=to_int(payload.get("getBackPings")),
            goldEarned=to_int(payload.get("goldEarned")),
            goldSpent=to_int(payload.get("goldSpent")),
            individualPosition=to_str(payload.get("individualPosition")),
            inhibitorKills=to_int(payload.get("inhibitorKills")),
            inhibitorTakedowns=to_int(payload.get("inhibitorTakedowns")),
            inhibitorsLost=to_int(payload.get("inhibitorsLost")),
            item0=to_int(payload.get("item0")),
            item1=to_int(payload.get("item1")),
            item2=to_int(payload.get("item2")),
            item3=to_int(payload.get("item3")),
            item4=to_int(payload.get("item4")),
            item5=to_int(payload.get("item5")),
            item6=to_int(payload.get("item6")),
            itemsPurchased=to_int(payload.get("itemsPurchased")),
            killingSprees=to_int(payload.get("killingSprees")),
            kills=to_int(payload.get("kills")),
            lane=to_str(payload.get("lane")),
            largestCriticalStrike=to_int(payload.get("largestCriticalStrike")),
            largestKillingSpree=to_int(payload.get("largestKillingSpree")),
            largestMultiKill=to_int(payload.get("largestMultiKill")),
            longestTimeSpentLiving=to_int(payload.get("longestTimeSpentLiving")),
            magicDamageDealt=to_int(payload.get("magicDamageDealt")),
            magicDamageDealtToChampions=to_int(payload.get("magicDamageDealtToChampions")),
            magicDamageTaken=to_int(payload.get("magicDamageTaken")),
            missions=MissionsDto.from_dict(to_dict(payload.get("missions"))),
            neutralMinionsKilled=to_int(payload.get("neutralMinionsKilled")),
            needVisionPings=to_int(payload.get("needVisionPings")),
            nexusKills=to_int(payload.get("nexusKills")),
            nexusTakedowns=to_int(payload.get("nexusTakedowns")),
            nexusLost=to_int(payload.get("nexusLost")),
            objectivesStolen=to_int(payload.get("objectivesStolen")),
            objectivesStolenAssists=to_int(payload.get("objectivesStolenAssists")),
            onMyWayPings=to_int(payload.get("onMyWayPings")),
            participantId=to_int(payload.get("participantId")),
            playerScore0=to_int(payload.get("playerScore0")),
            playerScore1=to_int(payload.get("playerScore1")),
            playerScore2=to_int(payload.get("playerScore2")),
            playerScore3=to_int(payload.get("playerScore3")),
            playerScore4=to_int(payload.get("playerScore4")),
            playerScore5=to_int(payload.get("playerScore5")),
            playerScore6=to_int(payload.get("playerScore6")),
            playerScore7=to_int(payload.get("playerScore7")),
            playerScore8=to_int(payload.get("playerScore8")),
            playerScore9=to_int(payload.get("playerScore9")),
            playerScore10=to_int(payload.get("playerScore10")),
            playerScore11=to_int(payload.get("playerScore11")),
            pentaKills=to_int(payload.get("pentaKills")),
            perks=PerksDto.from_dict(to_dict(payload.get("perks"))),
            physicalDamageDealt=to_int(payload.get("physicalDamageDealt")),
            physicalDamageDealtToChampions=to_int(payload.get("physicalDamageDealtToChampions")),
            physicalDamageTaken=to_int(payload.get("physicalDamageTaken")),
            placement=to_int(payload.get("placement")),
            playerAugment1=to_int(payload.get("playerAugment1")),
            playerAugment2=to_int(payload.get("playerAugment2")),
            playerAugment3=to_int(payload.get("playerAugment3")),
            playerAugment4=to_int(payload.get("playerAugment4")),
            playerSubteamId=to_int(payload.get("playerSubteamId")),
            pushPings=to_int(payload.get("pushPings")),
            profileIcon=to_int(payload.get("profileIcon")),
            puuid=to_str(payload.get("puuid")),
            quadraKills=to_int(payload.get("quadraKills")),
            riotIdGameName=to_str(payload.get("riotIdGameName")),
            riotIdTagline=to_str(payload.get("riotIdTagline")),
            role=to_str(payload.get("role")),
            sightWardsBoughtInGame=to_int(payload.get("sightWardsBoughtInGame")),
            spell1Casts=to_int(payload.get("spell1Casts")),
            spell2Casts=to_int(payload.get("spell2Casts")),
            spell3Casts=to_int(payload.get("spell3Casts")),
            spell4Casts=to_int(payload.get("spell4Casts")),
            subteamPlacement=to_int(payload.get("subteamPlacement")),
            summoner1Casts=to_int(payload.get("summoner1Casts")),
            summoner1Id=to_int(payload.get("summoner1Id")),
            summoner2Casts=to_int(payload.get("summoner2Casts")),
            summoner2Id=to_int(payload.get("summoner2Id")),
            summonerId=to_str(payload.get("summonerId")),
            summonerLevel=to_int(payload.get("summonerLevel")),
            summonerName=to_str(payload.get("summonerName")),
            teamEarlySurrendered=to_bool(payload.get("teamEarlySurrendered")),
            teamId=to_int(payload.get("teamId")),
            teamPosition=to_str(payload.get("teamPosition")),
            timeCCingOthers=to_int(payload.get("timeCCingOthers")),
            timePlayed=to_int(payload.get("timePlayed")),
            totalAllyJungleMinionsKilled=to_int(payload.get("totalAllyJungleMinionsKilled")),
            totalDamageDealt=to_int(payload.get("totalDamageDealt")),
            totalDamageDealtToChampions=to_int(payload.get("totalDamageDealtToChampions")),
            totalDamageShieldedOnTeammates=to_int(payload.get("totalDamageShieldedOnTeammates")),
            totalDamageTaken=to_int(payload.get("totalDamageTaken")),
            totalEnemyJungleMinionsKilled=to_int(payload.get("totalEnemyJungleMinionsKilled")),
            totalHeal=to_int(payload.get("totalHeal")),
            totalHealsOnTeammates=to_int(payload.get("totalHealsOnTeammates")),
            totalMinionsKilled=to_int(payload.get("totalMinionsKilled")),
            totalTimeCCDealt=to_int(payload.get("totalTimeCCDealt")),
            totalTimeSpentDead=to_int(payload.get("totalTimeSpentDead")),
            totalUnitsHealed=to_int(payload.get("totalUnitsHealed")),
            tripleKills=to_int(payload.get("tripleKills")),
            trueDamageDealt=to_int(payload.get("trueDamageDealt")),
            trueDamageDealtToChampions=to_int(payload.get("trueDamageDealtToChampions")),
            trueDamageTaken=to_int(payload.get("trueDamageTaken")),
            turretKills=to_int(payload.get("turretKills")),
            turretTakedowns=to_int(payload.get("turretTakedowns")),
            turretsLost=to_int(payload.get("turretsLost")),
            unrealKills=to_int(payload.get("unrealKills")),
            visionScore=to_int(payload.get("visionScore")),
            visionClearedPings=to_int(payload.get("visionClearedPings")),
            visionWardsBoughtInGame=to_int(payload.get("visionWardsBoughtInGame")),
            wardsKilled=to_int(payload.get("wardsKilled")),
            wardsPlaced=to_int(payload.get("wardsPlaced")),
            win=to_bool(payload.get("win")),
        )


