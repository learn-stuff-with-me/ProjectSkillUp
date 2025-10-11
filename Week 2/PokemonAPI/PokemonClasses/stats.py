from dataclasses import dataclass


@dataclass
class Stat:
    name: str
    base_stat: int
    effort: int
