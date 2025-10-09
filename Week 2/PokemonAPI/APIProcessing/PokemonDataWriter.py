from pathlib import Path
import json


class PokemonDataWriter:

    BASE_DATA_PATH = Path("Week 2/PokemonAPI/PokemonData/")

    def __init__(self, folder: str = "", file_name: str = ""):
        self._folder = folder
        self._file_name = file_name

    @property
    def path(self):
        return PokemonDataWriter.BASE_DATA_PATH / self._folder / self._file_name

    @path.setter
    def path(self, value: str):
        if not value:
            raise ValueError("path cannot be set to an empty string")

        if not isinstance(value, str):
            raise TypeError(
                f"path must be of data type string, data type passed: {type(value)}"
            )

        new_path = Path(value)

        self._folder = new_path.parent
        self._file_name = new_path.name

    def write_data_to_file(self, data: str) -> None:
        """
        Writes the provided data to a file in JSON format.

        Parameters
        ----------
        data : str
            The data to be written to the file. Should be a JSON-serializable string.

        Returns
        -------
        None
            This method does not return anything.

        Notes
        -----
        The file is overwritten if it already exists.
        """

        if not self.path.exists():
            self.path.mkdir(parents=True, exist_ok=True)

        with self.path.open("w") as data_file:
            json.dump(data, data_file, indent=4)
