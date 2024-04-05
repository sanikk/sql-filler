from tkinter import Label, Entry, Button, Frame, EW
from sql_filler.ui.utils import get_container
from sql_filler.services.postgresservice import test_connection


class AccountFrame(Frame):
    def __init__(self, master=None, data_service=None):
        """ tän master on Ui(Tk)"""
        Frame.__init__(self)
        # inject data service here?
        self._data_service = data_service
        self._connection_tab_position_params = {'row': 1, 'column': 1, 'sticky': 'EW'}
        self._unconnected_tab = self.unconnected_tab()
        self._unconnected_tab.grid(self._connection_tab_position_params)
        self._connected_tab = None

    def connect(self):
        self._connected_tab = self.connected_tab(master=self)
        self._unconnected_tab.grid_forget()
        self._connected_tab.grid(self._connection_tab_position_params)

    def disconnect(self):
        self._connected_tab.destroy()
        self._unconnected_tab.grid(self._connection_tab_position_params)

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
            if self._data_service.try_to_set_connection_info(dbname=new_dbname, username=new_username):
                self.connect()

        Button(master=container, text="Connect", command=connect).grid(row=1, column=1, rowspan=4, sticky=EW)
        return container

    def connected_tab(self, master=None) -> Frame:
        container = self.get_tab(text='Connected to')
        dbname, username = self._data_service.get_connection_credentials()
        Label(master=container, text=f'{username}@{dbname}').grid(row=1, column=0, sticky=EW)

        def disconnect():
            self.disconnect()

        Button(master=container, text="Disconnect", command=disconnect).grid(row=2, column=0, sticky=EW)
        return container

    def get_tab(self, **kwargs):
        container = get_container(master=self, width=400, height=300, **kwargs)
        container.grid(self._connection_tab_position_params, sticky=EW)
        return container
