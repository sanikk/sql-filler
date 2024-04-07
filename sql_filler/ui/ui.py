from tkinter import Tk, EW

from sql_filler.ui.accountFrame import AccountFrame
from sql_filler.ui.tableFrame import TableFrame
from sql_filler.ui.mainFrame import get_main_frame
from sql_filler.ui.utils import get_main_label


class UI(Tk):
    def __init__(self, master=None, data_service=None):
        Tk.__init__(self, master)

        self.geometry('800x600')
        self.title('SQL Filler')

        self._main_label = get_main_label(master=self)
        self._account = AccountFrame(master=self, data_service=data_service)
        self._table = TableFrame(master=self)
        self._work = get_main_frame(master=self)

        self.layout()

    def layout(self):
        self._main_label.grid(row=0, column=0, columnspan=2)
        self._account.frame.grid(row=1, column=0, sticky=EW)
        self._table.frame.grid(row=2, column=0)
        self._work.grid(row=1, column=1, rowspan=2)
        self.columnconfigure(index=0, weight=1, uniform='left', minsize=200)
        self.columnconfigure(index=1, weight=10, uniform='right', minsize=200)
        self.rowconfigure(0, weight=0, minsize=100)
        self.rowconfigure(index=2, weight=1, minsize=200)
        self.rowconfigure(index=3, weight=5, minsize=300)
