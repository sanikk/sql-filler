from sql_filler.db_connection import get_connection, test_connection
from psycopg import sql
import re


class PostgresService:
    def __init__(self):
        self._dbname = None
        self._username = None

        # use index with data_service -> ui
        self._runtime_table_list = []
        self._generated_inserts = []

    # public methods
    # Connection
    def first_connection(self, dbname=None, username=None):
        if self._test_connection(dbname=dbname, username=username):
            return True
        return False

    def disconnect(self):
        self._dbname = None
        self._username = None

    def is_connected(self):
        return self._dbname is not None and self._username is not None

    def get_connection_credentials(self):
        return self._dbname, self._username

    # tableFrame
    def get_table_names(self):
        if self._username and self._clean_sql_string(self._username):
            query = sql.SQL("SELECT tablename from pg_catalog.pg_tables WHERE tableowner=%s")
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query, [self._username])
                    # TODO check return?
                    returnable = [item for tupl in cur.fetchall() for item in tupl]
                    self._runtime_table_list = returnable
                    return returnable

    # Tab methods
    def get_information_schema_columns(self):
        query = sql.SQL('SELECT * FROM information_schema.columns WHERE table_schema=\'public\'')
        # just a hardcoded query, not much to check
        if True:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query, [self._username])
                    res = cur.fetchall()
                    return res

    def get_insert_tab_from_table(self, table_number: int):
        # TODO these are just sketches for checks
        if table_number is None or not isinstance(table_number, int):
            return
        if table_number < 0 or table_number >= len(self._runtime_table_list):
            return
        table_name = self._runtime_table_list[table_number]
        if not table_name or not self._clean_sql_string(table_name):
            return
        query = sql.SQL("""
        SELECT 
        table_name, CAST(table_name::regclass AS oid) as table_id, column_name, ordinal_position, column_default, 
        is_nullable, data_type, generation_expression, is_updatable, character_maximum_length 
        FROM information_schema.columns 
        WHERE table_schema=\'public\' AND table_name=%s 
        ORDER BY ordinal_position ASC
        """)

        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, [table_name])
                return cur.fetchall()

    def generate_single_insert(self, table_number, amount, base_strings):
        strings = [f"{base_strings}{i}" for i in range(1, amount + 1)]
        table_name = sql.Identifier(self._runtime_table_list[table_number])
        placeholders = sql.SQL(", ").join(sql.Placeholder() * len(base_strings))
        query = sql.SQL("INSERT INTO {table_name} VALUES ( {placeholders} )")

        fquery = query.format(
            table_name=table_name,
            placeholders=placeholders
        )
        returnable = fquery.as_string(self._get_connection())
        return returnable

    def insert_generated_data(self):
        sql = """
            RETURNING id
        """
        pass

    def get_tab2_info(self):
        return ''

    # internal methods

    def _test_connection(self, dbname=None, username=None):
        if test_connection(dbname=dbname, username=username):
            self._dbname = dbname
            self._username = username
            return True
        return False

    def _get_connection(self):
        if self._dbname and self._username:
            return get_connection(dbname=self._dbname, username=self._username)
        return None

    def _clean_sql_string(self, string: str):
        # allowed characters a-z, A-Z, 0-9, _, :, (, ), ., %
        # a-z0-9_ allowed in table names
        # you need : for casting, () for obv. reasons
        # /s tabs, newline
        exp = r'^[a-zA-Z0-9_():\.\=\%\s]+$'
        return re.match(exp, string)
