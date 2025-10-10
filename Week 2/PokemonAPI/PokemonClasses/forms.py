from dataclasses import dataclass


@dataclass
class Forms:
    form_id: int
    name: str
    order: int
    form_order: int
    form_is_default: bool
    form_is_battle_only: bool
    form_is_mega: bool
    form_name: str
