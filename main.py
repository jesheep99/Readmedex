import pokebase as pb
import sys

# 1. Validar que se reciba el argumento del Pokémon
if len(sys.argv) < 2:
    print("Error: No se proporcionó el nombre o ID del Pokémon.")
    sys.exit(1)

in_pokemon = sys.argv[1]

try:
    # 2. Obtener datos desde la PokéAPI
    pokemon = pb.pokemon(in_pokemon)
    sprite = pokemon.sprites.front_default
except Exception as e:
    print(f"Error al consultar la PokéAPI para '{in_pokemon}': {e}")
    sys.exit(1)

# 3. Construir el bloque dinámico del Pokémon (que irá arriba)
pokemon_markdown = f"""<p align="center">
  <img src="{sprite}" alt="{pokemon.name}" width="150" height="150"/>
</p>

## 🎮 Pokémon Activo del Perfil
* **Nombre:** `{pokemon.name.capitalize()}`
* **Altura:** `{pokemon.height}`
"""

TEMPLATE_FILE = "Real-Readme.md"
OUTPUT_FILE = "Readme.md"
MARKER = "<!-- POKEMON_SECTION -->"

def generate_readme():
    try:
        # 4. Leer la plantilla fija (Real-Readme.md)
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # 5. Reemplazar el marcador por la información del Pokémon
        if MARKER in template_content:
            final_content = template_content.replace(MARKER, pokemon_markdown)
        else:
            # Fallback por si el marcador no está: coloca el Pokémon arriba por defecto
            final_content = f"{pokemon_markdown}\n\n---\n\n{template_content}"

        # 6. Escribir el archivo final (Readme.md)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(final_content)

        print(f"¡Éxito! {OUTPUT_FILE} generado correctamente usando {TEMPLATE_FILE}.")

    except IOError as e:
        print(f"Error de E/S al procesar los archivos Markdown: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()