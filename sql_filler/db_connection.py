from psycopg2 import connect, OperationalError
from sqlalchemy import text
from dotenv import load_dotenv
from os import getenv


load_dotenv()


def stupid_mock_checker(input:str):
    for merkki in input:
        if merkki.isdigit() and
            merkki.isalpha() or
            merkki == '_':
            return True
    return False

def get_connection(dbname, username):
    username = text
    try:
        # TODO sanitize this ASAP!
        conn = connect(f"dbname={dbname} user={username}")
    except OperationalError:
        # TODO log this
        print(f"Could not connect to {username}@{dbname} (dbmodule.py:get_connection)")
        return None
    return conn
