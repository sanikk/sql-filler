from tkinter import Label, Entry, Button, Frame, NSEW, EW
from sql_filler.ui.utils import get_container
from sql_filler.services.postgresservice import test_connection


class AccountFrame(Frame):
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.connection_tab_position = {'row': 1, 'column': 1}
        self.unconnected = self.unconnected_tab()
        self.connected = None
        self.unconnected.grid(self.connection_tab_position, sticky=EW)

    def connect(self):
        self.connected = self.connected_tab(master=self)
        self.connected.grid(self.connection_tab_position, sticky=EW)
        self.unconnected.grid_forget()

    def disconnect(self):
        self.connected.destroy()
        self.unconnected.grid(**self.connection_tab_position, sticky=EW)

    def unconnected_tab(self, master=None) -> Frame:
        container = self.get_tab()
        Label(master=container, text="Username").grid(row=1, column=0)
        database_username_entry = Entry(master=container)
        database_username_entry.grid(row=2, column=0)

        Label(master=container, text="Database name").grid(row=3, column=0)
        database_name_entry = Entry(master=container)
        database_name_entry.grid(row=4, column=0)

        def connect():
            new_dbname = database_name_entry.get()
            new_username = database_username_entry.get()
            if test_connection(dbname=new_dbname, username=new_username):
                self.connect()

        Button(master=container, text="Connect", command=connect).grid(row=1, column=1, rowspan=4, sticky=EW)
        return container

    def connected_tab(self, master=None) -> Frame:
        container = self.get_tab(text='Connected to')
        Label(master=container, text=f'').grid(row=1, column=0, sticky=EW)

        def disconnect():
            self.disconnect()

        Button(master=container, text="Disconnect", command=disconnect).grid(row=2, column=0, sticky=EW)
        return container

    def get_tab(self, **kwargs):
        container = get_container(master=self, width=400, height=300, **kwargs)
        container.grid(**self.connection_tab_position, sticky=EW)
        return container
