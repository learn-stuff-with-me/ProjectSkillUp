from typing import Any, Self
from PokemonDataReader import PokemonDataReader
from abilities import Ability
from stats import Stat


class Pokemon:

    def __init__(
        self,
        name: str,
        id: int = None,
        base_experience: int = None,
        height: int = None,
        weight: int = None,
    ):
        self.id = id
        self.name = name
        self.base_experience = base_experience
        self.height = height
        self.weight = weight
        self.data_reader = PokemonDataReader(self.name)
        self.abilities = None
        self.moves = None
        self.stats = None
        self.types = None
        self.forms = None

    def read_all_data(self) -> None:
        """
        Reads and parses all relevant Pokémon data from the data reader.

        This method loads Pokémon data and sequentially parses abilities, forms, moves,
        stats, and types, storing the processed information in the corresponding attributes.

        Returns
        -------
        None
            This method does not return any value. It updates instance attributes with parsed data.
        """
        self.pokemon_data = self.data_reader.read_pokemon_data()
        self._parse_abilities()
        self._parse_forms()
        self._parse_moves()
        self._parse_stats()
        self._parse_types()

    def _parse_abilities(self) -> None:
        """
        Parses the abilities from the Pokémon data and initializes the abilities attribute.
        Extracts each ability's name and hidden status from the `pokemon_data` dictionary,
        creates an `Ability` object for each, and stores them in the `abilities` attribute.

        Returns
        -------
        None
            This method does not return anything. It sets the `abilities` attribute.
        """
        all_abilities = []
        for ability in self.pokemon_data.get("abilities"):
            all_abilities.append(
                Ability(ability.get("ability").get("name"), ability.get("is_hidden"))
            )

        self.abilities = all_abilities

    def _parse_forms(self) -> None:
        """
        Parses the 'forms' data from the Pokémon information and sets the 'forms' attribute.
        If multiple forms are present, assigns a list of form names to 'self.forms'.
        If only one form is present, assigns the single form name to 'self.forms'.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        forms = self.pokemon_data.get("forms")
        if len(forms) > 1:
            all_forms = []

            for form in forms:
                all_forms.append(form.get("name"))

            self.forms = all_forms

        else:
            self.forms = forms[0].get("name")

    def _parse_moves(self) -> None:
        """
        Parses the moves from the Pokémon data and stores their names.
        Retrieves the list of moves from the `pokemon_data` attribute, extracts the name of each move,
        and assigns the list of move names to the `moves` attribute.

        Returns
        -------
        None
            This method does not return anything. The result is stored in the `moves` attribute.
        """
        moves = self.pokemon_data.get("moves")

        all_moves = []

        for move in moves:
            all_moves.append(move.get("move").get("name"))

        self.moves = all_moves

    def _parse_stats(self) -> None:
        """
        Parses the stats from the Pokémon data and initializes the `self.stats` attribute.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Extracts the 'stats' field from `self.pokemon_data`, creates `Stat` objects for each stat,
        and stores them in the `self.stats` attribute.
        """
        stats = self.pokemon_data.get("stats")

        all_stats = []

        for stat in stats:
            all_stats.append(
                Stat(
                    stat.get("stat").get("name"),
                    stat.get("base_stat"),
                    stat.get("effort"),
                )
            )

        self.stats = all_stats

    def _parse_types(self) -> None:
        """
        Parses the types information from the Pokémon data and assigns it to the `self.types` attribute.
        If the Pokémon has multiple types, `self.types` will be a list of type names.
        If the Pokémon has a single type, `self.types` will be a string representing the type name.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Assumes `self.pokemon_data` contains a "types" key with a list of type dictionaries.
        """
        types = self.pokemon_data.get("types")

        if len(types) > 1:
            all_types = []

            for type in types:
                all_types.append(type.get("type").get("name"))

            self.types = all_types

        else:
            self.types = types[0].get("type").get("name")


bulbasaur = Pokemon("bulbasaur")

bulbasaur.read_all_data()

print()
