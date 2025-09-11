import polars as pl
import requests

def obtener_pokemon_gen1():
    """Obtiene lista de Pokémon Gen 1 desde PokéAPI o usa lista básica"""
    try:
        response = requests.get("https://pokeapi.co/api/v2/generation/1/", timeout=5)
        pokemon_data = response.json()['pokemon_species']
        nombres = {p['name'].replace('-', ' ').title() for p in pokemon_data}
        
        # Casos especiales
        if 'Mr Mime' in nombres:
            nombres.remove('Mr Mime')
            nombres.add('Mr. Mime')
        if 'Farfetchd' in nombres:
            nombres.remove('Farfetchd')
            nombres.add("Farfetch'd")
            
        print(f"✅ {len(nombres)} Pokémon Gen 1 obtenidos desde PokéAPI")
        return nombres
    except:
        print("⚠️ Sin conexión - usando validación básica")
        return {'Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Mewtwo'}

def limpiar_datos_pokemon(archivo_csv):
    """
    Limpia datos Pokémon: corrige tipos y valida datos
    """
    
    # 1. LEER ARCHIVO
    try:
        df = pl.read_csv(archivo_csv)
        print(f"📁 Archivo leído: {df.shape[0]} filas, {df.shape[1]} columnas")
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    
    # 2. IDENTIFICAR COLUMNAS
    cols = {
        'nombre': next((c for c in df.columns if 'nombre' in c.lower()), None),
        'tipo1': next((c for c in df.columns if 'tipo' in c.lower() and '1' in c), None),
        'tipo2': next((c for c in df.columns if 'tipo' in c.lower() and '2' in c), None),
        'ataque': next((c for c in df.columns if 'ataque' in c.lower()), None),
        'defensa': next((c for c in df.columns if 'defensa' in c.lower()), None),
        'velocidad': next((c for c in df.columns if 'velocidad' in c.lower()), None),
        'hp': next((c for c in df.columns if any(x in c.lower() for x in ['ps', 'hp', 'vida'])), None)
    }
    
    print("🔍 Columnas encontradas:")
    for nombre, col in cols.items():
        print(f"  {nombre}: {col}")
    
    # 3. OBTENER POKÉMON VÁLIDOS
    pokemon_validos = obtener_pokemon_gen1()
    
    # 4. APLICAR CORRECCIONES
    df_limpio = df.clone()
    cambios = []
    
    # Corregir Tipo 1: Hada/Fairy → Normal
    if cols['tipo1']:
        antes = df_limpio.filter(pl.col(cols['tipo1']).is_in(['Hada', 'Fairy'])).height
        if antes > 0:
            df_limpio = df_limpio.with_columns(
                pl.when(pl.col(cols['tipo1']).is_in(['Hada', 'Fairy']))
                .then(pl.lit('Normal'))
                .otherwise(pl.col(cols['tipo1']))
                .alias(cols['tipo1'])
            )
            cambios.append(f"🔧 {antes} tipos Hada/Fairy → Normal")
    
    # Corregir Tipo 2: eliminar Acero/Steel y Hada/Fairy
    if cols['tipo2']:
        antes = df_limpio.filter(pl.col(cols['tipo2']).is_in(['Acero', 'Steel', 'Hada', 'Fairy'])).height
        if antes > 0:
            df_limpio = df_limpio.with_columns(
                pl.when(pl.col(cols['tipo2']).is_in(['Acero', 'Steel', 'Hada', 'Fairy']))
                .then(pl.lit(""))
                .otherwise(pl.col(cols['tipo2']))
                .alias(cols['tipo2'])
            )
            cambios.append(f"🔧 {antes} tipos secundarios no válidos eliminados")
    
    # Convertir estadísticas a números
    stats_cols = ['ataque', 'defensa', 'velocidad', 'hp']
    for stat in stats_cols:
        col = cols[stat]
        if col and df_limpio[col].dtype not in [pl.Int32, pl.Int64, pl.Float32, pl.Float64]:
            try:
                valores_antes = df_limpio.filter(pl.col(col).is_not_null()).height
                df_limpio = df_limpio.with_columns(
                    pl.col(col).cast(pl.Float64, strict=False).alias(col)
                )
                valores_despues = df_limpio.filter(pl.col(col).is_not_null()).height
                perdidos = valores_antes - valores_despues
                if perdidos > 0:
                    cambios.append(f"🔧 {perdidos} valores no numéricos en {stat} → null")
                else:
                    cambios.append(f"✅ {stat} convertido a numérico")
            except:
                cambios.append(f"❌ No se pudo convertir {stat}")
    
    # Eliminar duplicados
    if cols['nombre']:
        antes_dup = df_limpio.shape[0]
        df_limpio = df_limpio.unique(subset=[cols['nombre']], keep="first")
        despues_dup = df_limpio.shape[0]
        if antes_dup != despues_dup:
            cambios.append(f"🔧 {antes_dup - despues_dup} duplicados eliminados")
    
    # 5. VALIDACIONES RÁPIDAS
    problemas = []
    
    # Nombres
    if cols['nombre'] and len(pokemon_validos) > 10:  # Solo si tenemos lista completa
        invalidos = df_limpio.filter(~pl.col(cols['nombre']).is_in(pokemon_validos)).height
        if invalidos > 0:
            problemas.append(f"⚠️ {invalidos} nombres no son de Gen 1")
    
    # Nulos en estadísticas
    for stat in stats_cols:
        col = cols[stat]
        if col:
            nulos = df_limpio.filter(pl.col(col).is_null()).height
            if nulos > 0:
                problemas.append(f"⚠️ {nulos} valores nulos en {stat}")
    
    # 6. GUARDAR Y REPORTAR
    archivo_salida = archivo_csv.replace('.csv', '_limpio.csv')
    df_limpio.write_csv(archivo_salida)
    
    print(f"\n📊 RESUMEN:")
    print(f"  Original: {df.shape[0]} filas → Limpio: {df_limpio.shape[0]} filas")
    
    if cambios:
        print(f"\n✅ CAMBIOS APLICADOS:")
        for cambio in cambios:
            print(f"  {cambio}")
    
    if problemas:
        print(f"\n⚠️ PROBLEMAS DETECTADOS:")
        for problema in problemas:
            print(f"  {problema}")
    
    print(f"\n💾 Guardado en: {archivo_salida}")
    print(f"\n📋 MUESTRA DEL RESULTADO:")
    print(df_limpio.head())
    
    return df_limpio

# USO
if __name__ == "__main__":
    archivo = r"c:\Users\benja\OneDrive\Documentos\GitHub\Data_science\Tarea_3\pokemones.csv"
    
    try:
        import requests
        resultado = limpiar_datos_pokemon(archivo)
        print("\n🎉 ¡Completado!" if resultado is not None else "\n❌ Falló")
    except ImportError:
        print("❌ Instala requests: pip install requests")