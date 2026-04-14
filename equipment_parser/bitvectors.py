from typing import Mapping
import typing

ACTION_FLAGS = [
    "ACT_SPEC",
    "ACT_SENTINEL",
    "ACT_SCAVENGER",
    "ACT_ISNPC",
    "ACT_NICE_THIEF",
    "ACT_BREATHES_FIRE",
    "ACT_STAY_ZONE",
    "ACT_WIMPY",
    "ACT_BREATHES_LIGHTNING",
    "ACT_BREATHES_FROST",
    "ACT_BREATHES_ACID",
    "ACT_MEMORY",
    "ACT_IMMUNE_TO_PARA",
    "ACT_NO_SUMMON",
    "ACT_NO_BASH",
    "ACT_TEACHER",
    "ACT_IGNORE",
    "ACT_CANFLY",
    "ACT_CANSWIM",
    "ACT_BREATHES_GAS",
    "ACT_BREATHES_SHADOW",
    "ACT_BREATHES_BLIND_GAS",
    "ACT_GUILD_GOLEM",
    "ACT_SPEC_DIE",
    "ACT_ELITE",
    "ACT_BREAK_CHARM",
    "ACT_PROTECTOR",
    "ACT_MOUNT",
    "ACT_WILDMAGIC",
    "ACT_PATROL",
    "ACT_HUNTER",
    "ACT_SPEC_TEACHER"
]

ACTION2_FLAGS = [
    "ACT2_COMBAT_NEARBY",
    "ACT2_NO_LURE",
    "ACT2_REMEMBERS_GROUP",
    "ACT2_BACK_RANK",
    "ACT2_WAIT"
]

AGGRO_FLAGS = [
    "AGGR_ALL",             
    "AGGR_DAY_ONLY",        
    "AGGR_NIGHT_ONLY",      
    "AGGR_GOOD_ALIGN",      
    "AGGR_NEUTRAL_ALIGN",   
    "AGGR_EVIL_ALIGN",      
    "AGGR_GOOD_RACE",       
    "AGGR_EVIL_RACE",       
    "AGGR_UNDEAD_RACE",     
    "AGGR_OUTCASTS",        
    "AGGR_FOLLOWERS",       
    "AGGR_UNDEAD_FOL",      
    "AGGR_ELEMENTALS",      
    "AGGR_DRACOLICH",       
    "AGGR_HUMAN",           
    "AGGR_BARBARIAN",       
    "AGGR_DROW_ELF",        
    "AGGR_GREY_ELF",        
    "AGGR_MOUNT_DWARF",     
    "AGGR_DUERGAR",         
    "AGGR_HALFLING",        
    "AGGR_GNOME",           
    "AGGR_OGRE",            
    "AGGR_TROLL",           
    "AGGR_HALF_ELF",        
    "AGGR_ILLITHID",        
    "AGGR_ORC",             
    "AGGR_THRIKREEN",       
    "AGGR_CENTAUR",         
    "AGGR_GITHYANKI",       
    "AGGR_MINOTAUR",        
    "AGGR_GOBLIN",          
]

AGGRO2_FLAGS = [
    "AGGR2_ALL",            
    "AGGR2_LICH",           
    "AGGR2_PVAMPIRE",       
    "AGGR2_PDKNIGHT",       
    "AGGR2_PSBEAST",        
    "AGGR2_WARRIOR",        
    "AGGR2_RANGER",         
    "AGGR2_PSIONICIST",     
    "AGGR2_PALADIN",        
    "AGGR2_ANTIPALADIN",    
    "AGGR2_CLERIC",         
    "AGGR2_MONK",           
    "AGGR2_DRUID",          
    "AGGR2_SHAMAN",         
    "AGGR2_SORCERER",       
    "AGGR2_NECROMANCER",    
    "AGGR2_CONJURER",       
    "AGGR2_ROGUE",          
    "AGGR2_ASSASSIN",       
    "AGGR2_MERCENARY",      
    "AGGR2_BARD",           
    "AGGR2_THIEF",          
    "AGGR2_WARLOCK",        
    "AGGR2_MINDFLAYER",     
    "AGGR2_MALE",           
    "AGGR2_FEMALE",         
    "AGGR2_SGIANT",         
    "AGGR2_WIGHT",          
    "AGGR2_PHANTOM",        
    "AGGR2_SHADE",          
    "AGGR2_REVENANT",       
    "AGGR2_GITHZERAI",      
    "AGGR2_THEURGIST",      
]

AGGRO3_FLAGS = [
    "AGGR3_ALL",            
    "AGGR3_OROG",	        
    "AGGR3_DRIDER",         
    "AGGR3_KOBOLD",         
    "AGGR3_KUOTOA",         
    "AGGR3_WOODELF",        
    "AGGR3_FIRBOLG",        
    "AGGR3_AGATHINON",      
    "AGGR3_ELADRIN",        
    "AGGR3_PILLITHID",      
    "AGGR3_ALCHEMIST",      
    "AGGR3_BERSERKER",      
    "AGGR3_REAVER",         
    "AGGR3_ILLUSIONIST",    
    "AGGR3_ETHERMANCER",    
    "AGGR3_DREADLORD",      
    "AGGR3_AVENGER",        
    "AGGR3_BLIGHTER",       
    "AGGR3_SUMMONER",       
    "AGGR3_DRAGOON",        
]

AFF_FLAGS = [
    "AFF_NONE"
    "AFF_BLIND",                
    "AFF_INVISIBLE",            
    "AFF_FARSEE",               
    "AFF_DETECT_INVISIBLE",     
    "AFF_HASTE",                
    "AFF_SENSE_LIFE",           
    "AFF_MINOR_GLOBE",          
    "AFF_STONE_SKIN",           
    "AFF_UD_VISION",            
    "AFF_ARMOR",                
    "AFF_WRAITHFORM",           
    "AFF_WATERBREATH",          
    "AFF_KNOCKED_OUT",          
    "AFF_PROTECT_EVIL",         
    "AFF_BOUND",                
    "AFF_SLOW_POISON",          
    "AFF_PROTECT_GOOD",         
    "AFF_SLEEP",                
    "AFF_SKILL_AWARE",          
    "AFF_SNEAK",                
    "AFF_HIDE",                 
    "AFF_FEAR",                 
    "AFF_CHARM",                
    "AFF_MEDITATE",             
    "AFF_BARKSKIN",             
    "AFF_INFRAVISION",          
    "AFF_LEVITATE",             
    "AFF_FLY",                  
    "AFF_AWARE",                
    "AFF_PROT_FIRE",            
    "AFF_CAMPING",              
    "AFF_BIOFEEDBACK",          
    "AFF_INFERNAL_FURY",        
    "AFF_FREEDOM_OF_MVMNT",     
    "AFF_SANCTUM_DRACONIS",     
]

AFF2_FLAGS = [
    "AFF2_FIRESHIELD",          
    "AFF2_ULTRAVISION",         
    "AFF2_DETECT_EVIL",         
    "AFF2_DETECT_GOOD",         
    "AFF2_DETECT_MAGIC",        
    "AFF2_MAJOR_PHYSICAL",      
    "AFF2_PROT_COLD",           
    "AFF2_PROT_LIGHTNING",      
    "AFF2_MINOR_PARALYSIS",     
    "AFF2_MAJOR_PARALYSIS",     
    "AFF2_SLOW",                
    "AFF2_GLOBE",               
    "AFF2_PROT_GAS",            
    "AFF2_PROT_ACID",           
    "AFF2_POISONED",            
    "AFF2_SOULSHIELD",          
    "AFF2_SILENCED",            
    "AFF2_MINOR_INVIS",         
    "AFF2_VAMPIRIC_TOUCH",      
    "AFF2_STUNNED",             
    "AFF2_EARTH_AURA",          
    "AFF2_WATER_AURA",          
    "AFF2_FIRE_AURA",           
    "AFF2_AIR_AURA",            
    "AFF2_HOLDING_BREATH",      
    "AFF2_MEMORIZING",          
    "AFF2_IS_DROWNING",         
    "AFF2_PASSDOOR",            
    "AFF2_FLURRY",              
    "AFF2_CASTING",             
    "AFF2_SCRIBING",            
    "AFF2_HUNTER",              
]

AFF3_FLAGS = [
    "AFF3_TENSORS_DISC",        
    "AFF3_TRACKING",            
    "AFF3_SINGING",             
    "AFF3_ECTOPLASMIC_FORM",    
    "AFF3_ABSORBING",           
    "AFF3_PROT_ANIMAL",         
    "AFF3_SPIRIT_WARD",         
    "AFF3_GR_SPIRIT_WARD",      
    "AFF3_NON_DETECTION",       
    "AFF3_SILVER",              
    "AFF3_PLUSONE",             
    "AFF3_PLUSTWO",             
    "AFF3_PLUSTHREE",           
    "AFF3_PLUSFOUR",            
    "AFF3_PLUSFIVE",            
    "AFF3_ENLARGE",             
    "AFF3_REDUCE",              
    "AFF3_COVER",               
    "AFF3_FOUR_ARMS",           
    "AFF3_INERTIAL_BARRIER",    
    "AFF3_LIGHTNINGSHIELD",     
    "AFF3_COLDSHIELD",          
    "AFF3_CANNIBALIZE",         
    "AFF3_SWIMMING",            
    "AFF3_TOWER_IRON_WILL",     
    "AFF3_UNDERWATER",          
    "AFF3_BLUR",                
    "AFF3_ENHANCE_HEALING",     
    "AFF3_ELEMENTAL_FORM",      
    "AFF3_PASS_WITHOUT_TRACE",  
    "AFF3_PALADIN_AURA",        
    "AFF3_FAMINE",              
    "AFF3_VIVERNAE_CONCORDIA",  
]

AFF4_FLAGS = [
    "AFF4_LOOTER",                  
    "AFF4_CARRY_PLAGUE",            
    "AFF4_SACKING",                 
    "AFF4_SENSE_FOLLOWER",          
    "AFF4_STORNOGS_SPHERES",        
    "AFF4_STORNOGS_GREATER_SPHERES",
    "AFF4_VAMPIRE_FORM",            
    "AFF4_NO_UNMORPH",              
    "AFF4_HOLY_SACRIFICE",          
    "AFF4_BATTLE_ECSTASY",          
    "AFF4_DAZZLER",                 
    "AFF4_PHANTASMAL_FORM",         
    "AFF4_NOFEAR",                  
    "AFF4_REGENERATION",            
    "AFF4_DEAF",                    
    "AFF4_BATTLETIDE",              
    "AFF4_EPIC_INCREASE",           
    "AFF4_MAGE_FLAME",              
    "AFF4_GLOBE_OF_DARKNESS",       
    "AFF4_DEFLECT",                 
    "AFF4_HAWKVISION",              
    "AFF4_MULTI_CLASS",             
    "AFF4_SANCTUARY",               
    "AFF4_HELLFIRE",                
    "AFF4_SENSE_HOLINESS",          
    "AFF4_PROT_LIVING",             
    "AFF4_DETECT_ILLUSION",         
    "AFF4_ICE_AURA",                
    "AFF4_REV_POLARITY",            
    "AFF4_NEG_SHIELD",              
    "AFF4_TUPOR",                   
    "AFF4_WILDMAGIC",               
]

AFF5_FLAGS = [
    "AFF5_DAZZLEE",             
    "AFF5_MENTAL_ANGUISH",      
    "AFF5_MEMORY_BLOCK",        
    "AFF5_VINES",               
    "AFF5_ETHEREAL_ALLIANCE",   
    "AFF5_BLOOD_SCENT",         
    "AFF5_FLESH_ARMOR",         
    "AFF5_WET",                 
    "AFF5_HOLY_DHARMA",         
    "AFF5_ENH_HIDE",            
    "AFF5_LISTEN",              
    "AFF5_PROT_UNDEAD",         
    "AFF5_IMPRISON",            
    "AFF5_TITAN_FORM",          
    "AFF5_DELIRIUM",            
    "AFF5_SHADE_MOVEMENT",      
    "AFF5_NOBLIND",             
    "AFF5_MAGICAL_GLOW",        
    "AFF5_REFRESHING_GLOW",     
    "AFF5_MINE",                
    "AFF5_STANCE_OFFENSIVE",    
    "AFF5_STANCE_DEFENSIVE",    
    "AFF5_OBSCURING_MIST",      
    "AFF5_NOT_OFFENSIVE",       
    "AFF5_DECAYING_FLESH",      
    "AFF5_DREADNAUGHT",         
    "AFF5_FOREST_SIGHT",        
    "AFF5_THORNSKIN",           
    "AFF5_FOLLOWING",           
    "AFF5_ORDERING",            
    "AFF5_STONED",              
    "AFF5_JUDICIUM_FIDEI",      
]

EXTRA_FLAGS = [
    "ITEM_GLOW",            
    "ITEM_NOSHOW",          
    "ITEM_BURIED",          
    "ITEM_NOSELL",          
    "ITEM_CAN_THROW2",      
    "ITEM_INVISIBLE",       
    "ITEM_NOREPAIR",        
    "ITEM_NODROP",          
    "ITEM_RETURNING",       
    "ITEM_ALLOWED_RACES",   
    "ITEM_ALLOWED_CLASSES", 
    "ITEM_PROCLIB",         
    "ITEM_SECRET",          
    "ITEM_FLOAT",           
    "ITEM_NORESET",         
    "ITEM_NOLOCATE",        
    "ITEM_NOIDENTIFY",      
    "ITEM_NOSUMMON",        
    "ITEM_LIT",             
    "ITEM_TRANSIENT",       
    "ITEM_NOSLEEP",         
    "ITEM_NOCHARM",         
    "ITEM_TWOHANDS",        
    "ITEM_NORENT",          
    "ITEM_CAN_THROW1",      
    "ITEM_HUM",             
    "ITEM_LEVITATES",       
    "ITEM_IGNORE",          
    "ITEM_ARTIFACT",        
    "ITEM_WHOLE_BODY",      
    "ITEM_WHOLE_HEAD",      
    "ITEM_ENCRUSTED",       
]

EXTRA2_FLAGS = [
    "ITEM2_SILVER",        
    "ITEM2_BLESS",         
    "ITEM2_SLAY_GOOD",     
    "ITEM2_SLAY_EVIL",     
    "ITEM2_SLAY_UNDEAD",   
    "ITEM2_SLAY_LIVING",   
    "ITEM2_MAGIC",         
    "ITEM2_LINKABLE",      
    "ITEM2_NOPROC",        
    "ITEM2_NOTIMER",       
    "ITEM2_NOLOOT",        
    "ITEM2_CRUMBLELOOT",   
    "ITEM2_STOREITEM",     
    "ITEM2_SOULBIND",      
    "ITEM2_CRAFTED",       
    "ITEM2_QUESTITEM",     
    "ITEM2_TRANSPARENT",   
]

WEAR_FLAGS = [
    "ITEM_NONE",            
    "ITEM_TAKE",            
    "ITEM_WEAR_FINGER",     
    "ITEM_WEAR_NECK",       
    "ITEM_WEAR_BODY",       
    "ITEM_WEAR_HEAD",       
    "ITEM_WEAR_LEGS",       
    "ITEM_WEAR_FEET",       
    "ITEM_WEAR_HANDS",      
    "ITEM_WEAR_ARMS",       
    "ITEM_WEAR_SHIELD",     
    "ITEM_WEAR_ABOUT",      
    "ITEM_WEAR_WAIST",      
    "ITEM_WEAR_WRIST",      
    "ITEM_WIELD",           
    "ITEM_HOLD",            
    "ITEM_THROW",           
    "ITEM_LIGHT_SOURCE",    
    "ITEM_WEAR_EYES",       
    "ITEM_WEAR_FACE",       
    "ITEM_WEAR_EARRING",    
    "ITEM_WEAR_QUIVER",     
    "ITEM_GUILD_INSIGNIA",  
    "ITEM_WEAR_BACK",       
    "ITEM_ATTACH_BELT",     
    "ITEM_HORSE_BODY",      
    "ITEM_WEAR_TAIL",       
    "ITEM_WEAR_NOSE",       
    "ITEM_WEAR_HORN",       
    "ITEM_WEAR_IOUN",       
    "ITEM_SPIDER_BODY",     
]

CLASS_NAMES = [
    "ALL",
    "Warrior",
    "Ranger",
    "Psionicist",
    "Paladin",
    "AntiPaladin",
    "Cleric",
    "Monk",
    "Druid",
    "Shaman",
    "Sorcerer",
    "Necromancer",
    "Conjurer",
    "Rogue",
    "Assassin",
    "Mercenary",
    "Bard",
    "Thief",
    "Warlock",
    "MindFlayer",
    "Alchemist",
    "Berserker",
    "Reaver",
    "Illusionist",
    "Blighter",
    "Dreadlord",
    "Ethermancer",
    "Avenger",
    "Theurgist",
    "Summoner",
    "Dragoon",
]

RACE_NAMES = [
    "HUMAN",
    "BARBARIAN",
    "DROW",
    "GREY",
    "MOUNTAIN",
    "DUERGAR",
    "HALFLING",
    "GNOME",
    "OGRE",
    "TROLL",
    "HALFELF",
    "ILLITHID",
    "ORC",
    "THRIKREEN",
    "CENTAUR",
    "GITHYANKI",
    "MINOTAUR",
    "SHADE",
    "REVENANT",
    "GOBLIN",
    "LICH",
    "PVAMPIRE",
    "PDKNIGHT",
    "PSBEAST",
    "SGIANT",
    "WIGHT",
    "PHANTOM",
    "HARPY",
    "OROG",
    "GITHZERAI",
    "DRIDER",
    "KOBOLD",
    "PILLITHID",
    "KUOTOA",
    "WOODELF",
    "FIRBOLG",
    "TIEFLING",
]

TOTEM_SPHERES = [
    "TOTEM_LESS_ANIM",      #1     // Lesser Animal
    "TOTEM_GR_ANIM",        #2     // Greater Animal
    "TOTEM_LESS_ELEM",      #4     // Lesser Elemental
    "TOTEM_GR_ELEM",        #8     // Greater Elemental
    "TOTEM_LESS_SPIR",      #16    // Lesser Spirit
    "TOTEM_GR_SPIR"         #32    // Greater Spirit
]

def BIT(n) -> int:
    return 1 << (n - 1)


TOTEM_SPHERE_FLAGS = [
    (name, BIT(i + 1))
    for i, name in enumerate(TOTEM_SPHERES)
]

ITEM_WEAR_FLAGS = [
    (name, BIT(i + 1))
    for i, name in enumerate(WEAR_FLAGS)
]

ITEM_EXTRA1_FLAGS = [
    (name, BIT(i + 1))
    for i, name in enumerate(EXTRA_FLAGS)
]

ITEM_EXTRA2_FLAGS = [
    (name, BIT(i + 1))
    for i, name in enumerate(EXTRA2_FLAGS)
]

ITEM_CLASS_ANTI_FLAGS = [
    (name, BIT(i + 1))
    for i, name in enumerate(CLASS_NAMES)
]

ITEM_ANTI2_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(RACE_NAMES)
}

MOB_ACTION_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(ACTION_FLAGS)
}
   
MOB_AGGRO_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(AGGRO_FLAGS)
}

MOB_AGGRO2_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(AGGRO2_FLAGS)
}

MOB_AGGRO3_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(AGGRO3_FLAGS)
}

ITEM_AFF1_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(AFF_FLAGS)
}

ITEM_AFF2_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(AFF2_FLAGS)
}

ITEM_AFF3_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(AFF3_FLAGS)
}

ITEM_AFF4_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(AFF4_FLAGS)
}

ITEM_AFF5_FLAGS = {
    (name, BIT(i + 1))
    for i, name in enumerate(AFF5_FLAGS)
}


def decode_bit_flags(mask: int, table: list[tuple[str, int]]) -> list[str]:

    return [name for name, bit in table if mask & bit]

def decode_flags(mask: int, flag_map: dict[str, int], skip_zero: bool = False) -> list[str]:
    result = []

    for name, bit in flag_map.items():
        if skip_zero and bit == 0:
            continue
        if mask & bit:
            result.append(name)

    return result