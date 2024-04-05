from sql_filler.db_connection import get_connection, test_connection
from sqlalchemy import text


class PostgresService:
    def __init__(self):
        self._dbname = None
        self._username = None

    # public methods
    def first_connection(self, dbname=None, username=None):
        if self._test_connection(dbname=dbname, username=username):
            return True
        return False

    def disconnect(self):
        self._dbname = None
        self._username = None

    def is_connected(self):
        return self._dbname is not None and self._username is not None

    def get_tab1_info(self):
        return self._get_information_schema_columns()

    def get_tab2_info(self):
        return self._get_information_schema_columns()

    def get_connection_credentials(self):
        return self._dbname, self._username

    # internal methods
    def _get_information_schema_columns(self):
        sql_string = 'SELECT * FROM information_schema.columns WHERE table_schema=\'public\''
        return self._execute_sql(sql_string).fetchall()

    def _test_connection(self, dbname=None, username=None):
        if test_connection(dbname=dbname, username=username):
            self._dbname = dbname
            self._username = username
            return True
        return False

    def _execute_sql(self, sql_string: str, params=None):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                return cur.execute(self._clean_sql_string(sql_string, params))

    def _clean_sql_string(self, sql_string: str, params=None):
        """Cleans sql_string with <tool>.
        Returns sqlalchemy TextClause now.
        """
        # TODO check text methods.
        return text(sql_string), params

    def _get_connection(self):
        if self._dbname and self._username:
            return get_connection(dbname=self._dbname, username=self._username)
        return None
