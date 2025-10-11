from dataclasses import dataclass


@dataclass
class Ability:
    ability_name: str
    is_hidden: bool
