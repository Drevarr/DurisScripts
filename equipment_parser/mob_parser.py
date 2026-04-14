from typing import Mapping
from bitvectors import *
from flags import *
from spells_skills import *

def parse_mob_file(filename):
    mobs = {}
    current = None
    stage = None
    desc_lines = []

    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for raw in f:
            line = raw.rstrip('\n')

            # New mob
            if line.startswith('#'):
                try:
                    vnum = int(line[1:])
                except ValueError:
                    continue

                current = {
                    'vnum': vnum,
                    'keywords': None,
                    'short_desc': None,
                    'long_desc': None,
                    'description': None,
                    'action_flags': None,
                    'agg_flags': None,
                    'agg2flags': None,
                    'agg3flags': None,
                    'affect1_flags': None,
                    'affect2_flags': None,
                    'affect3_flags': None,
                    'affect4_flags': None,
                    #'affect5_flags': None,                    
                    'alignment': None,
                    'species': None,
                    'hometown': None,
                    'class': None,
                    'spec': None,
                    'size': None,
                    'level': None,
                    'thac0': None,
                    'ac': None,
                    'hitroll': None,
                    'damage': None,
                    'exp': None,
                    'position': None,
                    'default_position': None,
                    'sex': None,
                }

                mobs[vnum] = current
                stage = 'keywords'
                desc_lines = []
                long_lines = []
                continue

            if current is None:
                continue

            if stage == 'keywords':
                if line.endswith('~'):
                    current['keywords'] = line[:-1]
                    stage = 'short'
                continue

            if stage == 'short':
                if line.endswith('~'):
                    current['short_desc'] = line[:-1]
                    stage = 'long'
                continue

            if stage == 'long':
                if line.endswith('~'):
                    long_lines.append(line[:-1])
                    current['long_desc'] = '\n'.join(long_lines).rstrip()
                    long_lines = []
                    stage = 'desc'
                elif line == '~':
                    current['long_desc'] = '\n'.join(long_lines).rstrip()
                    long_lines = []
                    stage = 'desc'
                else:
                    long_lines.append(line)
                continue

            if stage == 'desc':
                if line == '~':
                    current['description'] = '\n'.join(desc_lines).rstrip() or None
                    stage = 'stats1'
                else:
                    desc_lines.append(line)
                continue

            if stage == 'stats1':
                parts = line.split()
                # Example: 178250 0 0 0 33554468 12480 0 0 -100 S
                # action, agg, agg2, aff1, aff2, aff3, aff4 flags, align
                current['action_flags'] = decode_flags(int(parts[0]), MOB_ACTION_FLAGS) or "None"
                current['agg_flags'] = decode_flags(int(parts[1]), MOB_AGGRO_FLAGS) or "None"
                current['agg2_flags'] = decode_flags(int(parts[2]), MOB_AGGRO2_FLAGS) or "None"
                current['agg3_flags'] = decode_flags(int(parts[3]), MOB_AGGRO3_FLAGS) or "None"
                current['affect1_flags'] = decode_flags(int(parts[4]), ITEM_AFF1_FLAGS) or "None"
                current['affect2_flags'] = decode_flags(int(parts[5]), ITEM_AFF2_FLAGS) or "None"
                current['affect3_flags'] = decode_flags(int(parts[6]), ITEM_AFF3_FLAGS) or "None"
                current['affect4_flags'] = decode_flags(int(parts[7]), ITEM_AFF4_FLAGS) or "None"
                #current['affect5_flags'] = decode_flags(int(parts[8]), ITEM_AFF5_FLAGS)      
                current['alignment'] = int(parts[8])
                stage = 'stats2'
                continue

            if stage == 'stats2':
                # PG 8 1024 1 2
                parts = line.split()
                current['species'] = parts[0]
                current['hometown'] = int(parts[1])
                current['class'] = int(parts[2])
                current['spec'] = int(parts[3])
                current['size'] = int(parts[4])
                stage = 'stats3'
                continue

            if stage == 'stats3':
                # 51 0 0 1d1+1 1d1+1
                parts = line.split()
                current['level'] = int(parts[0])
                current['thac0'] = int(parts[1])
                current['ac'] = int(parts[2])
                current['hitroll'] = parts[3]
                current['damage'] = parts[4]
                stage = 'stats4'
                continue

            if stage == 'stats4':
                # 0.0.0.0 0
                parts = line.split()
                current['exp'] = int(parts[1])
                stage = 'stats5'
                continue

            if stage == 'stats5':
                # 8 8 0
                parts = line.split()
                current['position'] = int(parts[0])
                current['default_position'] = int(parts[1])
                current['sex'] = int(parts[2])
                stage = None
                continue

    return mobs