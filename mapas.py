import random

mapas = [
    {
        "dimensiones": "10,10",
        "inicio": (2, 1),
        "fin": (9, 1),
        "mapa": [
            "##########",
            "#        #",
            "#o# ######",
            "#  #  #   #",
            "## # ##   #",
            "#     #   #",
            "# ### #   #",
            "#     #   #",
            "# ### #   #",
            "#x        #",
            "##########",
        ]
    },
    {
        "dimensiones": "10,10",
        "inicio": (0, 2),
        "fin": (8, 9),
        "mapa": [
            "##########",
            "#        #",
            "#o#######",
            "#        #",
            "## #### ##",
            "#        #",
            "# ####### #",
            "#         #",
            "# #####x# #",
            "#         #",
            "###########",
        ]
    },
    # Agrega más mapas si deseas
]

def obtener_mapa_aleatorio():
    return random.choice(mapas)