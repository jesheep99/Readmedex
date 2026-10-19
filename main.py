import os
import random
import sys
import pokebase as pb

def generate_readme():
    if len(sys.argv) < 2:
        print("Error: No se proporcionó el nombre o ID del Pokémon.")
        sys.exit(1)

    in_pokemon = sys.argv[1]

    try:
        pokemon = pb.pokemon(in_pokemon)
        
        # 1. Probabilidad del 10% de que salga la versión Shiny (¡Sorpresa!)
        is_shiny = random.random() < 0.10
        sprite = pokemon.sprites.front_shiny if is_shiny and pokemon.sprites.front_shiny else pokemon.sprites.front_default
        shiny_label = " ✨ [Shiny] ✨" if is_shiny else ""

        # 2. Extraer los tipos del Pokémon
        types = [t.type.name.capitalize() for t in pokemon.types]
        types_str = " / ".join(types)

        # 3. Extraer estadísticas principales y generar barras visuales
        stats_dict = {}
        for s in pokemon.stats:
            stat_name = s.stat.name
            stat_value = s.base_stat
            # Normalizar barra a un máximo de 10 bloques (asumiendo max stat ~150)
            filled_blocks = min(int((stat_value / 150) * 10), 10)
            empty_blocks = 10 - filled_blocks
            bar = "█" * filled_blocks + "░" * empty_blocks
            stats_dict[stat_name] = (stat_value, bar)

        hp_val, hp_bar = stats_dict.get('hp', (0, '░'*10))
        atk_val, atk_bar = stats_dict.get('attack', (0, '░'*10))
        def_val, def_bar = stats_dict.get('defense', (0, '░'*10))

    except Exception as e:
        print(f"Error al consultar la PokéAPI: {e}")
        sys.exit(1)

    # 4. Construir el bloque dinámico mejorado con las tarjetas y estadísticas
    pokemon_markdown = f"""<p align="center">
  <img src="{sprite}" alt="{pokemon.name}" width="160" height="160"/>
</p>

## 🎮 Pokémon Activo del Perfil{shiny_label}
* **Nombre:** `{pokemon.name.capitalize()}`
* **Tipo(s):** `{types_str}`
* **Altura:** `{pokemon.height / 10} m` | **Peso:** `{pokemon.weight / 10} kg`

### 📊 Estadísticas Base
* **HP:** `[{hp_bar}]` `{hp_val}`
* **Ataque:** `[{atk_bar}]` `{atk_val}`
* **Defensa:** `[{def_bar}]` `{def_val}`
"""

    # Rutas y constantes
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(base_dir, "Real-Readme.md")
    output_file = os.path.join(base_dir, "Readme.md")
    marker = "<!-- POKEMON_SECTION -->"

    if not os.path.exists(template_file):
        print(f"❌ Error crítico: No se encontró 'Real-Readme.md' en {template_file}")
        sys.exit(1)

    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        sys.exit(1)

    if marker in template_content:
        final_content = template_content.replace(marker, pokemon_markdown)
    else:
        final_content = f"{pokemon_markdown}\n\n---\n\n{template_content}"

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"¡Éxito! {output_file} generado con las mejoras visuales.")
    except IOError as e:
        print(f"Error al escribir en {output_file}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()