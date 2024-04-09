class DataService:
    """
    Not sure this layer will be needed. Just passes signals from ui to postgresservice.

    UI frames interface with this now?
    """
    def __init__(self, postgresservice):
        self._postgresservice = postgresservice

    def try_first_connection(self, dbname: str, username: str) -> bool:
        if dbname and username and self._postgresservice.first_connection(dbname, username):
            return True
        return False

    def is_connected(self):
        return self._postgresservice.is_connected()

    def get_connection_credentials(self):
        return self._postgresservice.get_connection_credentials()

    def get_table_names(self):
        return self._postgresservice.get_table_names()

    def get_tab1_info(self):
        return self._postgresservice.get_information_schema_columns()

    def get_tab2_info(self):
        return self._postgresservice.get_tab2_info()
