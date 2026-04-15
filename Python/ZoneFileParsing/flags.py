item_type_lookup = {
    1:  "ITEM_LIGHT",       # an illuminating object (also ITEM_LOWEST)
    2:  "ITEM_SCROLL",      # spells to be 'recited'
    3:  "ITEM_WAND",        # contains spells to 'use'
    4:  "ITEM_STAFF",       # also contains spells to 'use' (area affect)
    5:  "ITEM_WEAPON",      # for hurting things
    6:  "ITEM_FIREWEAPON",  # weapon used to fire others (bows, slings...)
    7:  "ITEM_MISSILE",     # arrow, bolt, ballista missile...
    8:  "ITEM_TREASURE",    # is intrinsically valuable
    9:  "ITEM_ARMOR",       # a piece of equipment granting physical prot.
    10: "ITEM_POTION",      # for the quaffing
    11: "ITEM_WORN",        # non-armor clothing items
    12: "ITEM_OTHER",       # miscellaneous things
    13: "ITEM_TRASH",       # OTHER (less useful) miscellaneous things
    14: "ITEM_WALL",        # Wall of force, etc
    15: "ITEM_CONTAINER",   # for containing other items
    16: "ITEM_NOTE",        # for passing information
    17: "ITEM_DRINKCON",    # for containing potables
    18: "ITEM_KEY",         # for unlocking locks
    19: "ITEM_FOOD",        # for eating
    20: "ITEM_MONEY",       # a pile of cash
    21: "ITEM_PEN",         # for scribbling NOTEs
    22: "ITEM_BOAT",        # row, row, row me boat, gently down the stream
    23: "ITEM_BOOK",        # well, maybe someday will be useful
    24: "ITEM_CORPSE",      # internal use only, do NOT assign this type!
    25: "ITEM_TELEPORT",    # item can be used to teleport
    26: "ITEM_TIMER",       # used chiefly to load/activate traps
    27: "ITEM_VEHICLE",     # Like ships, but can 'follow' mobs (carriage)
    28: "ITEM_SHIP",        # item which represents a sea-going vessel
    29: "ITEM_SWITCH",      # item is a trigger for a switch proc
    30: "ITEM_QUIVER",      # container for MISSILEs only
    31: "ITEM_PICK",        # lockpicks
    32: "ITEM_INSTRUMENT",  # bard's instruments
    33: "ITEM_SPELLBOOK",   # Genuine magetype spellbook
    34: "ITEM_TOTEM",       # shaman totem
    35: "ITEM_STORAGE",     # like a container, but saves itself
    36: "ITEM_SCABBARD",    # weapon scabbard
    37: "ITEM_SHIELD",      # dedicated type for shields
    38: "ITEM_BANDAGE",
    39: "ITEM_SPAWNER",
    40: "ITEM_HERB",
    41: "ITEM_PIPE",        # ITEM_LAST = 41
}

#Material Type Flags
material_type_lookup = {
    0: "MAT_UNDEFINED",
    1: "MAT_NONSUBSTANTIAL",
    2: "MAT_FLESH",
    3: "MAT_CLOTH",
    4: "MAT_BARK",
    5: "MAT_SOFTWOOD",
    6: "MAT_HARDWOOD",
    7: "MAT_SILICON",
    8: "MAT_CRYSTAL",
    9: "MAT_CERAMIC",
    10: "MAT_BONE",
    11: "MAT_STONE",
    12: "MAT_HIDE",
    13: "MAT_LEATHER",
    14: "MAT_CURED_LEATHER",
    15: "MAT_IRON",
    16: "MAT_STEEL",
    17: "MAT_BRASS",
    18: "MAT_MITHRIL",
    19: "MAT_ADAMANTIUM",
    20: "MAT_BRONZE",
    21: "MAT_COPPER",
    22: "MAT_SILVER",
    23: "MAT_ELECTRUM",
    24: "MAT_GOLD",
    25: "MAT_PLATINUM",
    26: "MAT_GEM",
    27: "MAT_DIAMOND",
    28: "MAT_PAPER",
    29: "MAT_PARCHMENT",
    30: "MAT_LEAVES",
    31: "MAT_RUBY",
    32: "MAT_EMERALD",
    33: "MAT_SAPPHIRE",
    34: "MAT_IVORY",
    35: "MAT_DRAGONSCALE",
    36: "MAT_OBSIDIAN",
    37: "MAT_GRANITE",
    38: "MAT_MARBLE",
    39: "MAT_LIMESTONE",
    40: "MAT_LIQUID",
    41: "MAT_BAMBOO",
    42: "MAT_REEDS",
    43: "MAT_HEMP",
    44: "MAT_GLASSTEEL",
    45: "MAT_EGGSHELL",
    46: "MAT_CHITINOUS",
    47: "MAT_REPTILESCALE",
    48: "MAT_GENERICFOOD",
    49: "MAT_RUBBER",
    50: "MAT_FEATHER",
    51: "MAT_WAX",
    52: "MAT_PEARL",
    53: "MAT_TIN",
}

# Reverse lookup: name → value
MAT_BY_NAME = {v: k for k, v in material_type_lookup.items()}

#Craftmanship Flags
craftmanship_lookup ={
	0: "TERRIBLY MADE",
	1: "EXTREMELY POOR",
	2: "VERY POOR",
	3: "FAIRLY POOR",
	4: "WELL BELOW AVERAGE",
	5: "BELOW AVERAGE",
	6: "SLIGHTLY BELOW AVERAGE",
	7: "AVERAGE",
	8: "SLIGHTLY ABOVE AVERAGE",
	9: "ABOVE AVERAGE",
	10: "WELL ABOVE AVERAGE",
	11: "EXCELLENT",
	12: "SKILLED ARTISAN",
	13: "VERY SKILLED ARTISAN",
	14: "MASTER ARTISAN",
	15: "ONE OF A KIND",
}

# Reverse lookup: name
CRAFTMANSHIP_BY_NAME = {v: k for k, v in craftmanship_lookup.items()}

#Weapon Type Flags
weapon_type_lookup = {
    0: "WEAPON_NONE",
    1: "WEAPON_AXE",
    2: "WEAPON_DAGGER",
    3: "WEAPON_FLAIL",
    4: "WEAPON_HAMMER",
    5: "WEAPON_LONGSWORD",
    6: "WEAPON_MACE",
    7: "WEAPON_SPIKED_MACE",
    8: "WEAPON_POLEARM",
    9: "WEAPON_SHORTSWORD",
    10: "WEAPON_CLUB",
    11: "WEAPON_SPIKED_CLUB",
    12: "WEAPON_STAFF",
    13: "WEAPON_2HANDSWORD",
    14: "WEAPON_WHIP",
    15: "WEAPON_SPEAR",
    16: "WEAPON_LANCE",
    17: "WEAPON_SICKLE",
    18: "WEAPON_TRIDENT",
    19: "WEAPON_HORN",
    20: "WEAPON_NUMCHUCKS"
}

herb_type_lookup = {
    1900: "HERB_SMOKED",
    1901: "HERB_OCULARIUS",
    1902: "HERB_BLUE_HAZE",
    1903: "HERB_MEDICUS",
    1904: "HERB_BLACK_KUSH",
    1905: "HERB_GOOTWIET"
}

shield_type_lookup = {
    1: "SHIELDTYPE_STRAPARM",
    2: "SHIELDTYPE_HANDHELD"
}

shield_shape_lookup = {
    1: "SHIELDSHAPE_CIRCULAR",  #// perfect circle
    2: "SHIELDSHAPE_SQUARE",    #// square..
    3: "SHIELDSHAPE_RECTVERT",  #// a rectangle aligned vertically
    4: "SHIELDSHAPE_RECTHORZ",  #// horizontally
    5: "SHIELDSHAPE_OVALVERT",  #// vertical 'oval'
    6: "SHIELDSHAPE_OVALHORZ",  #// horizontal 'oval'
    7: "SHIELDSHAPE_TRIBIGUP",  #// triangle - wide side on top
    8: "SHIELDSHAPE_TRISMLUP"   #// triangle - narrow point on top
}

shield_size_lookup = {
    1: "SHIELDSIZE_TINY",        #// really small suckers
    2: "SHIELDSIZE_SMALL",       #// bucklers, small shields
    3: "SHIELDSIZE_MEDIUM",      #// normal shields
    4: "SHIELDSIZE_LARGE",       #// big shields
    5: "SHIELDSIZE_HUGE"         #// huge shields (might not need this)
}

missile_type_lookup ={
    1: "MISSILE_ARROW",
    2: "MISSILE_LIGHT_CBOW_QUARREL",
    3: "MISSILE_HEAVY_CBOW_QUARREL",
    4: "MISSILE_HAND_CBOW_QUARREL",
    5: "MISSILE_SLING_BULLET",
    6: "MISSILE_DART"
}

#Item Size Flags
item_size_lookup = {	    
    0: "NONE",
    1: "TINY",
    2: "SMALL",
    3: "MEDIUM",
    4: "LARGE",
    5: "HUGE",
    6: "GIANT",
    7: "GARGANTUAN",
    8: "SMALL-MEDIUM",
    9: "MEDIUM-LARGE",
    10: "MAGICAL"
}

# Reverse lookup: name
SIZE_BY_NAME = {v: k for k, v in item_size_lookup.items()}
WEAPON_TYPE_BY_NAME = {v: k for k, v in weapon_type_lookup.items()}

# Modifier Flags
modifiers_lookup = {
	1:"APPLY_STR",
	2:"APPLY_DEX",
	3:"APPLY_INT",             
	4:"APPLY_WIS",               
	5:"APPLY_CON",               
	6:"APPLY_SEX",               
	7:"APPLY_CLASS",           
	8:"APPLY_LEVEL",            
	9:"APPLY_AGE",             
	10:"APPLY_CHAR_WEIGHT",     
	11:"APPLY_CHAR_HEIGHT",      
	12:"APPLY_MANA",             
	13:"APPLY_HIT",             
	14:"APPLY_MOVE",            
	15:"APPLY_GOLD",             
	16:"APPLY_EXP",              
	17:"APPLY_ARMOR",           
	18:"APPLY_HITROLL",
	19:"APPLY_DAMROLL",
	20:"APPLY_SAVING_PARA",
	21:"APPLY_SAVING_ROD",
	22:"APPLY_SAVING_FEAR",     
	23:"APPLY_SAVING_BREATH",    
	24:"APPLY_SAVING_SPELL",    
	25:"APPLY_FIRE_PROT",        
	26:"APPLY_AGI",              
	27:"APPLY_POW",       
	28:"APPLY_CHA",              
	29:"APPLY_KARMA",           
	30:"APPLY_LUCK",             
	31:"APPLY_STR_MAX",          
	32:"APPLY_DEX_MAX",          
	33:"APPLY_INT_MAX",          
	34:"APPLY_WIS_MAX",          
	35:"APPLY_CON_MAX",          
	36:"APPLY_AGI_MAX",          
	37:"APPLY_POW_MAX",          
	38:"APPLY_CHA_MAX",          
	39:"APPLY_KARMA_MAX",        
	40:"APPLY_LUCK_MAX",         
	41:"APPLY_STR_RACE",         
	42:"APPLY_DEX_RACE",         
	43:"APPLY_INT_RACE",         
	44:"APPLY_WIS_RACE",         
	45:"APPLY_CON_RACE",         
	46:"APPLY_AGI_RACE",         
	47:"APPLY_POW_RACE",         
	48:"APPLY_CHA_RACE",         
	49:"APPLY_KARMA_RACE",       
	50:"APPLY_LUCK_RACE",        
	51:"APPLY_CURSE",            
	52:"APPLY_SKILL_GRANT",
	53:"APPLY_SKILL_ADD",        
	54:"APPLY_HIT_REG",          
	55:"APPLY_MOVE_REG",         
	56:"APPLY_MANA_REG",         
	57:"APPLY_SPELL_PULSE",      
	58:"APPLY_COMBAT_PULSE"
}

# Reverse lookup: name → value
SIZE_BY_NAME = {v: k for k, v in modifiers_lookup.items()}

weapon_type_lookup = {
	0: "WEAPON_NONE",
	1: "WEAPON_AXE",
	2: "WEAPON_DAGGER",
	3: "WEAPON_FLAIL",
	4: "WEAPON_HAMMER",
	5: "WEAPON_LONGSWORD",
	6: "WEAPON_MACE",
	7: "WEAPON_SPIKED_MACE",
	8: "WEAPON_POLEARM",
	9: "WEAPON_SHORTSWORD",
	10: "WEAPON_CLUB",
	11: "WEAPON_SPIKED_CLUB",
	12: "WEAPON_STAFF",
	13: "WEAPON_2HANDSWORD",
	14: "WEAPON_WHIP",
	15: "WEAPON_SPEAR",
	16: "WEAPON_LANCE",
	17: "WEAPON_SICKLE",
	18: "WEAPON_TRIDENT",
	19: "WEAPON_HORN",
	20: "WEAPON_NUMCHUCKS",
}