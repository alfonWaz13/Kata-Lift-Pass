from dataclasses import dataclass

from pymysql import Connection


@dataclass
class AddPriceCommand:
    lift_pass_type: str
    lift_pass_cost: float


class AddPriceCommandHandler:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def execute(self, command: AddPriceCommand) -> dict:

        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO `base_price` (type, cost) VALUES (?, ?) "
            + "ON DUPLICATE KEY UPDATE cost = ?",
            (command.lift_pass_type, command.lift_pass_cost, command.lift_pass_cost),
        )
        return {}
