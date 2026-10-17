import os
import sys
import pokebase as pb

def generate_readme():
    # 1. Validar argumentos de entrada
    if len(sys.argv) < 2:
        print("Error: No se proporcionó el nombre o ID del Pokémon.")
        sys.exit(1)

    in_pokemon = sys.argv[1]

    # 2. Consultar la API
    try:
        pokemon = pb.pokemon(in_pokemon)
        sprite = pokemon.sprites.front_default
    except Exception as e:
        print(f"Error al consultar la PokéAPI: {e}")
        sys.exit(1)

    # 3. Definir la variable del contenido dinámico del Pokémon
    pokemon_markdown = f"""![pok]({sprite})
## Nombre: {pokemon.name.capitalize()}
## Alto: {pokemon.height}
"""

    # 4. Definir constantes de archivos y marcadores
    template_file = "Real-Readme.md"
    output_file = "Readme.md"
    marker = "<!-- POKEMON_SECTION -->"

    # 5. Leer el contenido de la plantilla estática (definición explícita de template_content)
    if not os.path.exists(template_file):
        print(f"Error: No se encontró el archivo {template_file}")
        sys.exit(1)

    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except IOError as e:
        print(f"Error al leer el archivo {template_file}: {e}")
        sys.exit(1)

    # 6. Reemplazar el marcador o aplicar fallback si no existe
    if marker in template_content:
        final_content = template_content.replace(marker, pokemon_markdown)
    else:
        # Fallback de respaldo si no encuentra el marcador
        final_content = f"{pokemon_markdown}\n\n---\n\n{template_content}"

    # 7. Escribir el archivo final de salida
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"¡Éxito! {output_file} generado correctamente.")
    except IOError as e:
        print(f"Error al escribir en {output_file}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()