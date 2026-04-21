import re
from PIL import Image

def get_sectors(filename):
    print("Reading rooms...")
    state = 0
    dir_state = 0
    vnum = 0
    sectors = {}
    starting_vnum = None

    with open(filename, "r") as infile:
        for line in infile:
            line = line.rstrip("\n")

            if state == 0:
                m = re.match(r'^#(\d+)\s*$', line)
                if m:
                    vnum = int(m.group(1))
                    if starting_vnum is None:
                        starting_vnum = vnum
                    state = 1

            elif state == 1:
                state = 2

            elif state == 2:
                if re.match(r'^~\s*$', line):
                    state = 3

            elif state == 3:
                m = re.match(r'^(\d+) (\d+) (\d+) (\d+)\s*$', line)
                if m:
                    sector = int(m.group(3))
                    sectors[vnum] = sector
                    state = 4

            elif state == 4:
                if re.match(r'^S\s*$', line):
                    state = 0
                else:
                    dir_state = (dir_state + 1) % 4

    print(f"{len(sectors)} rooms loaded")
    return sectors, starting_vnum


# Convert vnum to pixel location on png map
def vnum_to_pixel(vnum, start, width, square):
    offset = vnum - start
    y = offset // width
    x = offset % width
    return x * square, y * square


# Sector Constants
SECT_INSIDE = 0
SECT_CITY = 1
SECT_FIELD = 2
SECT_FOREST = 3
SECT_HILLS = 4
SECT_MOUNTAIN = 5
SECT_WATER_SWIM = 6
SECT_WATER_NOSWIM = 7
SECT_NO_GROUND = 8
SECT_UNDERWATER = 9
SECT_UNDERWATER_GR = 10
SECT_FIREPLANE = 11
SECT_OCEAN = 12
SECT_UNDRWLD_WILD = 13
SECT_UNDRWLD_CITY = 14
SECT_UNDRWLD_INSIDE = 15
SECT_UNDRWLD_WATER = 16
SECT_UNDRWLD_NOSWIM = 17
SECT_UNDRWLD_NOGROUND = 18
SECT_AIR_PLANE = 19
SECT_WATER_PLANE = 20
SECT_EARTH_PLANE = 21
SECT_ETHEREAL = 22
SECT_ASTRAL = 23
SECT_DESERT = 24
SECT_ARCTIC = 25
SECT_SWAMP = 26
SECT_UNDRWLD_MOUNTAIN = 27
SECT_UNDRWLD_SLIME = 28
SECT_UNDRWLD_LOWCEIL = 29
SECT_UNDRWLD_LIQMITH = 30
SECT_UNDRWLD_MUSHROOM = 31
SECT_CASTLE_WALL = 32
SECT_CASTLE_GATE = 33
SECT_CASTLE = 34
SECT_NEG_PLANE = 35
SECT_PLANE_OF_AVERNUS = 36
SECT_ROAD = 37
SECT_SNOWY_FOREST = 38


COLORS = {
    "&+R": "#FF6666", "&+r": "#CC0000",
    "&+W": "#FFFFFF", "&+w": "#CCCCCC",
    "&+Y": "#FFFF66", "&+y": "#CCCC00",
    "&+B": "#6666FF", "&+b": "#0000CC",
    "&+C": "#66FFFF", "&+c": "#00CCCC",
    "&+L": "#666666", "&+l": "#000000",
    "&+M": "#FF66FF", "&+m": "#CC00CC",
    "&+G": "#66FF66", "&+g": "#00CC00",
}


SECTOR_COLORS = {
    SECT_INSIDE: "#E1E1E1",
    SECT_CITY: "#454545",
    SECT_FIELD: "#56725F",
    SECT_FOREST: "#275746",
    SECT_HILLS: "#AE7356",
    SECT_MOUNTAIN: "#755446",
    SECT_WATER_SWIM: "#2970A3",
    SECT_WATER_NOSWIM: "#2970A3",
    SECT_NO_GROUND: "#FFFFFF",
    SECT_UNDERWATER: "#095083",
    SECT_UNDERWATER_GR: "#196093",
    SECT_FIREPLANE: "#9E3134",
    SECT_OCEAN: "#196093",
    SECT_UNDRWLD_WILD: "#CC00CC",
    SECT_UNDRWLD_CITY: "#E1E1E1",
    SECT_UNDRWLD_INSIDE: "#E1E1E1",
    SECT_UNDRWLD_WATER: "#196093",
    SECT_UNDRWLD_NOSWIM: "#095083",
    SECT_UNDRWLD_NOGROUND: "#222222",
    SECT_AIR_PLANE: "#66FFFF",
    SECT_WATER_PLANE: "#196093",
    SECT_EARTH_PLANE: "#D6B56A",
    SECT_ETHEREAL: COLORS["&+l"],
    SECT_ASTRAL: COLORS["&+l"],
    SECT_DESERT: "#D6B56A",
    SECT_ARCTIC: "#FFFFFF",
    SECT_SWAMP: "#AB86AE",
    SECT_UNDRWLD_MOUNTAIN: COLORS["&+L"],
    SECT_UNDRWLD_SLIME: COLORS["&+G"],
    SECT_UNDRWLD_LOWCEIL: COLORS["&+M"],
    SECT_UNDRWLD_LIQMITH: COLORS["&+W"],
    SECT_UNDRWLD_MUSHROOM: "#AB86AE",
    SECT_CASTLE_WALL: COLORS["&+W"],
    SECT_CASTLE_GATE: COLORS["&+L"],
    SECT_CASTLE: COLORS["&+L"],
    SECT_NEG_PLANE: COLORS["&+L"],
    SECT_PLANE_OF_AVERNUS: COLORS["&+R"],
    SECT_ROAD: "#454545",
    SECT_SNOWY_FOREST: COLORS["&+W"],
}


def generate_map_image(map_width, map_height, square_size, starting_vnum, sectors, output_filename):
    print("Generating image...")

    width_px = map_width * square_size
    height_px = map_height * square_size

    image = Image.new("RGB", (width_px, height_px), "#000000")
    pixels = image.load()

    for x in range(map_height):
        for y in range(map_width):
            vnum = starting_vnum + (y * map_width) + x

            if vnum in sectors:
                color = SECTOR_COLORS.get(sectors[vnum], "#000000")

                for i in range(square_size):
                    for j in range(square_size):
                        px = (x * square_size) + i
                        py = (y * square_size) + j
                        pixels[px, py] = tuple(int(color[k:k+2], 16) for k in (1, 3, 5))

    image.save(output_filename)
    print(f"{output_filename} generated.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("dump_map_image makes a png of a duris map .wld file")
        print("syntax: dump_map_image <filename.wld> <map size X> <map size Y> <square size>")
        sys.exit(1)

    filename = sys.argv[1]
    map_x = int(sys.argv[2])
    map_y = int(sys.argv[3])
    square_size = int(sys.argv[4])

    sectors, starting_vnum = get_sectors(filename)
    generate_map_image(map_x, map_y, square_size, starting_vnum, sectors, filename + ".png")