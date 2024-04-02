from psycopg2 import connect, OperationalError
from dotenv import load_dotenv
from os import getenv


load_dotenv()


def get_connection(dbname=None):
    if not dbname:
        dbname = getenv("SQLALCHEMY_DATABASE_URI")
    try:
        conn = connect(f"dbname={dbname}")
    except OperationalError:
        # TODO log this
        print(f"Could not connect to {dbname} (dbmodule.py:get_connection)")
        return None
    cur = conn.cursor()
    return conn, cur


def test_connection(dbname=None):
    try:
        conn = get_connection(dbname)
        if conn:
            return True
    except OperationalError:
        pass
    return False


def insert_independent(table_name, column_list, values):
    conn, cur = get_connection()

    columns_sql = ", ".join(column_list)
    sql = f"INSERT INTO %s ({','.join(column_list)}) VALUES ({','.join(['%s' for a in column_list])})"
    cur.execute(sql, (table_name, *values,))
    conn.commit()
    cur.close()
    conn.close()


def list_tables(user):
    conn, cur = get_connection()
    sql = "SELECT tablename from pg_catalog.pg_tables WHERE tableowner=%s"
    cur.execute(sql, (user,))
    return cur.fetchall()
