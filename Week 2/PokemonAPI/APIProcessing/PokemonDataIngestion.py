import requests
import json
from typing import Any
from PokemonDataWriter import PokemonDataWriter


class PokemonDataIngestion:

    ENDPOINTS = {
        "abilites": "https://pokeapi.co/api/v2/ability/",
        "characteristics": "https://pokeapi.co/api/v2/characteristic/",
        "egg groups": "https://pokeapi.co/api/v2/egg-group/",
        "genders": "https://pokeapi.co/api/v2/gender/",
        "growth rates": "https://pokeapi.co/api/v2/growth-rate/",
        "natures": "https://pokeapi.co/api/v2/nature/",
        "pokemon": "https://pokeapi.co/api/v2/pokemon/",
        "location areas": "https://pokeapi.co/api/v2/pokemon/",
        "colors": "https://pokeapi.co/api/v2/pokemon-color/",
        "forms": "https://pokeapi.co/api/v2/pokemon-form/",
        "habitats": "https://pokeapi.co/api/v2/pokemon-habitat/",
        "shapes": "https://pokeapi.co/api/v2/pokemon-shape/",
        "species": "https://pokeapi.co/api/v2/pokemon-species/",
        "stats": "https://pokeapi.co/api/v2/stat/",
        "types": "https://pokeapi.co/api/v2/type/",
        "moves": "https://pokeapi.co/api/v2/move/",
    }

    def __init__(self, data_type: str):
        self.data_type = data_type
        self.endpoint = PokemonDataIngestion.ENDPOINTS.get(data_type)
        self.data_writer = PokemonDataWriter(
            folder=self.data_type.title().replace(" ", "")
        )

    def get_data_for_id_or_name(self, id: int = None, name: str = "") -> dict[str, Any]:
        """
        Retrieve data for a specific Pokémon by ID or name from the endpoint.

        Parameters
        ----------
        id : int, optional
            The ID of the Pokémon to retrieve. Default is None.
        name : str, optional
            The name of the Pokémon to retrieve. Default is an empty string.

        Returns
        -------
        dict[str, Any]
            The data retrieved from the endpoint as a dictionary.

        Raises
        ------
        ValueError
            If neither `id` nor `name` is provided.
        """

        if not id and not name:
            raise ValueError(
                """
                You must pass a value for either the name or ID to get data from the endpoint.
                """
            )

        response = requests.get(self.endpoint + (str(id) or name))

        response.raise_for_status()

        data = response.json()

        file_name = f"{data.get('name')}.json"

        self.data_writer.path = f"{self.data_type.title().replace(' ', '')}"

        return data

    def get_all_endpoint_data(self) -> list[dict]:

        endpoint_id = 1
        data = {}
        while code := requests.get(self.endpoint + str(endpoint_id)).status_code == 200:
            data[endpoint_id] = requests.get(f"{self.endpoint}{endpoint_id}").json()

            endpoint_id += 1

        return data


test = PokemonDataIngestion("species")

bulbasaur_data = test.get_data_for_id_or_name(1)

test.data_writer.write_data_to_file(data=bulbasaur_data)
