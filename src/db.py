from typing import Dict

import pymysql.cursors
from pymysql import Connection


def create_lift_pass_db_connection(connection_options: Dict[str, str]) -> Connection:
    try:
        connection = try_to_connect_with_pymysql(connection_options)
        return connection
    except Exception as ex:
        print(f"unable to connect to db with {ex}")


def try_to_connect_with_pymysql(connection_options: Dict[str, str]) -> Connection:
    class PyMySQLCursorWrapper(pymysql.cursors.Cursor):
        """
        The pymysql.cursors.Cursor class very nearly works the same as the odbc equivalent. Unfortunately it doesn't
        understand the '?' in a SQL statement as an argument placeholder, and instead uses '%s'. This wrapper fixes that.
        """

        def mogrify(self, query: str, args: object = ...) -> str:
            query = query.replace("?", "%s")
            return str(super().mogrify(query, args))

    return pymysql.connect(
        host=connection_options["host"],
        user=connection_options["user"],
        password=connection_options["password"],
        database=connection_options["database"],
        cursorclass=PyMySQLCursorWrapper,
    )
