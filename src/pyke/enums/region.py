from enum import Enum


class Region(Enum):
    """# Region to execute against"""

    BR = "br1"
    EUNE = "eun1"
    EUW = "euw1"
    JP = "jp1"
    KR = "kr"
    LAN = "la1"
    LAS = "la2"
    ME = "me1"
    NA = "na1"
    OCE = "oc1"
    RU = "ru"
    TR = "tr1"
    SG = "sg2"  # covers PH, SG, and TH — all route to the sg2 server
    TW = "tw2"
    VN = "vn2"
