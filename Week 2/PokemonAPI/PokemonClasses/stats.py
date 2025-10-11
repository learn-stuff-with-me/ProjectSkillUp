from dataclasses import dataclass


@dataclass
class Stat:
    name: str
    base_stat: int
    effort: int

    def __str__(self):
        return (
            f"Name: {self.name}\nBase Stat: {self.base_stat}\nEffort: {self.effort}\n"
        )
