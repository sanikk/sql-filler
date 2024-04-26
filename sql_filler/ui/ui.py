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

        self._work = WorkFrame(master=self.frame, data_service=data_service)
        self._table = TableFrame(master=self.frame, data_service=data_service, work=self._work)
        self._account = AccountFrame(master=self.frame, data_service=data_service, table=self._table)

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

    # TODO maybe move most of these to dedicated services. inserttab_service, table_service, etc? with connection to
    #  postgresservice or dataservice injected at init.
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

    def generate_insert_statements(self, table_number, amount, base_strings):
        return self._data_service.generate_insert_statements(table_number=table_number, amount=amount,
                                                             base_strings=base_strings)

    def insert_generated_values(self):
        self._data_service.insert_generated_values()

    def discard_generated_values(self):
        self._data_service.discard_generated_values()
        self._work.discard_generated_values()

    def switch_selected_table(self, selected):
        self._work.switch_selected_table()

    def get_insert_tab(self):
        table_number = self._table.get_selected_table()
        return self._data_service.get_insert_tab(table_number=table_number)

    # passthrough function for main.py so far
    def mainloop(self):
        self.frame.mainloop()

    #dev
    def get_selected_table(self):
        return self._table.get_selected_table()
