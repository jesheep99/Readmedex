import pokebase as pb
import sys

in_pokemon = sys.argv[1] 


pokemon = pb.pokemon(in_pokemon)
print(pokemon.name) 
print(pokemon.height)
sprite = pokemon.sprites.front_default
print(sprite)



def print_text_to_file(text, filename):
    """Prints the given text to a file.

    Args:
        text (str): The text to be printed.
        filename (str): The name of the file to write to.
    """

    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text successfully written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Example usage:
text_to_print = f"""![pok]({sprite})
## nombre : {pokemon.name}
## alto: {pokemon.height}
"""


filename = "Readme.md"

print_text_to_file(text_to_print, filename)

