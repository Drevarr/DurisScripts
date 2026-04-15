import json
import sqlite3
from typing import Dict, List, Tuple, Any

def create_object_database(db_path: str = "mud_objects2.db") -> sqlite3.Connection:
    """
    Creates (or connects to) the SQLite database with full schema for your MUD objects.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Main object table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS objects (
            vnum INTEGER PRIMARY KEY,
            name_list TEXT NOT NULL,
            short_description TEXT,
            long_description TEXT,
            item_type TEXT,
            material TEXT,
            size TEXT,
            space INTEGER,
            craftsmanship TEXT,
            damage_resist INTEGER,
            weight INTEGER,
            worth INTEGER,
            condition INTEGER
        )
    """)

    # Many-to-many tables for flags
    for table_name in [
        "object_wear_flags",
        "object_extra1_flags",
        "object_extra2_flags",
        "object_anti1_flags",
        "object_anti2_flags",
        "object_aff1_flags",
        "object_aff2_flags",
        "object_aff3_flags",
        "object_aff4_flags"
    ]:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                vnum INTEGER,
                flag TEXT,
                PRIMARY KEY (vnum, flag),
                FOREIGN KEY (vnum) REFERENCES objects(vnum) ON DELETE CASCADE
            )
        """)

    # Fixed 8 values (weapon: damage dice, etc.) + notes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS object_values (
            vnum INTEGER PRIMARY KEY,
            val0 INTEGER, val1 INTEGER, val2 INTEGER, val3 INTEGER,
            val4 INTEGER, val5 INTEGER, val6 INTEGER, val7 INTEGER,
            item_notes JSON,
            FOREIGN KEY (vnum) REFERENCES objects(vnum) ON DELETE CASCADE
        )
    """)

    # Location-based affects (modifier, value) - e.g., +6 STR, +6 CON
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS object_affects (
            vnum INTEGER,
            location INTEGER,
            modifier INTEGER,
            PRIMARY KEY (vnum, location),
            FOREIGN KEY (vnum) REFERENCES objects(vnum) ON DELETE CASCADE
        )
    """)

    # Extra descriptions (keyword list -> description)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS object_extra_descriptions (
            vnum INTEGER,
            keywords TEXT,
            description TEXT,
            PRIMARY KEY (vnum, keywords),
            FOREIGN KEY (vnum) REFERENCES objects(vnum) ON DELETE CASCADE
        )
    """)

    conn.commit()
    return conn


def insert_object_into_db(obj: Dict[str, Any], conn: sqlite3.Connection):
    """
    Inserts or updates a full object dictionary into the SQLite database.
    Handles all fields from your latest example.
    """
    cursor = conn.cursor()
    vnum = obj['vnum']

    # Main object record 
    cursor.execute("""
        INSERT OR REPLACE INTO objects (
            vnum, name_list, short_description, long_description,
            item_type, material, size, space, craftsmanship,
            damage_resist, weight, worth, condition
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        vnum,
        obj['name_list'],
        obj['short_description'],
        obj['long_description'],
        obj['item_type'],
        obj['material'],
        obj['size'],
        obj.get('space'),
        obj.get('craftsmanship'),
        obj.get('damage_resist', 0),
        obj['weight'],
        obj['worth'],
        obj['condition']
    ))

    def insert_flags(table: str, flags: List[str]):
        if not flags:
            return
        for flag in flags:
            cursor.execute(f"INSERT OR IGNORE INTO {table} (vnum, flag) VALUES (?, ?)", (vnum, flag))

    # Wear and extra flags
    insert_flags("object_wear_flags", obj.get('wear_flags', []))
    insert_flags("object_extra1_flags", obj.get('extra1_flags', []))
    insert_flags("object_extra2_flags", obj.get('extra2_flags', []))

    # Anti flags (can contain 'ALL' or class/race names)
    insert_flags("object_anti1_flags", obj.get('anti1_flags', []))
    insert_flags("object_anti2_flags", obj.get('anti2_flags', []))

    # Permanent affects (AFF_ flags)
    insert_flags("object_aff1_flags", obj.get('aff1', []))
    insert_flags("object_aff2_flags", obj.get('aff2', []))
    insert_flags("object_aff3_flags", obj.get('aff3', []))
    insert_flags("object_aff4_flags", obj.get('aff4', []))

    # Added item_notes based on item type
    values = obj.get('values', [])
    values_padded = (values + [0] * 8)[:8]
    cursor.execute("""
        INSERT OR REPLACE INTO object_values
        (vnum, val0, val1, val2, val3, val4, val5, val6, val7, item_notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (vnum, *values_padded, json.dumps(obj['item_notes'])))

    # Location-based affects (e.g., APPLY_STR, +6) 
    for location, modifier in obj.get('affects', []):
        cursor.execute("""
            INSERT OR REPLACE INTO object_affects (vnum, location, modifier)
            VALUES (?, ?, ?)
        """, (vnum, location, modifier))

    # Extra descriptions 
    for keywords, description in obj.get('extra_descriptions', []):
        cursor.execute("""
            INSERT OR REPLACE INTO object_extra_descriptions
            (vnum, keywords, description) VALUES (?, ?, ?)
        """, (vnum, keywords, description))

    conn.commit()
