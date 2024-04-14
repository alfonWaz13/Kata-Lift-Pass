from dataclasses import dataclass

from pymysql import Connection


@dataclass
class AddPriceCommand:
    lift_pass_type: str
    cost: float


class AddPriceCommandHandler:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection
