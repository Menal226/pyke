from pyke.models.timelineDto import TimelineDto


def test_timeline_from_dict_parses_nested_payload():
    payload = {
        "metadata": {
            "dataVersion": "2",
            "matchId": "EUW1_1234567890",
            "participants": ["p1", "p2"],
        },
        "info": {
            "frameInterval": 60000,
            "participants": [{"puuid": "p1", "participantId": 1}],
            "frames": [
                {
                    "participantFrames": {
                        "1": {
                            "participantId": 1,
                            "currentGold": 350,
                            "position": {"x": 5000, "y": 5000},
                            "championStats": {"health": 700},
                            "damageStats": {"totalDamageDone": 1200},
                        }
                    },
                    "events": [
                        {
                            "timestamp": 1000,
                            "realTimestamp": 12345,
                            "type": "ITEM_PURCHASED",
                        }
                    ],
                    "timestamp": 60000,
                }
            ],
        },
    }

    result = TimelineDto.from_dict(payload)

    assert result.metadata.matchId == "EUW1_1234567890"
    assert result.metadata.participants == ["p1", "p2"]
    assert result.info.frameInterval == 60000
    assert result.info.participants[0].participantId == 1

    frame = result.info.frames[0]
    assert frame.timestamp == 60000
    assert frame.events[0].type == "ITEM_PURCHASED"

    participant_frame = frame.participantFrames.frames["1"]
    assert participant_frame.currentGold == 350
    assert participant_frame.position.x == 5000
    assert participant_frame.championStats.health == 700
    assert participant_frame.damageStats.totalDamageDone == 1200


def test_timeline_from_dict_defaults_when_missing_fields():
    result = TimelineDto.from_dict({})

    assert result.metadata.dataVersion == ""
    assert result.metadata.matchId == ""
    assert result.metadata.participants == []
    assert result.info.frameInterval == 0
    assert result.info.frames == []
    assert result.info.participants == []
