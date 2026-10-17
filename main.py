import os
import sys
import pokebase as pb

def generate_readme():
    if len(sys.argv) < 2:
        print("Error: No se proporcionó el nombre o ID del Pokémon.")
        sys.exit(1)

    in_pokemon = sys.argv[1]

    try:
        pokemon = pb.pokemon(in_pokemon)
        sprite = pokemon.sprites.front_default
    except Exception as e:
        print(f"Error al consultar la PokéAPI: {e}")
        sys.exit(1)

    pokemon_markdown = f"""![pok]({sprite})
## Nombre: {pokemon.name.capitalize()}
## Alto: {pokemon.height}
"""

    # --- RUTAS ABSOLUTAS BASADAS EN EL SCRIPT ---
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(base_dir, "Real-Readme.md")
    output_file = os.path.join(base_dir, "Readme.md")
    marker = "<!-- POKEMON_SECTION -->"

    # Verificar si el archivo existe antes de abrirlo (esto te dirá exactamente el error en los logs)
    if not os.path.exists(template_file):
        print(f"❌ Error crítico: No se encontró 'Real-Readme.md' en la ruta: {template_file}")
        print(f"📁 Contenido actual de {base_dir}: {os.listdir(base_dir)}")
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
        print(f"¡Éxito! {output_file} generado correctamente.")
    except IOError as e:
        print(f"Error al escribir en {output_file}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()