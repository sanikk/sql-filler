class DataService:
    """
    Not sure this layer will be needed. Just passes signals from ui to postgresservice.

    UI interfaces with this.
    """
    def __init__(self, postgresservice):
        self._postgresservice = postgresservice

    def try_to_set_connection_info(self, dbname: str, username: str) -> bool:
        if dbname and username and self._postgresservice.test_connection(dbname, username):
            return True
        return False

    def is_connected(self):
        return self._postgresservice.is_connected()

    def get_connection_credentials(self):
        return self._postgresservice.get_connection_credentials()

    def get_tab1_info(self):
        return self._postgresservice.get_tab1_info()

    def get_tab2_info(self):
        return self._postgresservice.get_tab2_info()
