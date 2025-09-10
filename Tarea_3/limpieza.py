import polars as pl

def limpiar_datos_pokemon(ruta_archivo):
    """
    Limpia y valida datos de Pokémon de primera generación
    """
    
    # Leer el archivo CSV
    try:
        df = pl.read_csv(ruta_archivo)
        print(f"✅ Archivo leído exitosamente: {df.shape[0]} filas, {df.shape[1]} columnas")
        print(f"Columnas encontradas: {df.columns}")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None
    
    print("\n" + "="*60)
    print("ANÁLISIS INICIAL DE DATOS")
    print("="*60)
    
    # Mostrar información básica
    print(df.describe())
    print(f"\nPrimeras 5 filas:")
    print(df.head())
    
    # Pokémon válidos de primera generación (1-151)
    pokemon_gen1 = {
        'Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard',
        'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree',
        'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot',
        'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok',
        'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran♀', 'Nidorina',
        'Nidoqueen', 'Nidoran♂', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable',
        'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat',
        'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat',
        'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck',
        'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag',
        'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop',
        'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool',
        'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash',
        'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Farfetch\'d', 'Doduo',
        'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder',
        'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee',
        'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute',
        'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung',
        'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela',
        'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu',
        'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar',
        'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto',
        'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte',
        'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno',
        'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew'
    }
    
    # ❌ SOLO TIPOS DE GEN 1 - NO INCLUYE HADA/FAIRY
    tipos_validos = {
        'Normal', 'Fuego', 'Agua', 'Eléctrico', 'Planta', 'Hielo', 'Lucha',
        'Veneno', 'Tierra', 'Volador', 'Psiquico', 'Bicho', 'Roca', 'Fantasma', 'Dragón',
        # También en inglés por si acaso
        'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting',
        'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon'
    }
    
    print("\n" + "="*60)
    print("DETECCIÓN DE PROBLEMAS")
    print("="*60)
    
    problemas_encontrados = []
    
    # ✅ DETECCIÓN DE COLUMNAS CORREGIDA - Mapeo directo por nombre exacto
    col_nombre = 'Nombre' if 'Nombre' in df.columns else None
    col_tipo1 = 'Tipo 1' if 'Tipo 1' in df.columns else None
    col_tipo2 = 'Tipo 2' if 'Tipo 2' in df.columns else None
    col_ataque = 'Ataque' if 'Ataque' in df.columns else None
    col_defensa = 'Defensa' if 'Defensa' in df.columns else None
    col_velocidad = 'Velocidad' if 'Velocidad' in df.columns else None
    col_hp = 'PS' if 'PS' in df.columns else None
    
    print(f"Columnas identificadas:")
    print(f"  Nombre: {col_nombre}")
    print(f"  Tipo 1: {col_tipo1}")
    print(f"  Tipo 2: {col_tipo2}")
    print(f"  Ataque: {col_ataque}")
    print(f"  Defensa: {col_defensa}")
    print(f"  Velocidad: {col_velocidad}")
    print(f"  HP/PS: {col_hp}")
    
    # 1. Valores nulos o vacíos
    if col_nombre:
        nulos_nombre = df.filter(pl.col(col_nombre).is_null() | (pl.col(col_nombre) == "")).height
        if nulos_nombre > 0:
            problemas_encontrados.append(f"❌ {nulos_nombre} filas con nombres nulos o vacíos")
            print(f"❌ {nulos_nombre} filas con nombres nulos o vacíos")
    
    # 2. Validar nombres de Pokémon de Gen 1
    if col_nombre:
        df_validacion = df.with_columns([
            pl.col(col_nombre).is_in(pokemon_gen1).alias("pokemon_valido")
        ])
        nombres_invalidos = df_validacion.filter(~pl.col("pokemon_valido"))
        if nombres_invalidos.height > 0:
            problemas_encontrados.append(f"❌ {nombres_invalidos.height} Pokémon no válidos de Gen 1")
            print(f"❌ {nombres_invalidos.height} Pokémon no válidos de Gen 1:")
            print(nombres_invalidos.select([col_nombre]).unique())
    
    # 3. Validar tipos - AQUÍ SE VA A DETECTAR HADA COMO INVÁLIDO
    if col_tipo1:
        tipos_unicos1 = df.filter(pl.col(col_tipo1).is_not_null()).select(pl.col(col_tipo1).unique()).to_series().to_list()
        print(f"\n🔍 Tipos primarios encontrados en tu archivo: {tipos_unicos1}")
        
        tipos_invalidos1 = df.filter(
            ~pl.col(col_tipo1).is_in(tipos_validos) & 
            pl.col(col_tipo1).is_not_null()
        )
        
        if tipos_invalidos1.height > 0:
            tipos_malos = tipos_invalidos1.select(pl.col(col_tipo1).unique()).to_series().to_list()
            problemas_encontrados.append(f"❌ {tipos_invalidos1.height} filas con tipos primarios inválidos")
            print(f"❌ {tipos_invalidos1.height} filas con tipos primarios inválidos")
            print(f"   Tipos inválidos encontrados: {tipos_malos}")
            
            # Mostrar qué Pokémon tienen estos tipos inválidos
            if col_nombre:
                pokemon_con_tipos_malos = tipos_invalidos1.select([col_nombre, col_tipo1]).unique()
                print(f"   Pokémon afectados:")
                print(pokemon_con_tipos_malos)
    else:
        print("⚠️ No se pudo detectar la columna 'Tipo 1'")
    
    if col_tipo2:
        tipos_unicos2 = df.filter(pl.col(col_tipo2).is_not_null() & (pl.col(col_tipo2) != "")).select(pl.col(col_tipo2).unique()).to_series().to_list()
        print(f"🔍 Tipos secundarios encontrados en tu archivo: {tipos_unicos2}")
        
        tipos_invalidos2 = df.filter(
            ~pl.col(col_tipo2).is_in(tipos_validos) & 
            pl.col(col_tipo2).is_not_null() & 
            (pl.col(col_tipo2) != "")
        )
        
        if tipos_invalidos2.height > 0:
            tipos_malos2 = tipos_invalidos2.select(pl.col(col_tipo2).unique()).to_series().to_list()
            problemas_encontrados.append(f"❌ {tipos_invalidos2.height} filas con tipos secundarios inválidos")
            print(f"❌ {tipos_invalidos2.height} filas con tipos secundarios inválidos")
            print(f"   Tipos inválidos encontrados: {tipos_malos2}")
    else:
        print("⚠️ No se pudo detectar la columna 'Tipo 2'")
    
    # 4. Validar estadísticas
    columnas_stats = [
        (col_ataque, "Ataque", 1, 255),
        (col_defensa, "Defensa", 1, 255),
        (col_velocidad, "Velocidad", 1, 255),
        (col_hp, "HP/PS", 1, 255)
    ]
    
    for col, nombre, min_val, max_val in columnas_stats:
        if col:
            # Valores nulos
            nulos = df.filter(pl.col(col).is_null()).height
            if nulos > 0:
                problemas_encontrados.append(f"❌ {nulos} valores nulos en {nombre}")
                print(f"❌ {nulos} valores nulos en {nombre}")
            
            # Valores fuera de rango
            fuera_rango = df.filter(
                (pl.col(col) < min_val) | (pl.col(col) > max_val)
            ).height
            if fuera_rango > 0:
                problemas_encontrados.append(f"❌ {fuera_rango} valores de {nombre} fuera del rango ({min_val}-{max_val})")
                print(f"❌ {fuera_rango} valores de {nombre} fuera del rango ({min_val}-{max_val})")
    
    # 5. Duplicados
    if col_nombre:
        duplicados = df.group_by(col_nombre).len().filter(pl.col("len") > 1)
        if duplicados.height > 0:
            problemas_encontrados.append(f"❌ {duplicados.height} Pokémon duplicados")
            print(f"❌ {duplicados.height} Pokémon duplicados:")
            print(duplicados)
    
    print("\n" + "="*60)
    print("RESUMEN DE LIMPIEZA")
    print("="*60)
    
    if not problemas_encontrados:
        print("✅ ¡Perfecto! No se encontraron problemas en los datos.")
        return df
    else:
        print(f"Se encontraron {len(problemas_encontrados)} tipos de problemas:")
        for problema in problemas_encontrados:
            print(f"  {problema}")
    
    # Crear DataFrame limpio ELIMINANDO TIPOS INVÁLIDOS
    print("\n🧹 Creando dataset limpio (ELIMINANDO tipos Hada/Fairy)...")
    
    condiciones_limpieza = []
    
    if col_nombre:
        condiciones_limpieza.append(pl.col(col_nombre).is_not_null())
        condiciones_limpieza.append(pl.col(col_nombre) != "")
        condiciones_limpieza.append(pl.col(col_nombre).is_in(pokemon_gen1))
    
    # ESTA ES LA PARTE CRÍTICA - ELIMINA FILAS CON TIPOS INVÁLIDOS
    if col_tipo1:
        condiciones_limpieza.append(pl.col(col_tipo1).is_in(tipos_validos))
    
    if col_tipo2:
        # Para tipo2, permitir nulos o vacíos, pero si tiene valor debe ser válido
        condiciones_limpieza.append(
            (pl.col(col_tipo2).is_null()) | 
            (pl.col(col_tipo2) == "") | 
            (pl.col(col_tipo2).is_in(tipos_validos))
        )
    
    # Aplicar filtros
    if condiciones_limpieza:
        # 🔍 IDENTIFICAR QUÉ FILAS SE VAN A ELIMINAR ANTES DE HACERLO
        filas_validas = pl.all_horizontal(condiciones_limpieza)
        df_limpio = df.filter(filas_validas)
        df_eliminadas = df.filter(~filas_validas)  # ← Las que NO cumplen las condiciones
        
        # Remover duplicados
        duplicados_eliminados = None
        if col_nombre:
            # Identificar duplicados antes de eliminar
            antes_duplicados = df_limpio.shape[0]
            duplicados_encontrados = df_limpio.group_by(col_nombre).len().filter(pl.col("len") > 1)
            if duplicados_encontrados.height > 0:
                print(f"\n🔍 Duplicados que se van a eliminar:")
                print(duplicados_encontrados)
                # Guardar los duplicados que se eliminan
                duplicados_eliminados = df_limpio.group_by(col_nombre).tail(n=-1)  # Todos excepto el primero
                
            df_limpio = df_limpio.unique(subset=[col_nombre], keep="first")
            despues_duplicados = df_limpio.shape[0]
            duplicados_removidos = antes_duplicados - despues_duplicados
        
        filas_eliminadas_total = df.shape[0] - df_limpio.shape[0]
        print(f"✅ Dataset limpio creado: {df_limpio.shape[0]} filas")
        print(f"🗑️ TOTAL ELIMINADAS: {filas_eliminadas_total} filas")
        
        # 📋 MOSTRAR DETALLES DE LO QUE SE ELIMINÓ
        if df_eliminadas.height > 0:
            print(f"\n📋 DETALLES DE LAS {df_eliminadas.height} FILAS ELIMINADAS POR DATOS INVÁLIDOS:")
            
            if col_nombre and col_tipo1:
                eliminadas_detalle = df_eliminadas.select([col_nombre, col_tipo1, col_tipo2] if col_tipo2 else [col_nombre, col_tipo1])
                print(eliminadas_detalle)
                
                # Agrupar por razón de eliminación
                print(f"\n🔍 RAZONES DE ELIMINACIÓN:")
                
                # Pokémon no válidos
                pokemon_invalidos = df_eliminadas.filter(~pl.col(col_nombre).is_in(pokemon_gen1))
                if pokemon_invalidos.height > 0:
                    print(f"  • {pokemon_invalidos.height} Pokémon no válidos de Gen 1:")
                    print(f"    {pokemon_invalidos.select(col_nombre).unique().to_series().to_list()}")
                
                # Tipos inválidos
                if col_tipo1:
                    tipos1_invalidos = df_eliminadas.filter(~pl.col(col_tipo1).is_in(tipos_validos))
                    if tipos1_invalidos.height > 0:
                        tipos_malos_eliminados = tipos1_invalidos.select(pl.col(col_tipo1).unique()).to_series().to_list()
                        print(f"  • {tipos1_invalidos.height} filas con Tipo 1 inválido: {tipos_malos_eliminados}")
                        
                        # Mostrar qué Pokémon específicos
                        pokemon_tipo1_malo = tipos1_invalidos.select([col_nombre, col_tipo1]).unique()
                        print(f"    Pokémon afectados:")
                        for row in pokemon_tipo1_malo.iter_rows():
                            print(f"      - {row[0]}: {row[1]}")
                
                if col_tipo2:
                    tipos2_invalidos = df_eliminadas.filter(
                        ~pl.col(col_tipo2).is_in(tipos_validos) & 
                        pl.col(col_tipo2).is_not_null() & 
                        (pl.col(col_tipo2) != "")
                    )
                    if tipos2_invalidos.height > 0:
                        tipos_malos2_eliminados = tipos2_invalidos.select(pl.col(col_tipo2).unique()).to_series().to_list()
                        print(f"  • {tipos2_invalidos.height} filas con Tipo 2 inválido: {tipos_malos2_eliminados}")
        
        # Mostrar duplicados eliminados
        if col_nombre and duplicados_removidos > 0:
            print(f"\n📋 DUPLICADOS ELIMINADOS: {duplicados_removidos} filas")
            if duplicados_eliminados is not None and duplicados_eliminados.height > 0:
                print("  Pokémon duplicados eliminados:")
                print(duplicados_eliminados.select([col_nombre]))
        
        # Guardar dataset limpio
        ruta_salida = ruta_archivo.replace('.csv', '_limpio.csv')
        df_limpio.write_csv(ruta_salida)
        print(f"\n💾 Dataset limpio guardado en: {ruta_salida}")
        
        # 💾 GUARDAR TAMBIÉN LAS FILAS ELIMINADAS PARA REVISIÓN
        if df_eliminadas.height > 0:
            ruta_eliminadas = ruta_archivo.replace('.csv', '_eliminadas.csv')
            df_eliminadas.write_csv(ruta_eliminadas)
            print(f"🗑️ Filas eliminadas guardadas en: {ruta_eliminadas}")
        
        return df_limpio
    else:
        print("⚠️ No se pudieron aplicar filtros de limpieza")
        return df

# Uso del código
if __name__ == "__main__":
    # CAMBIA ESTA RUTA POR LA DE TU ARCHIVO
    ruta_archivo = r"c:\Users\benja\OneDrive\Documentos\GitHub\Data_science\Tarea_3\pokemones.csv"
    
    df_limpio = limpiar_datos_pokemon(ruta_archivo)
    
    if df_limpio is not None:
        print("\n🎉 ¡Proceso de limpieza completado!")
        print(f"Dimensiones finales: {df_limpio.shape}")