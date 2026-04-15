function duris.map:setCustomColors()
    duris.log:debug("Setting color environment")

    -- Remap mud IDs to non-ANSI range
    for _, v in pairs(gmcp.room.sectors.sectors) do
        duris.map.terrain[v.name] = v.id + 16
    end

    local alpha = 255
    local terrain = duris.map.terrain
    local colors  = color_table

    local function set(terrainName, colorName)
        local r, g, b = unpack(colors[colorName])
        setCustomEnvColor(terrain[terrainName], r, g, b, alpha)
    end

    local mappings = {
        -- Roads
        road               = "DarkGoldenrod",
        path           = "tan",

        -- Misc
        inside             = "light_gray",
        city               = "LightCoral",
        unused             = "slate_grey",
        areaexit           = "dim_gray",
        castle             = "plum",
        pillar             = "light_pink",
        temple             = "medium_purple",
        shop               = "orange",
        clanexit           = "red",
        chessblack         = "dim_gray",
        chesswhite         = "white",
        lottery            = "yellow_green",
        alley              = "yellow",
        office             = "linen",
        electric           = "DodgerBlue",
        well               = "DarkSlateBlue",
        bloodyhall         = "maroon",
        bloodyroom         = "firebrick",
        palace_room        = "MediumOrchid",
        ship               = "SaddleBrown",

        -- Weather / Environment
        mist               = "alice_blue",
        snow               = "snow",
        rain               = "cyan",
        sun                = "gold",
        lightning          = "steel_blue",
        rainbow            = "DeepPink",

        -- Outdoors
        plain              = "papaya_whip",
        field              = "yellow_green",
        forest             = "ForestGreen",
        mountain           = "RosyBrown",
        desert             = "moccasin",
        cave               = "dark_orange",
        beach              = "LightGoldenrod",

        -- Water
        waterswim          = "cornflower_blue",
        waternoswim        = "medium_slate_blue",
        ocean              = "deep_sky_blue",
        river              = "medium_aquamarine",
        underwater         = "NavyBlue",

        -- Hell
        hellinside         = "maroon",
        hellhall           = "violet_red",
        hell1              = "red",
        hell2              = "tomato",
        hell3              = "OrangeRed",
        hell4              = "coral",

        -- Space
        space1             = "light_grey",
        space2             = "gray",
        space3             = "dim_gray",
        space4             = "dark_slate_grey",
    }

    for terrainName, colorName in pairs(mappings) do
        set(terrainName, colorName)
    end
end
