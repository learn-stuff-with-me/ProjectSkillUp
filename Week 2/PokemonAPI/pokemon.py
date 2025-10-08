from typing import Any, Self
import requests

import moves
from species import PokemonSpecies
import generations
import types
from stats import PokemonStats
import abilities
import habitats
import natures
import forms


class Pokemon:

    def __init__(
        self,
        id: int,
        name: str = "",
        base_experience: int = None,
        height: int = None,
        weight: int = None,
        **kwargs,
    ):
        self.id = id
        self.name = name
        self.base_experience = base_experience
        self.height = height
        self.weight = weight
        self.stats = kwargs.get("stats", None)
        self.moves = kwargs.get("moves", None)
        self.types = kwargs.get("types", None)
        self.abilities = kwargs.get("abilities", None)
        self.species = PokemonSpecies.get_pokemon_species(id)

    def setup_stats(self):
        all_stats = []
        if self.stats:
            for stat in self.stats:
                base_stat = stat.get("base_stat")
                effort = stat.get("effort")
                name = stat.get("stat").get("name")
                all_stats.append(
                    PokemonStats.get_pokemon_stat(
                        stat_name=name, base_stat=base_stat, effort=effort
                    )
                )

        self.stats = all_stats


pokemon_id = 1
data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}").json()

bulbasaur = Pokemon(**data)

bulbasaur.setup_stats()

print("do something")
