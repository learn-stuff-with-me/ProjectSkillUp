import requests


class PokemonSpecies:

    def __init__(self, id: int, **kwargs):
        self.id = id
        self.name = kwargs.get("name")
        self.capture_rate = kwargs.get("capture_rate")
        self.base_happiness = kwargs.get("base_happiness")
        self.is_legendary = kwargs.get("is_legendary")
        self.is_mythical = kwargs.get("is_mythical")
        self.has_gender_differences = kwargs.get("has_gender_differences")

    @classmethod
    def get_pokemon_species(cls, species_id: int):
        url = f"https://pokeapi.co/api/v2/pokemon-species/{species_id}"

        data = requests.get(url).json()

        return cls(**data)

    def __str__(self):
        return f"""
            Capture Rate: {self.capture_rate}
            Base Happiness: {self.base_happiness}
            Legendary: {self.is_legendary}
            Mythical: {self.is_mythical}
            Gender Differences: {self.has_gender_differences}
            """
