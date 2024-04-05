from psycopg2 import connect, OperationalError
from dotenv import load_dotenv


load_dotenv()


def stupid_connection_string_checker(input_string: str):
    """
    Checks if the input_string has only letters and digits and underscores.
    :param input_string:
    :return:
    """
    if not input_string:
        return False
    for character in input_string:
        # These should be alphabets, digits or underscores
        if character.isdigit() or character.isalpha() or character == '_':
            continue
        return False
    return True


def get_connection(dbname, username):
    if stupid_connection_string_checker(dbname) or stupid_connection_string_checker(username):
        return None
    try:
        conn = connect(f"dbname={dbname} user={username}")
    except OperationalError:
        # TODO log this
        print(f"Could not connect to {username}@{dbname} (dbmodule.py:get_connection)")
        return None
    return conn
