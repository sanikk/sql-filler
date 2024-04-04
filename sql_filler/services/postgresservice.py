from sql_filler.db_module import test_connection
from sql_filler.db_connection import get_connection
from sqlalchemy import text


class PostgresService:

    def __init__(self):
        self._dbname = None
        self._username = None

    def _connect(self, dbname: str, username: str):
        self._dbname = dbname
        self._username = username

    def _disconnect(self):
        self._dbname = None
        self._username = None

    def try_connection(self, dbname: str, username: str) -> bool:
        if test_connection(dbname, username):
            self._connect(dbname, username)
            return True
        return False

    def is_connected(self):
        """
        Checks if dbname and username class variables are set to anything.

        :return: True if dbname and username exist
        """
        return self._dbname is not None and self._username is not None

    def get_connection_credentials(self):
        return self._dbname, self._username

    def get_information_schema_columns(self):
        sql = 'SELECT * FROM information_schema.columns WHERE table_schema=\'public\''
        with get_connection() as conn:
            with conn.cursor() as cur:
                return cur.execute(text(sql)).fetchall()
