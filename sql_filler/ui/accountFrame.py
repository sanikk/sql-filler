from tkinter import Label, Entry, Button
from sql_filler.ui.utils import get_container
from sql_filler.services.postgresservice import PostgresService, test_connection


def get_account_frame(master=None):
    # TODO fix this file next, 2 tabs(connect, unconnected), switcher
    account_container = get_container(text="SQL connection", master=master)

    Label(master=account_container, text="Username").grid(row=1, column=0)
    database_username_entry = Entry(master=account_container)
    database_username_entry.grid(row=2, column=0)

    Label(master=account_container, text="Database name").grid(row=3, column=0)
    database_name_entry = Entry(master=account_container)
    database_name_entry.grid(row=4, column=0)

    def connect():
        new_dbname = database_name_entry.get()
        new_username = database_username_entry.get()
        if test_connection(new_dbname):
            master.connect(new_username, new_dbname)
            master.set_account_frame()
    Button(master=account_container, text="Connect", command=connect).grid(row=5, column=0)

    account_container.grid(row=1, column=0, sticky="nsew")
    return account_container


