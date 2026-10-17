import pokebase as pb
import sys

in_pokemon = sys.argv[1] 


pokemon = pb.pokemon(in_pokemon)
sprite = pokemon.sprites.front_default

def print_text_to_file(text, filename):
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text successfully written to {filename}")