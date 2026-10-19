<p align="center">
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png" alt="gengar" width="150" height="150"/>
</p>

## 🎮 Pokémon Activo del Perfil
* **Nombre:** `Gengar`
* **Altura:** `15`


---

## ⚙️ Cómo funciona Readmedex

`Readmedex` es una **GitHub Action** de uso ludico contenedorizada en Docker que obtiene datos de la PokéAPI de forma dinámica y actualiza la documentación de tu repositorio en cada ejecución tomando un commit como dato de entrada.

### 🏗️ Arquitectura y Flujo de Ejecución

```text
  +-------------------+
  | Flujo de GitHub   |
  | (Evento: Push/Cron)
  +---------+---------+
            |
            v
  +-------------------+        +-----------------------------------+
  | Contenedor Docker | -----> | entrypoint.sh                     |
  | (jesheep99/Readmedex)      | python3 /app/main.py <pokemon>    |
  +-------------------+        +-----------------+-----------------+
                                                 |
                                                 v
  +-------------------+        +-----------------------------------+
  |     PokéAPI       | <----- | main.py (pokebase)                |
  | (pokeapi.co)      | -----> | Obtiene sprite, nombre y altura   |
  +-------------------+        +-----------------+-----------------+
                                                 |
                                                 v
  +-------------------+        +-----------------------------------+
  |  Real-Readme.md   | -----> | Lee la plantilla y reemplaza el   |
  | (Plantilla fija)  |        | marcador (<!--POKEMON_SECTION -->))|
  +-------------------+        +-----------------+-----------------+
                                                 |
                                                 v
                               +-----------------------------------+
                               | Genera el Readme.md final         |
                               +-----------------------------------+

[1. Disparo] ----> [2. Procesar Entrada] ----> [3. Consulta API] ----> [4. Salida Renderizada]
  Ejecución workflow  'pikachu' / ID             Datos de PokéAPI        Readme.md actualizado


- Disparo: El workflow envía el nombre o ID del Pokémon como argumento a la Acción.

- Ejecución: entrypoint.sh ejecuta main.py dentro de un entorno aislado de Python y Docker.

- Procesamiento de Plantilla: main.py lee Real-Readme.md, conserva todo el contenido estático e inyecta el Markdown dinámico del Pokémon justo en el marcador (<!--POKEMON_SECTION -->).

- Salida: Se genera y guarda el archivo Readme.md final de forma automática.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3 (pokebase)

Entorno: Docker / Shell Entrypoint

Automatización: GitHub Actions (CI/CD)