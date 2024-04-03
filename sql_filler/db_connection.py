from psycopg2 import connect, OperationalError
from dotenv import load_dotenv
from os import getenv


load_dotenv()


def get_connection(dbname=None, username=None):
    if not dbname:
        dbname = getenv("SQLALCHEMY_DATABASE_URI")
    if not username:
        username = getenv("SQLALCHEMY_USERNAME")
    try:
        conn = connect(f"dbname={dbname} user={username}")
    except OperationalError:
        # TODO log this
        print(f"Could not connect to {username}@{dbname} (dbmodule.py:get_connection)")
        return None
    cur = conn.cursor()
    return conn, cur
