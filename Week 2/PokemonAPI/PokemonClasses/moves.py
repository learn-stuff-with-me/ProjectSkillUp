import requests


class PokemonMoves:

    def __init__(self, id: int, base_stat: int, effort: int, **kwargs):
        self.id = id
        self.base_stat = base_stat
        self.effort = effort
        self.name = kwargs.get("name")
        self.is_battle_only = kwargs.get("is_battle_only", False)

    @classmethod
    def get_pokemon_moves(cls, move_id: int = None, move_name: str = ""):
        url = f"https://pokeapi.co/api/v2/move/{move_id or move_name}"

        data = requests.get(url).json()

        return cls(**data)

    def __str__(self):
        return f"""
            Name: {self.name}
            Base Stat: {self.base_stat}
            Effort: {self.effort}
            Battle Only: {self.is_battle_only}
            """
