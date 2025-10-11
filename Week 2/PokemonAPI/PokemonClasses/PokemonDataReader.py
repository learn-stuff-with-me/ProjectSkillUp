import json
from pathlib import Path
from typing import Any


class PokemonDataReader:

    BASE_PATH = "Week 2/PokemonAPI/PokemonData/pokemon"

    def __init__(self, pokemon_name: str):
        self.pokemon_name = pokemon_name
        self.path = Path(PokemonDataReader.BASE_PATH) / f"{self.pokemon_name}.json"

    def read_pokemon_data(self) -> dict[str, Any]:
        if not self.path.exists():
            raise FileNotFoundError(
                f"Could not find the file in the location {self.path}"
            )

        with self.path.open("r") as pokemon_file:
            pokemon_data = json.load(pokemon_file)

        return pokemon_data
