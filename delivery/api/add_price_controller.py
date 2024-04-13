from pymysql import Connection


class AddPriceController:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection