def parse_zon_file(filename):
    """
    Parses a .zon file and returns a dict with zone metadata.
    Only the first 3 non-comment lines are used.
    """
    meaningful = []

    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith('*'):
                continue

            meaningful.append(line)

            if len(meaningful) == 3:
                break

    if len(meaningful) < 3:
        raise ValueError("Invalid .zon file: not enough data lines")

    #  Line 1: zone vnum
    if not meaningful[0].startswith('#'):
        raise ValueError("Invalid zone vnum line")

    vnum = int(meaningful[0][1:])

    # Line 2: zone name
    name_line = meaningful[1]
    if not name_line.endswith('~'):
        raise ValueError("Zone name not terminated with ~")

    zone_name = name_line[:-1]

    # Line 3: zone stats
    parts = meaningful[2].split()
    if len(parts) != 6:
        raise ValueError("Invalid zone stat line")

    max_vnum   = int(parts[0])
    reset_mode = int(parts[1])
    zone_flags = int(parts[2])
    min_time   = int(parts[3])
    max_time   = int(parts[4])
    zone_diff  = int(parts[5])

    return {
        'vnum': vnum,
        'name': zone_name,
        'max_vnum': max_vnum,
        'min_time': min_time,
        'max_time': max_time,
        'reset_mode': reset_mode,
        'zone_flags': zone_flags,
        'zone_diff': zone_diff,
    }