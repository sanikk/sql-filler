from tkinter import Label, Entry, Button, Frame, EW
from sql_filler.ui.utils import get_container


class AccountFrame:
    def __init__(self, master=None, data_service=None, table=None):
        self.frame = get_container(master=master)
        self._connection_tab_position_params = {'row': 1, 'column': 1, 'sticky': 'EW'}

        self._dbname_entry_box = None
        self._username_entry_box = None

        self._unconnected_tab = self.unconnected_tab()
        self._unconnected_tab.grid(self._connection_tab_position_params)
        self._connected_tab = None

        self._data_service = data_service
        self._table = table

    def connect(self):
        dbname, username = self.get_entry_values()
        if dbname and username and self._data_service.account_new(dbname, username):
            self._connected_tab = self.connected_tab()
            self._unconnected_tab.grid_forget()
            self._connected_tab.grid(self._connection_tab_position_params)

            self._table.update_tables()

    def disconnect(self):
        self._data_service.account_close()
        self._connected_tab.destroy()
        self._unconnected_tab.grid(self._connection_tab_position_params)

        self._table.update_tables()

    def unconnected_tab(self, master=None) -> Frame:
        container = self.get_tab()

        Label(master=container, text="Username").grid(row=1, column=0)
        self._username_entry_box = Entry(master=container)
        self._username_entry_box.grid(row=2, column=0)

        Label(master=container, text="Database name").grid(row=3, column=0)
        self._dbname_entry_box = Entry(master=container)
        self._dbname_entry_box.grid(row=4, column=0)

        Button(master=container, text="Connect", command=self.connect).grid(row=1, column=1, rowspan=4, sticky=EW)

        return container

    def connected_tab(self, master=None) -> Frame:
        container = self.get_tab(text='Connected to')

        dbname, username = self._data_service.account_get_login_info()
        Label(master=container, text=f'{username}@{dbname}').grid(row=1, column=0, sticky=EW)

        Button(master=container, text="Disconnect", command=self.disconnect).grid(row=2, column=0, sticky=EW)

        return container

    def get_tab(self, **kwargs):
        container = get_container(master=self.frame)
        container.grid(self._connection_tab_position_params, sticky=EW)
        return container

    def grid(self, row, column, sticky):
        """
        Passthrough method for ui->self.frame
        :param row:
        :param column:
        :param sticky:
        :return:
        """
        self.frame.grid(row=row, column=column, sticky=sticky)

    def get_entry_values(self):
        if self._dbname_entry_box and self._username_entry_box:
            return self._dbname_entry_box.get(), self._username_entry_box.get()
        return None, None
