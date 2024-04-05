from tkinter import Tk, EW

from sql_filler.ui.accountFrame import AccountFrame
from sql_filler.ui.tableFrame import get_table_frame
from sql_filler.ui.mainFrame import get_main_frame
from sql_filler.ui.utils import get_main_label


class UI(Tk):
    def __init__(self, master=None, dataservice=None):
        Tk.__init__(self, master)
        self._data_service = dataservice

        self.geometry('800x600')
        self.title('SQL Filler')

        self._dbname = None
        self._username = None

        self._main_label = get_main_label(master=self)
        self._account_frame = AccountFrame(master=self)
        self._table_frame = get_table_frame(master=self)
        self._work_frame = get_main_frame(master=self)

        self.layout()

    def layout(self):
        self._main_label.grid(row=0, column=0, columnspan=2)
        self._account_frame.grid(row=1, column=0, sticky=EW)
        self._table_frame.grid(row=2, column=0)
        self._work_frame.grid(row=1, column=1, rowspan=2)
        self.columnconfigure(index=0, weight=1, uniform='left', minsize=200)
        self.columnconfigure(index=1, weight=10, uniform='right', minsize=200)
        self.rowconfigure(0, weight=0, minsize=100)
        self.rowconfigure(index=2, weight=1, minsize=200)
        self.rowconfigure(index=3, weight=5, minsize=300)

    def get_connection_info(self):
        """Return dbname and username from postgresservice"""
        return self._data_service.get_connection_credentials()

    def is_connected(self):
        """
        Check if there is a valid dbname and a valid username saved in postgresservice.

        :return: True if the service's dbname and username are set.
        """
        return self._data_service.is_connected()
