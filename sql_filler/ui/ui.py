from tkinter import Tk

from sql_filler.ui.accountFrame import AccountFrame
from sql_filler.ui.tableFrame import TableFrame
from sql_filler.ui.workFrame import WorkFrame

from sql_filler.ui.utils import get_main_label


class UI:
    def __init__(self, master=None, data_service=None):
        self.frame = Tk()
        self.frame.geometry('800x600')
        self.frame.title('SQL Filler')

        self._data_service = data_service

        self._main_label = get_main_label(master=self.frame)
        self._account = AccountFrame(master=self.frame, ui=self)
        self._table = TableFrame(master=self.frame, ui=self)
        self._work = WorkFrame(master=self.frame, ui=self)

        self._grid()
        self._layout()

    def _grid(self):
        self._main_label.grid(row=0, column=0, columnspan=2)
        self._account.grid(row=1, column=0, sticky='SEW')
        self._table.grid(row=2, column=0, sticky='NEW')
        self._work.grid(row=1, column=1, rowspan=2)

    def _layout(self):
        self.frame.columnconfigure(index=0, weight=0)
        self.frame.columnconfigure(index=1, weight=0)
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(index=1, weight=0)
        self.frame.rowconfigure(index=2, weight=0)

    def get_table_names(self):
        return self._data_service.get_table_names()

    def get_connection_credentials(self):
        return self._data_service.get_connection_credentials()

    def connect(self):
        dbname, username = self._account.get_entry_values()
        if dbname and username and self._data_service.connect(dbname, username):
            self._account.connect()
            self._table.update_tables()

    def disconnect(self):
        self._data_service.disconnect()
        self._account.disconnect()
        self._table.update_tables()

    def insert_values(self):
        values = []
        self._data_service.insert_values(values)

    def switch_selected_table(self):
        self._work.switch_selected_table()

    def get_insert_tab(self):
        table_number = self._table.get_selected_table()
        return self._data_service.get_insert_tab(table_number=table_number)

    # passthrough function for main.py so far
    def mainloop(self):
        self.frame.mainloop()
