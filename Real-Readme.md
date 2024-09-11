# este proyecto es una pruba de concepto 

es una accion que consuta la api de pokeapi 
atravez de pokebase

# funcionamiento

toma un commit y usa ese commit message como (${{ github.event.head_commit.message }})
variable de entrada para el script python. 
la variable de entrada hacia el script python provienes
del worflow del mismo repositorio y ingresa desde el entrypoint.sh ($1)
de el dockerfile
