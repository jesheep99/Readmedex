import pokebase as pb
import sys

in_pokemon = sys.argv[1] 


pokemon = pb.pokemon(in_pokemon)
print(pokemon.name) 
#print(pokemon.height)
sprite = pokemon.sprites.front_default
print(sprite)

