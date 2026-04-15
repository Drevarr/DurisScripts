from Python.equipment_parser.bitvectors import *

def itemvalue(obj):
    if obj is None:
        return 0

    workingvalue = 0.0
    multiplier = 1.0

    # Wear location multipliers
    if 'ITEM_WEAR_EYES' in obj['wear_flags']:
        multiplier *= 1.3
    if 'ITEM_WEAR_EARRING' in obj['wear_flags']:
        multiplier *= 1.2
    if 'ITEM_WEAR_FACE' in obj['wear_flags']:
        multiplier *= 1.3
    if 'ITEM_WEAR_QUIVER' in obj['wear_flags']:
        multiplier *= 1.1
    if 'ITEM_WEAR_FINGER' in obj['wear_flags']:
        multiplier *= 1.2
    if 'ITEM_GUILD_INSIGNIA' in obj['wear_flags']:
        multiplier *= 1.5
    if 'ITEM_WEAR_NECK' in obj['wear_flags']:
        multiplier *= 1.2
    if 'ITEM_WEAR_WAIST' in obj['wear_flags']:
        multiplier *= 1.1
    if 'ITEM_WEAR_WRIST' in obj['wear_flags']:
        multiplier *= 1.1

    # Affect flags (bitvector) additions
    if 'AFF_STONE_SKIN' in obj['aff1']:
        workingvalue += 125
    if 'AFF_BIOFEEDBACK' in obj['aff1']:
        workingvalue += 110
    if 'AFF_FARSEE' in obj['aff1']:
        workingvalue += 45
    if 'AFF_DETECT_INVISIBLE' in obj['aff1']:
        workingvalue += 90
    if 'AFF_HASTE' in obj['aff1']:
        workingvalue += 75
    if 'AFF_INVISIBLE' in obj['aff1']:
        workingvalue += 35
    if 'AFF_SENSE_LIFE' in obj['aff1']:
        workingvalue += 45
    if 'AFF_MINOR_GLOBE' in obj['aff1']:
        workingvalue += 28
    if 'AFF_UD_VISION' in obj['aff1']:
        workingvalue += 40
    if 'AFF_WATERBREATH' in obj['aff1']:
        workingvalue += 45
    if 'AFF_PROTECT_EVIL' in obj['aff1']:
        workingvalue += 35
    if 'AFF_PROTECT_GOOD' in obj['aff1']:
        workingvalue += 35
    if 'AFF_SLOW_POISON' in obj['aff1']:
        workingvalue += 20
    if 'AFF_SNEAK' in obj['aff1']:
        workingvalue += 125
    if 'AFF_BARKSKIN' in obj['aff1']:
        workingvalue += 25
    if 'AFF_INFRAVISION' in obj['aff1']:
        workingvalue += 7
    if 'AFF_LEVITATE' in obj['aff1']:
        workingvalue += 13
    if 'AFF_HIDE' in obj['aff1']:
        workingvalue += 85
    if 'AFF_FLY' in obj['aff1']:
        workingvalue += 75
    if 'AFF_AWARE' in obj['aff1']:
        workingvalue += 75
    if 'AFF_PROT_FIRE' in obj['aff1']:
        workingvalue += 20

    if 'AFF2_FIRESHIELD' in obj['aff2']:
        workingvalue += 45
    if 'AFF2_ULTRAVISION' in obj['aff2']:
        workingvalue += 80
    if 'AFF2_DETECT_EVIL' in obj['aff2']:
        workingvalue += 5
    if 'AFF2_DETECT_GOOD' in obj['aff2']:
        workingvalue += 5
    if 'AFF2_DETECT_MAGIC' in obj['aff2']:
        workingvalue += 10
    if 'AFF2_PROT_COLD' in obj['aff2']:
        workingvalue += 20
    if 'AFF2_PROT_LIGHTNING' in obj['aff2']:
        workingvalue += 30
    if 'AFF2_GLOBE' in obj['aff2']:
        workingvalue += 80
    if 'AFF2_PROT_GAS' in obj['aff2']:
        workingvalue += 30
    if 'AFF2_PROT_ACID' in obj['aff2']:
        workingvalue += 30
    if 'AFF2_SOULSHIELD' in obj['aff2']:
        workingvalue += 45
    if 'AFF2_MINOR_INVIS' in obj['aff2']:
        workingvalue += 15
    if 'AFF2_VAMPIRIC_TOUCH' in obj['aff2']:
        workingvalue += 65
    if 'AFF2_EARTH_AURA' in obj['aff2']:
        workingvalue += 110
    if 'AFF2_WATER_AURA' in obj['aff2']:
        workingvalue += 115
    if 'AFF2_FIRE_AURA' in obj['aff2']:
        workingvalue += 120
    if 'AFF2_AIR_AURA' in obj['aff2']:
        workingvalue += 130
    if 'AFF2_PASSDOOR' in obj['aff2']:
        workingvalue += 80
    if 'AFF2_FLURRY' in obj['aff2']:
        workingvalue += 150

    if 'AFF3_PROT_ANIMAL' in obj['aff3']:
        workingvalue += 20
    if 'AFF3_SPIRIT_WARD' in obj['aff3']:
        workingvalue += 35
    if 'AFF3_GR_SPIRIT_WARD' in obj['aff3']:
        workingvalue += 25
        multiplier += 1.20
    if 'AFF3_ENLARGE' in obj['aff3']:
        workingvalue += 120
    if 'AFF3_REDUCE' in obj['aff3']:
        workingvalue += 120
    if 'AFF3_INERTIAL_BARRIER' in obj['aff3']:
        workingvalue += 135
    if 'AFF3_COLDSHIELD' in obj['aff3']:
        workingvalue += 45
    if 'AFF3_TOWER_IRON_WILL' in obj['aff3']:
        workingvalue += 45
    if 'AFF3_BLUR' in obj['aff3']:
        workingvalue += 65
    if 'AFF3_PASS_WITHOUT_TRACE' in obj['aff3']:
        workingvalue += 45

    if 'AFF4_VAMPIRE_FORM' in obj['aff4']:
        workingvalue += 90
    if 'AFF4_HOLY_SACRIFICE' in obj['aff4']:
        workingvalue += 105
    if 'AFF4_BATTLE_ECSTASY' in obj['aff4']:
        workingvalue += 105
    if 'AFF4_DAZZLER' in obj['aff4']:
        workingvalue += 45
    if 'AFF4_PHANTASMAL_FORM' in obj['aff4']:
        workingvalue += 105
    if 'AFF4_NOFEAR' in obj['aff4']:
        workingvalue += 40
    if 'AFF4_REGENERATION' in obj['aff4']:
        workingvalue += 60
    if 'AFF4_GLOBE_OF_DARKNESS' in obj['aff4']:
        workingvalue += 15
    if 'AFF4_HAWKVISION' in obj['aff4']:
        workingvalue += 20
    if 'AFF4_SANCTUARY' in obj['aff4']:
        workingvalue += 105
    if 'AFF4_HELLFIRE' in obj['aff4']:
        workingvalue += 110
    if 'AFF4_SENSE_HOLINESS' in obj['aff4']:
        workingvalue += 15
    if 'AFF4_PROT_LIVING' in obj['aff4']:
        workingvalue += 45
    if 'AFF4_DETECT_ILLUSION' in obj['aff4']:
        workingvalue += 40
    if 'AFF4_ICE_AURA' in obj['aff4']:
        workingvalue += 90
    if 'AFF4_NEG_SHIELD' in obj['aff4']:
        workingvalue += 45
    if 'AFF4_WILDMAGIC' in obj['aff4']:
        workingvalue += 240

    # Old-school proc (up to three spells on wield)
    if ('ITEM_WIELD' in obj['wear_flags']) and obj['item_type']:
        #Load values to determine spells
        spell_val = obj["values"][4]
        spells = [
            spell_val % 1000,
            (spell_val % 1000000) // 1000,
            (spell_val % 1000000000) // 1000000
        ]

        mod = ((obj["values"][5] / 10.0) if obj["values"][5] > 19 else 1.0) * (30.0 / obj["values"][6])

        #Get spell circles - need a method to do this
        spellcirclesum = get_mincircle(spells[0]) + get_mincircle(spells[1]) + get_mincircle(spells[2])

        if obj["values"][4] // 1000000000:  # casts one random spell
            numspells = sum(1 for s in spells if s > 0)
            numspells = numspells if numspells > 0 else 1
            workingvalue += mod * (spellcirclesum / numspells)
        else:  # casts all spells
            workingvalue += mod * spellcirclesum

    # Real object proc - Need to review spec_object assigned
    #if obj_index[obj.R_num].func.obj:
        #workingvalue += get_ival_from_proc(obj_index[obj.R_num].func.obj)

    # Object affects (A0/A1/A2 etc.)
    for i in range(MAX_OBJ_AFFECT):
        affect = obj.affected[i]
        if affect.location == 0 and affect.modifier == 0:
            continue  # assume unused slots are zeroed

        mod = affect.modifier

        if affect.location in (APPLY_DAMROLL, APPLY_HITROLL):
            if obj.type == ITEM_WEAPON:
                workingvalue += mod if mod <= 2 else mod * (mod - 1)
            else:
                workingvalue += (3 * mod - 1) if mod <= 2 else 3 * mod * mod + 3
            multiplier *= 1.25

        elif affect.location in (APPLY_STR, APPLY_DEX, APPLY_INT, APPLY_WIS, APPLY_CON, APPLY_AGI):
            workingvalue += 2 * mod if mod <= 3 else (mod - 1) * (mod - 1)

        elif affect.location in (APPLY_POW, APPLY_CHA, APPLY_LUCK):
            workingvalue += 2 * mod if mod <= 6 else (mod - 2) * (mod - 2) - 10

        elif affect.location == APPLY_HIT:
            workingvalue += 2 * mod if mod <= 4 else (18 * mod) // 5 - 7

        elif affect.location in (APPLY_MOVE, APPLY_MANA):
            workingvalue += mod if mod <= 25 else 4 * mod - 75

        elif affect.location in (APPLY_HIT_REG, APPLY_MOVE_REG, APPLY_MANA_REG):
            workingvalue += mod if mod < 4 else (mod * mod) // 3

        elif affect.location in (
            APPLY_AGI_RACE, APPLY_STR_RACE, APPLY_CON_RACE, APPLY_INT_RACE,
            APPLY_WIS_RACE, APPLY_CHA_RACE, APPLY_DEX_RACE
        ):
            if not (1 <= mod <= LAST_RACE):
                print(f"itemvalue: obj '{obj.short_description}' {OBJ_VNUM(obj)} has bad racial modifier {mod}")
                workingvalue += 100
            else:
                stat = {
                    APPLY_AGI_RACE: stat_factor[int(mod)].Agi,
                    APPLY_STR_RACE: stat_factor[int(mod)].Str,
                    APPLY_CON_RACE: stat_factor[int(mod)].Con,
                    APPLY_INT_RACE: stat_factor[int(mod)].Int,
                    APPLY_WIS_RACE: stat_factor[int(mod)].Wis,
                    APPLY_CHA_RACE: stat_factor[int(mod)].Cha,
                    APPLY_DEX_RACE: stat_factor[int(mod)].Dex,
                }[affect.location]
                workingvalue += 2 * stat - 150

        elif affect.location == APPLY_AC and mod != 0:
            ac = abs(mod)
            workingvalue += (3 * ac) // 2
            multiplier += ac / 500.0

        elif affect.location in (
            APPLY_SAVING_PARA, APPLY_SAVING_ROD, APPLY_SAVING_FEAR,
            APPLY_SAVING_BREATH, APPLY_SAVING_SPELL
        ):
            workingvalue += mod * mod * (2 if mod <= 0 else -2)

        elif affect.location in (APPLY_COMBAT_PULSE, APPLY_SPELL_PULSE):
            multiplier *= 2
            workingvalue += mod * -75

        elif affect.location in (
            APPLY_STR_MAX, APPLY_DEX_MAX, APPLY_INT_MAX, APPLY_WIS_MAX,
            APPLY_CON_MAX, APPLY_CHA_MAX, APPLY_AGI_MAX, APPLY_POW_MAX, APPLY_LUCK_MAX
        ):
            import math
            workingvalue += 3.0 * mod if mod < 2 else 3.52 * mod * math.sqrt(mod) + mod
            multiplier += 0.15

    # Weapon-specific bonuses
    if obj.type == ITEM_WEAPON:
        workingvalue += obj.value[1] * obj.value[2]  # avg damage
        multiplier += obj.value[1] * obj.value[2] * 0.005

        if IS_BACKSTABBER(obj):
            mod = obj.value[2]
            workingvalue += ((obj.value[1] * obj.value[1] + 19.0) / 20.0) * (mod * mod * mod) / 5.0

    # Armor-specific AC
    if obj.type == ITEM_ARMOR:
        ac = abs(obj.value[0])
        workingvalue += (3 * ac) // 2
        multiplier += ac / 500.0

    # Two-handed penalty
    if obj.extra_flags & ITEM_TWOHANDS:
        multiplier *= 0.80

    # Final multiplication
    workingvalue *= multiplier

    if workingvalue < 1:
        workingvalue = 1

    # Special case: non-takeable utility items should be worth 1
    if not (obj.wear_flags & ITEM_TAKE) and obj.type == ITEM_TELEPORT or \
       obj.type in (ITEM_KEY, ITEM_SWITCH, ITEM_VEHICLE, ITEM_SHIP, ITEM_STORAGE):
        if workingvalue != 1:
            print(f"Always load obj '{OBJ_SHORT(obj)}' {OBJ_VNUM(obj)} has stats giving ival {workingvalue:.3f}.")
        return 1

    return int(workingvalue)