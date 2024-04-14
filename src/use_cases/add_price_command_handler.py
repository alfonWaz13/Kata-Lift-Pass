from dataclasses import dataclass


@dataclass
class AddPriceCommand:
    lift_pass_type: str
    cost: float
