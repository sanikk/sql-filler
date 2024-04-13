class DataService:
    def __init__(self, postgresservice):
        self._postgresservice = postgresservice

    def connect(self, dbname: str, username: str) -> bool:
        if dbname and username and self._postgresservice.first_connection(dbname, username):
            return True
        return False

    def disconnect(self):
        self._postgresservice.disconnect()

    def is_connected(self):
        return self._postgresservice.is_connected()

    def get_connection_credentials(self):
        return self._postgresservice.get_connection_credentials()

    def get_table_names(self):
        return self._postgresservice.get_table_names()

    def get_insert_tab(self):
        response = self._postgresservice.get_insert_tab_from_table()
        if response:
            return [self._pretty_insert_tab_result(*result) for result in response]
        return None

    def _pretty_insert_tab_result(self, table_name, column_name, ordinal_position, column_default, is_nullable,
                                  data_type, generation_expression, is_updatable, character_maximum_length):
        """
        Makes an object out of insert tab result.
        Parameters are spelled out for easy pasting.

        :param table_name:
        :param column_name:
        :param ordinal_position:
        :param column_default:
        :param is_nullable:
        :param data_type:
        :param generation_expression:
        :param is_updatable:
        :param character_maximum_length:
        :return:
        """
        return {
            'table_name': table_name,
            'column_name': column_name,
            'ordinal_position': ordinal_position,
            'column_default': column_default,
            'is_nullable': is_nullable,
            'data_type': data_type,
            'generation_expression': generation_expression,
            'is_updatable': is_updatable,
            'character_maximum_length': character_maximum_length
        }

    def get_tab1_info(self):
        return self._postgresservice.get_information_schema_columns()

    def get_tab2_info(self):
        return self._postgresservice.get_tab2_info()
