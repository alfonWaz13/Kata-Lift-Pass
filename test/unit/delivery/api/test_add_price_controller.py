from doublex import Stub, Mimic
from expects import expect, equal

from src.delivery.api.add_price_controller import AddPriceController
from src.main import app
from src.use_cases.add_price_command_handler import (
    AddPriceCommand,
    AddPriceCommandHandler,
)


class TestAddPriceController:
    def test_add_price_response_is_what_expected(self) -> None:
        lift_pass_type = "1jour"
        lift_pass_cost = 100
        expected_response = {"type": lift_pass_type, "cost": lift_pass_cost}
        command = AddPriceCommand(
            lift_pass_type=lift_pass_type, lift_pass_cost=lift_pass_cost
        )
        with Mimic(Stub, AddPriceCommandHandler) as command_handler:
            command_handler.execute(command).returns(expected_response)
        add_price_controller = AddPriceController(command_handler)
        query_string = {"type": "1jour", "cost": "100"}

        with app.test_request_context(query_string=query_string):
            response = add_price_controller.add_price()

        expect(response).to(equal(expected_response))
