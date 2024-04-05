from psycopg2 import connect, OperationalError


def _stupid_connection_string_checker(input_string: str):
    """Checks if the input_string has only letters and digits and underscores."""
    # TODO fix this!
    if not input_string:
        return False
    for character in input_string:
        # These should be alphabets, digits or underscores
        if character.isdigit() or character.isalpha() or character == '_':
            continue
        return False
    return True


def _check_connection_info(dbname, username):
    if not _stupid_connection_string_checker(dbname):
        return False
    if not _stupid_connection_string_checker(username):
        return False
    return True


def get_connection(dbname, username):
    """
    Return connection with params dbname and username.

    Validation of connection string happens here!

    :param dbname:
    :param username:
    :return: connection
             None
    """
    if not _check_connection_info(dbname, username):
        return None
    try:
        conn = connect(f"dbname={dbname} user={username}")
    except OperationalError:
        # TODO log this
        print(f"Could not connect to {username}@{dbname} (dbmodule.py:get_connection)")
        return None
    return conn


def test_connection(dbname=None, username=None):
    try:
        conn = get_connection(dbname=dbname, username=username)
        if conn:
            conn.close()
            return True
    except OperationalError:
        pass
    return False
