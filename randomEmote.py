# This is the randomEmote function.  The emotes here are the default Twitch emotes that everyone has access to.
# If you add custom emotes you will need to be sure your bot has access to them

import numpy as np

def random_emote(cnt=1):
    emotes = [
        ":)",
        ":(",
        ":o",
        ":z",
        "B)",
        ":\\",
        ";)",
        ";p",
        ":p",
        "R)",
        "o_O",
        ":D",
        ">(",
        "<3",
        "4Head",
        "ANELE",
        "ArgieB8",
        "ArsonNoSexy",
        "AsianGlow",
        "BabyRage",
        "BatChest",
        "BCWarrior",
        "BegWan",
        "BibleThump",
        "BigBrother",
        "BigPhish",
        "BlargNaut",
        "bleedPurple",
        "BloodTrail",
        "BrainSlug",
        "BrokeBack",
        "BuddhaBar",
        "CarlSmile",
        "ChefFrank",
        "cmonBruh",
        "CoolCat",
        "CoolStoryBob",
        "copyThis",
        "CorgiDerp",
        "CrreamAwk",
        "CurseLit",
        "DAESuppy",
        "DansGame",
        "DatSheffy",
        "DBstyle",
        "DendiFace",
        "DogFace",
        "DoritosChip",
        "duDudu",
        "DxCat",
        "EleGiggle",
        "FailFish",
        "FrankerZ",
        "FreakinStinkin",
        "FUNgineer",
        "FutureMan",
        "GingerPower",
        "GivePLZ",
        "GrammarKing",
        "HeyGuys",
        "HotPokket",
        "imGlitch",
        "InuyoFace",
        "ItsBoshyTime",
        "Jebaited",
        "JKanStyle",
        "JonCarnage",
        "KAPOW",
        "Kappa",
        "KappaClaus",
        "KappaPride",
        "KappaRoss",
        "KappaWealth",
        "Kappu",
        "Keepo",
        "KevinTurtle",
        "Kippa",
        "KonCha",
        "Kreygasm",
        "Mau5",
        "mcaT",
        "MikeHogu",
        "MingLee",
        "MorphinTime",
        "MrDestructoid",
        "MVGame",
        "NinjaGrumpy",
        "NomNom",
        "NotATK",
        "NotLikeThis",
        "OhMyDog",
        "OneHand",
        "OpieOP",
        "OptimizePrime",
        "panicBasket",
        "PanicVis",
        "PartyTime",
        "pastaThat",
        "PeoplesChamp",
        "PermaSmug",
        "PicoMause",
        "PipeHype",
        "PJSalt",
        "PJSugar",
        "PMSTwin",
        "PogChamp",
        "Poooound",
        "PraiseIt",
        "PRChase",
        "PrimeMe",
        "PunchTrees",
        "PunOko",
        "RaccAttack",
        "RalpherZ",
        "RedCoat",
        "ResidentSleeper",
        "riPepperonis",
        "RitzMitz",
        "RlyTho",
        "RuleFive",
        "SabaPing",
        "SeemsGood",
        "ShadyLulu",
        "ShazBotstix",
        "SmoocherZ",
        "SMOrc",
        "SoBayed",
        "SoonerLater",
        "Squid1",
        "Squid2",
        "Squid3",
        "Squid4",
        "SSSsss",
        "StinkyCheese",
        "StoneLightning",
        "StrawBeary",
        "SuperVinlin",
        "SwiftRage",
        "TakeNRG",
        "TearGlove",
        "TehePelo",
        "TF2John",
        "ThankEgg",
        "TheIlluminati",
        "TheRinger",
        "TheTarFu",
        "TheThing",
        "ThunBeast",
        "TinyFace",
        "TooSpicy",
        "TriHard",
        "TTours",
        "TwitchLit",
        "twitchRaid",
        "TwitchRPG",
        "TwitchUnity",
        "UncleNox",
        "UnSane",
        "UWot",
        "VoHiYo",
        "VoteNay",
        "VoteYea",
        "WholeWheat",
        "WTRuck",
        "WutFace",
        "YouDontSay",
        "YouWHY",
    ]

    if cnt > 50:
        cnt = 50
    
    rndEmote = np.random.choice(emotes, cnt)

    rndEmote = rndEmote.tolist()
    rndEmote = " ".join(rndEmote)

    return(rndEmote)