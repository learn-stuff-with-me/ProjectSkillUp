import requests


class PokemonStats:

    def __init__(self, id: int, base_stat: int, effort: int, **kwargs):
        self.id = id
        self.base_stat = base_stat
        self.effort = effort
        self.name = kwargs.get("name")
        self.is_battle_only = kwargs.get("is_battle_only", False)

    @classmethod
    def get_pokemon_stat(
        cls,
        stat_id: int = None,
        stat_name: str = "",
        base_stat: int = None,
        effort: int = None,
    ):
        url = f"https://pokeapi.co/api/v2/stat/{stat_id or stat_name}"

        data = requests.get(url).json()

        return cls(base_stat=base_stat, effort=effort, **data)

    def __str__(self):
        return f"""
            Name: {self.name}
            Base Stat: {self.base_stat}
            Effort: {self.effort}
            Battle Only: {self.is_battle_only}
            """
