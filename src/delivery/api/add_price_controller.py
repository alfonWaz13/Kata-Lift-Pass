from flask import request

from src.use_cases.add_price_command_handler import (
    AddPriceCommandHandler,
    AddPriceCommand,
)


class AddPriceController:
    def __init__(self, command_handler: AddPriceCommandHandler) -> None:
        self.command_handler = command_handler

    def add_price(self) -> dict:
        lift_pass_cost = request.args["cost"]
        lift_pass_type = request.args["type"]

        command = AddPriceCommand(
            lift_pass_type=lift_pass_type, lift_pass_cost=float(lift_pass_cost)
        )

        return self.command_handler.execute(command=command)
