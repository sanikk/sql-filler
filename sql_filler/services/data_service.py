class DataService:
    # TODO naming schema:
    #  account_
    #  table_
    #  work_
    def __init__(self, postgresservice):
        self._postgresservice = postgresservice

    def connection_new(self, dbname: str, username: str) -> bool:
        if dbname and username and self._postgresservice.first_connection(dbname, username):
            return True
        return False

    def connection_close(self):
        self._postgresservice.disconnect()

    def connection_get_status(self):
        return self._postgresservice.is_connected()

    def connection_get_login_info(self):
        return self._postgresservice.get_connection_credentials()

    def inserttab_fill(self, table_number: int):
        if table_number is not None and isinstance(table_number, int):
            response = self._postgresservice.get_insert_tab_from_table(table_number=table_number)
            if response:
                return [self._pretty_insert_tab_result(*result) for result in response]
        return None

    def get_table_names(self):
        return self._postgresservice.get_table_names()

    def _pretty_insert_tab_result(self, table_name, table_id, column_name, ordinal_position, column_default, is_nullable,
                                  data_type, generation_expression, is_updatable, character_maximum_length):
        """
        Makes an object out of insert tab result.
        Parameters are spelled out for easy pasting.

        """
        return {
            'table_name': table_name,
            'table_id': table_id,
            'column_name': column_name,
            'ordinal_position': ordinal_position,
            'column_default': column_default,
            'is_nullable': is_nullable,
            'data_type': data_type,
            'generation_expression': generation_expression,
            'is_updatable': is_updatable,
            'character_maximum_length': character_maximum_length
        }

    def generate_insert_statements(self, table_number, amount, base_strings):
        # TODO remove column names, they are for dev purposes. we can use integers.
        #  10 different allowed characters is about right.
        return self._postgresservice.generate_single_insert(table_number=table_number, amount=amount,
                                                            base_strings=base_strings)


        # for ordinal_position, value in values:
            # this if does nothing now. i'm thinking of adding preprocessing here.
            # if ',.' in value:
             #    print(f"{value} contains ',.'")
            # else:
                # pass

        # TODO add foreign key support, so multiple inserts are possible in one generate request. we need right insert
        #  order and stuff


    def _process_input_string(self, input_string):
        pass

    def insert_generated_values(self):
        self._postgresservice.insert_generated_values()

    def discard_generated_values(self):
        self._postgresservice.discard_generated_values()

    def get_tab1_info(self):
        return self._postgresservice.get_information_schema_columns()

    def get_tab2_info(self):
        return self._postgresservice.get_tab2_info()
