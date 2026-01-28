from textual.theme import Theme

class MyThemes:
    minecraft_theme = Theme(
        name="minecraft",
        # Colores base inspirados en el entorno de Minecraft
        primary="#5E8C31",      # Verde de hierba (grass block)
        secondary="#8B5E3C",    # Marrón de madera (oak wood)
        accent="#FF4500",       # Naranja-rojo de lava o fuego
        foreground="#F0F0F0",   # Texto claro (como el menú de Minecraft)
        background="#1A1A1A",   # Fondo oscuro (noche en el Overworld)
        success="#5E8C31",      # Verde de hierba (también usado para "éxito")
        warning="#D2691E",      # Marrón dorado (arena o advertencia)
        error="#B22222",        # Rojo ladrillo (bloque de piedra roja o error)
        surface="#2D2D2D",      # Panel oscuro (como piedra)
        panel="#3C3C3C",        # Contenedores (como cofres)
        dark=True,
        variables={
            # Cursor tipo bloque (como en consola de comandos de Minecraft)
            "block-cursor-text-style": "reverse",
            # Atajos en el footer: color de texto como esmeralda
            "footer-key-foreground": "#5E8C31",
            # Selección en inputs: semi-transparente como vidrio teñido
            "input-selection-background": "#5E8C31 40%",
            # Borde de widgets activos: lava suave
            "focus-border": "#FF4500",
            # Fondo de botones en hover: madera clara
            "button-hover-background": "#A07655",
        },
        
    )

    nether_theme = Theme(
        name="nether",
        # Colores del Nether: lava, fuego, netherrack, obsidiana, fuego del alma
        primary="#FF5555",      # Rojo lava brillante
        secondary="#BD4F4F",    # Netherrack oscuro
        accent="#FFAA33",       # Fuego naranja (llamas)
        foreground="#FFE8D6",   # Texto claro (como las partículas de fuego)
        background="#0C0A09",   # Fondo: oscuridad del Nether (casi negro)
        success="#55AA55",      # Verde esmeralda (para contrastar, como en cofres)
        warning="#FFAA33",      # Fuego naranja (advertencia = calor)
        error="#FF2222",        # Lava hirviendo (rojo intenso)
        surface="#1A1210",      # Superficie: piedra del Nether (negro-rojizo)
        panel="#2A1B17",        # Paneles: cofre del Nether o bastión
        dark=True,
        variables={
            # Cursor tipo bloque, estilo "fuego"
            "block-cursor-text-style": "reverse",
            # Atajos en footer: color de fuego del alma
            "footer-key-foreground": "#55FFFF",  # Cian suave (como soul fire)
            # Selección en inputs: lava translúcida
            "input-selection-background": "#FF5555 30%",
            # Borde al hacer foco: fuego naranja
            "focus-border": "#FFAA33",
            # Fondo de botón al pasar el ratón: netherrack más claro
            "button-hover-background": "#D16060",
        },
    )

    end_theme = Theme(
        name="end",
        # Colores del End: vacío, portal, ojo del ender, obsidiana
        primary="#B388EB",      # Púrpura del portal del End
        secondary="#6A5ACD",    # Azul pizarra (como el cielo del End)
        accent="#FFD700",       # Dorado brillante (como los trofeos del dragón)
        foreground="#E6E6FA",   # Lavanda claro (texto legible en el vacío)
        background="#0D021A",   # Fondo: oscuridad profunda del End
        success="#50C878",      # Esmeralda (para contrastar con cofres del End)
        warning="#FFD700",      # Dorado (advertencia = poder del dragón)
        error="#FF4567",        # Rosa intenso (como partículas del Endermite)
        surface="#150828",      # Superficie: piedra del End (negro-púrpura)
        panel="#1E1038",        # Paneles: cofre del End / estructura de obsidiana
        dark=True,
        variables={
            # Cursor tipo bloque: estilo "ojo del ender"
            "block-cursor-text-style": "reverse",
            # Atajos en footer: color del portal activo
            "footer-key-foreground": "#B388EB",
            # Selección en inputs: resplandor púrpura translúcido
            "input-selection-background": "#B388EB 35%",
            # Borde al hacer foco: dorado del trofeo
            "focus-border": "#FFD700",
            # Fondo de botón al pasar el ratón: púrpura más claro
            "button-hover-background": "#9A67EA",
        },
    )