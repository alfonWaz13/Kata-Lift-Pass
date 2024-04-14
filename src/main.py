from typing import Dict

from flask import Flask

from src.db import create_lift_pass_db_connection
from src.delivery.api.add_price_controller import AddPriceController
from src.delivery.api.get_price_controller import GetPriceController
from src.use_cases.add_price_command_handler import AddPriceCommandHandler

app = Flask("lift-pass-pricing")

connection_options = {
    "host": "mariadb",
    "user": "root",
    "database": "lift_pass",
    "password": "mysql",
}


connection = create_lift_pass_db_connection(connection_options)
add_price_command_handler = AddPriceCommandHandler(connection=connection)
add_price_controller = AddPriceController(command_handler=add_price_command_handler)
get_price_controller = GetPriceController(connection=connection)


@app.route("/prices", methods=["PUT"])
def add_price() -> Dict[str, int]:
    return add_price_controller.add_price()


@app.route("/prices", methods=["GET"])
def get_price() -> Dict[str, int]:
    return get_price_controller.get_price()
