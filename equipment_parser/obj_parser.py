from typing import Mapping
from bitvectors import *
from flags import *
from spells_skills import *

def read_tilde_block(lines):
    buf = []
    for line in lines:
        line = line.rstrip("\n")
        if line.endswith("~"):
            buf.append(line[:-1])
            break
        buf.append(line)
    return "\n".join(buf)


def read_ints_line(lines):
    return list(map(int, next(lines).split()))


def process_item_values(item_values, item_type):
    Item_Type_Notes={}
    
    match item_type:
        case "ITEM_WAND" | "ITEM_STAFF":
            spell_level = item_values[0] 
            max_charges = item_values[1]
            charges_left = item_values[2]
            spell_1 = spell_lookup[item_values[3]]
            Item_Type_Notes = {
            "Spell": spell_1,
            "Level": spell_level,
            "Max Charges": max_charges,
            "Reamining Charges": charges_left
            }
            
        case "ITEM_SCROLL" | "ITEM_POTION":
            spell_level = item_values[0] 
            spell_1 = spell_lookup[item_values[1]]
            spell_2 = spell_lookup[item_values[2]] or ""
            spell_3 = spell_lookup[item_values[3]] or ""
            Item_Type_Notes = {
            "Spell Level": {spell_level},
            "Spells": f"{spell_1} {spell_2} {spell_3}"
            }

        case "ITEM_WEAPON":
            weapon_type = weapon_type_lookup[item_values[0]]
            num_dice = item_values[1]
            size_dice = item_values[2]
            proc = item_values[5]
            proc_level = item_values[6]
            proc_pct = f"1/{item_values[7]}" if item_values[7] else 0
            Item_Type_Notes = {
                "Type": weapon_type,
                "Damage": f"{num_dice}D{size_dice}",
                "Proc": proc,
                "Proc Level": proc_level,
                "Proc Chance": proc_pct
            }

        case "ITEM_MISSILE":
            to_hit_mod = item_values[0]
            num_dice = item_values[1]            
            size_dice = item_values[2]
            missile_type = missile_type_lookup[item_values[3]]
            Item_Type_Notes = {
            "Missile Type": missile_type,
            "To Hit Mod": f"+{to_hit_mod}",
            "Damage": f"{num_dice}D{size_dice}"            
            }

        case "ITEM_ARMOR":
            armor_class = item_values[0]
            warmth = item_values[1]
            prestige = item_values[2]
            matl_type = material_type_lookup[item_values[3]]
            Item_Type_Notes = {
            "Armor Class": armor_class,
            "Prestige": prestige,
            "Warmth": warmth,
            "Material Type": matl_type
            }

        case "ITEM_WORN":
            matl_type = material_type_lookup[item_values[3]]
            Item_Type_Notes = {
            "Material Type": matl_type
            }
            
        case "ITEM_SHIELD":
            shield_type = shield_type_lookup[item_values[0]]
            shield_shape = shield_shape_lookup[item_values[1]]
            shield_size = shield_size_lookup[item_values[2]]
            armor_class = item_values[3]
            shield_thick = item_values[4]
            misc_flag = "Spiked" if item_values[5] else "None"
            Item_Type_Notes = {
            "Armor Class": armor_class,
            "Misc Flag": misc_flag,
            "Shield Type": shield_type,
            "Shield Shape": shield_shape,
            "Shield Size": shield_size,
            "Shield Thickness": shield_thick
            }
            
        case "ITEM_CONTAINER" | "ITEM_STORAGE":
            holds = item_values[0]
            locktype = item_values[1] 
            key = item_values[2]
            size_hold = item_values[3]
            Item_Type_Notes = {
            "Max Hold Weight": holds,
            "Hold Size": size_hold,
            "Lock Type": locktype,
            "Key Vnum": key
            }

        case "ITEM_KEY":
            break_pct = item_values[1]
            Item_Type_Notes = {
            "Break Pct": break_pct
            }
            
        case "ITEM_FOOD":
            time = item_values[0]
            hit_reg = item_values[1]*15 or 15
            move_reg = item_values[2]
            poi = "YES" if item_values[3] else "NO"
            str_con = item_values[4]
            agi_dex = item_values[5]
            int_wis = item_values[6]
            hit_dam = item_values[7]
            Item_Type_Notes = {
            "Duration": time,
            "Hit Regen": hit_reg,
            "Move Regen": move_reg,
            "Str/Con": str_con,
            "Agi/Dex": agi_dex,
            "Int/Wis": int_wis,
            "Hit/Dam": hit_dam,
            "Poison": poi
            }
            
        case "ITEM_MONEY":
            copper = item_values[0]
            silver = item_values[1]
            gold = item_values[2]
            platinum = item_values[3]
            Item_Type_Notes = {
            "Copper": copper,
            "Silver": silver,
            "Gold": gold,
            "Platinum": platinum
            }
            
        case "ITEM_TELEPORT":
            to_room = item_values[0]
            command = item_values[1]
            charges = item_values[2]
            if charges == -1:
                charges = "Infinite"
            zone_to = item_values[3]
            Item_Type_Notes = {
                "To Room": to_room,
                "Command": command,
                "Charges": charges,
                "To Zone": zone_to
            }

        case "ITEM_PICK":
            pick_bonus = item_values[0]
            break_pct = item_values[1]
            Item_Type_Notes = {
                "Pick Bonus": pick_bonus,
                "Break Pct": break_pct
            }

        case "ITEM_INSTRUMENT":
            type = item_values[0]
            level = item_values[1]
            break_pct = item_values[2]
            min_level = item_values[4]
            Item_Type_Notes = {
                "Type": type,
                "Level": level,
                "Break Chance": break_pct,
                "Min Level": min_level
            }

        case "ITEM_SPELLBOOK":
            prof = item_values[0]
            tongue = item_values[1]
            total_pages = item_values[2]
            used_pages = item_values[3]
            Item_Type_Notes = {
                "Class": prof,
                "Tongue": tongue,
                "Total Pages": total_pages,
                "Used Pages": used_pages,
            }

        case "ITEM_SWITCH":
            cmd = item_values[0]
            room = item_values[1]
            direction = item_values[2]
            switch_move = "SWITCH" if item_values[3] else "WALL"
            Item_Type_Notes = {
                "Command": cmd,
                "Room": room,
                "Direction": direction,
                "What Move": switch_move
            }

        case "ITEM_QUIVER":
            max_hold = item_values[0]
            flags = item_values[1]
            missile_type = item_values[2]
            cur_hold = item_values[3]
            Item_Type_Notes = {
                "Max Hold": max_hold,
                "Current Held": cur_hold,
                "Flags": flags,
                "Missile Type": missile_type
            }
                
        case "ITEM_TOTEM":
            spheres = ', '.join(decode_flags(item_values[0], TOTEM_SPHERE_FLAGS))
            Item_Type_Notes = {
                "Spheres": spheres
            }
    
        case "ITEM_BANDAGE":
            maxheal = item_values[0]
            Item_Type_Notes = {
                "Max Heal": maxheal
            }
    
        case "ITEM_HERB":
            level = item_values[0]
            herb_1 = herb_type_lookup[item_values[1]]
            herb_2 = herb_type_lookup[item_values[2]]
            herb_3 = herb_type_lookup[item_values[3]]
            duration = item_values[7]
            if herb_2:
                spell_2_level = level/2
            if herb_3:
                spell_3_level = level/3
            stoned_duration = item_values[6]
            Item_Type_Notes = {
                "Level": level,
                "Duration": duration,
                "Spell_1": herb_1,
                "Spell_1 Level:": level,
                "Spell_2": herb_2,
                "Spell_2 Level": spell_2_level,
                "Spell_3": herb_3,
                "Spell_3 Duration": spell_3_level,
                "Stoned Duration": stoned_duration
            }
                

        case "ITEM_PIPE":
            type = item_values[0]
            pipe_hp = item_values[1]
            break_pct = item_values[2]     #if( number(1, 100) < pipe->value[2] )
            item_value_note = {
                "Type": type,
                "Pipe HP": pipe_hp,
                "Break Pct": break_pct
            }
            
        case _:
            print("No specific item value notes, let Drevarr know if you think something is wrong.")  # Default case

    return Item_Type_Notes


def parse_obj_file(path):
    objects = {}

    pending_line = None

    with open(path, "r", encoding="utf-8") as f:
        lines = iter(f)

        while True:
            if pending_line is not None:
                raw = pending_line
                pending_line = None
            else:
                raw = next(lines, None)

            if raw is None:
                break

            line = raw.strip()

            if not line.startswith("#"):
                continue

            if line.startswith("$"):
                break

            # object header
            vnum = int(line[1:])

            namelist   = read_tilde_block(lines)
            short_desc = read_tilde_block(lines)
            long_desc  = read_tilde_block(lines)
            _ = read_tilde_block(lines)  # full desc / unused

            # stats line 1
            stats1 = read_ints_line(lines)

            defaults = [0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0]
            stats1 = (stats1 + defaults)[:11]

            (
                item_type, matl_type, size, space,
                craftsmanship, dmg_resist,
                extra1_flags, wear_flags,
                extra2_flags, anti1_flags, anti2_flags
            ) = stats1

            # stats line 2
            stats2 = read_ints_line(lines)
            stats2 = (stats2 + [0] * 8)[:8]
            item_vals = stats2
            item_vals_notes = process_item_values(item_vals, item_type)

            # stats line 3
            stats3 = read_ints_line(lines)
            stats3 = (stats3 + [0] * 8)[:8]

            weight, worth, condition, aff1, aff2, aff3, aff4, aff5 = stats3

            # optional E / A sections
            extra_desc = []
            affects = []

            while True:
                #peek = next(lines).strip()
                try:
                    peek = next(lines).strip()
                except StopIteration:
                    break                

                if peek == "E":
                    keyword = read_tilde_block(lines)
                    if "_id_name_" in keyword:
                        continue
                    desc = read_tilde_block(lines)
                    extra_desc.append((keyword, desc))

                elif peek == "A":
                    loc, mod = read_ints_line(lines)
                    loc = modifiers_lookup[loc]
                    affects.append((loc, mod))

                else:
                    # push back one line for the outer loop
                    pending_line = peek + "\n"
                    break

            # ---- store object ----
            objects[vnum] = {
                "vnum": vnum,
                "name_list": namelist,
                "short_description": short_desc,
                "long_description": long_desc,
                "item_type": item_type_lookup[item_type],
                "material": material_type_lookup[matl_type],
                "size": item_size_lookup[size],
                "space": space,
                "craftsmanship": craftmanship_lookup[craftsmanship],
                "damage_resist": dmg_resist,
                "wear_flags": decode_flags(wear_flags, ITEM_WEAR_FLAGS),
                "extra1_flags": decode_flags(extra1_flags, ITEM_EXTRA1_FLAGS),
                "extra2_flags": decode_flags(extra2_flags, ITEM_EXTRA2_FLAGS),
                "anti1_flags": decode_flags(anti1_flags, ITEM_CLASS_ANTI_FLAGS),
                "anti2_flags": decode_flags(anti2_flags, ITEM_ANTI2_FLAGS),
                "item_values": item_vals,
                "item_value_notes": item_vals_notes,
                "weight": weight,
                "worth": worth,
                "condition": condition,
                "aff1": decode_flags(aff1, ITEM_AFF1_FLAGS),
                "aff2": decode_flags(aff2, ITEM_AFF2_FLAGS),
                "aff3": decode_flags(aff3, ITEM_AFF3_FLAGS),
                "aff4": decode_flags(aff4, ITEM_AFF4_FLAGS),
                "aff5": decode_flags(aff5, ITEM_AFF5_FLAGS),
                "affects": affects,
                "extra_descriptions": extra_desc,
            }

    return objects