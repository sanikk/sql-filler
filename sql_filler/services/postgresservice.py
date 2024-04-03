from sql_filler.db_module import test_connection


class PostgresService:

    def __init__(self):
        self.__dbname = None
        self.__username = None

    def __connect(self, dbname: str, username: str):
        self.__dbname = dbname
        self.__username = username

    def __disconnect(self):
        self.__dbname = None
        self.__username = None

    def try_connection(self, dbname: str, username: str) -> bool:
        if test_connection(dbname, username):
            self.__connect(dbname, username)
            return True
        return False

    def is_connected(self):
        return self.__dbname is not None and self.__username is not None

    def get_connection(self):
        return self.__dbname, self.__username
