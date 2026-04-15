import sqlite3
from typing import Dict, List, Tuple, Any

def create_object_database(db_path: str = "mud_objects.db") -> sqlite3.Connection:
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

    # Fixed 8 values (weapon: damage dice, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS object_values (
            vnum INTEGER PRIMARY KEY,
            val0 INTEGER, val1 INTEGER, val2 INTEGER, val3 INTEGER,
            val4 INTEGER, val5 INTEGER, val6 INTEGER, val7 INTEGER,
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

    # --- Main object record ---
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

    # --- Helper to insert flag lists ---
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

    # --- Values (always 8 integers) ---
    values = obj.get('values', [])
    values_padded = (values + [0] * 8)[:8]
    cursor.execute("""
        INSERT OR REPLACE INTO object_values
        (vnum, val0, val1, val2, val3, val4, val5, val6, val7)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (vnum, *values_padded))

    # --- Location-based affects (e.g., APPLY_STR, +6) ---
    for location, modifier in obj.get('affects', []):
        cursor.execute("""
            INSERT OR REPLACE INTO object_affects (vnum, location, modifier)
            VALUES (?, ?, ?)
        """, (vnum, location, modifier))

    # --- Extra descriptions ---
    for keywords, description in obj.get('extra_descriptions', []):
        cursor.execute("""
            INSERT OR REPLACE INTO object_extra_descriptions
            (vnum, keywords, description) VALUES (?, ?, ?)
        """, (vnum, keywords, description))

    conn.commit()


def fetch_object_by_vnum(vnum: int, conn: sqlite3.Connection) -> Dict[str, Any] | None:
    """
    Retrieves a complete object dictionary by its vnum.
    Returns None if not found.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM objects WHERE vnum = ?", (vnum,))
    row = cursor.fetchone()
    if not row:
        return None

    # Column names from the objects table
    columns = [desc[0] for desc in cursor.description]
    obj = dict(zip(columns, row))

    # Fetch flags from a table
    def get_flags(table_name: str) -> List[str]:
        cursor.execute(f"SELECT flag FROM {table_name} WHERE vnum = ?", (vnum,))
        return [row[0] for row in cursor.fetchall()]

    # Fetch all flag lists
    obj['wear_flags'] = get_flags("object_wear_flags")
    obj['extra1_flags'] = get_flags("object_extra1_flags")
    obj['extra2_flags'] = get_flags("object_extra2_flags")
    obj['anti1_flags'] = get_flags("object_anti1_flags")
    obj['anti2_flags'] = get_flags("object_anti2_flags")
    obj['aff1'] = get_flags("object_aff1_flags")
    obj['aff2'] = get_flags("object_aff2_flags")
    obj['aff3'] = get_flags("object_aff3_flags")
    obj['aff4'] = get_flags("object_aff4_flags")

    # Fetch values
    cursor.execute("SELECT val0,val1,val2,val3,val4,val5,val6,val7 FROM object_values WHERE vnum = ?", (vnum,))
    values_row = cursor.fetchone()
    obj['values'] = list(values_row) if values_row else [0] * 8

    # Fetch affects (location-based)
    cursor.execute("SELECT location, modifier FROM object_affects WHERE vnum = ?", (vnum,))
    obj['affects'] = [(loc, mod) for loc, mod in cursor.fetchall()]

    # Fetch extra descriptions
    cursor.execute("SELECT keywords, description FROM object_extra_descriptions WHERE vnum = ?", (vnum,))
    obj['extra_descriptions'] = [(kw, desc) for kw, desc in cursor.fetchall()]

    return obj


def search_objects_by_name(keyword: str, conn: sqlite3.Connection, limit: int = 50) -> List[Dict[str, Any]]:
    """
    Searches objects where name_list contains the keyword (case-insensitive).
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT vnum FROM objects 
        WHERE name_list LIKE ? OR short_description LIKE ? OR long_description LIKE ?
        LIMIT ?
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", limit))

    results = []
    for (vnum,) in cursor.fetchall():
        obj = fetch_object_by_vnum(vnum, conn)
        if obj:
            results.append(obj)
    return results


def get_all_weapons(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """Returns all objects of type ITEM_WEAPON"""
    cursor = conn.cursor()
    cursor.execute("SELECT vnum FROM objects WHERE item_type = 'ITEM_WEAPON'")
    return [fetch_object_by_vnum(vnum, conn) for (vnum,) in cursor.fetchall() if fetch_object_by_vnum(vnum, conn)]


def get_objects_with_flag(flag: str, conn: sqlite3.Connection, flag_table: str = None) -> List[Dict[str, Any]]:
    """
    Generic search for objects that have a specific flag.
    If flag_table is None, searches across all common flag tables.
    """
    cursor = conn.cursor()
    tables_to_search = [
        "object_wear_flags",
        "object_extra1_flags",
        "object_extra2_flags",
        "object_anti1_flags",
        "object_anti2_flags",
        "object_aff1_flags",
        "object_aff2_flags",
        "object_aff3_flags",
        "object_aff4_flags"
    ]

    if flag_table:
        tables_to_search = [flag_table]

    vnums = set()
    for table in tables_to_search:
        cursor.execute(f"SELECT vnum FROM {table} WHERE flag = ?", (flag,))
        for (vnum,) in cursor.fetchall():
            vnums.add(vnum)

    return [obj for vnum in vnums if (obj := fetch_object_by_vnum(vnum, conn))]


def get_artifacts(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """Convenience: all items with ITEM_ARTIFACT flag"""
    return get_objects_with_flag("ITEM_ARTIFACT", conn, "object_extra1_flags")


def get_glowing_items(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """Items with GLOW flag"""
    return get_objects_with_flag("ITEM_GLOW", conn, "object_extra1_flags")


def get_items_allowed_only_for_class(class_name: str, conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """
    Finds items restricted to a specific class (via anti flags like not ASSASSIN, etc.)
    Note: This finds items that EXCLUDE other classes — common pattern in MUDs.
    """
    return get_objects_with_flag(class_name.upper(), conn, "object_anti1_flags")

