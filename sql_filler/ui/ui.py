from tkinter import Tk, StringVar
from sql_filler.ui.accountFrame import get_account_frame
from sql_filler.ui.tableFrame import get_table_frame
from sql_filler.ui.mainFrame import get_main_frame
from sql_filler.ui.utils import get_main_label


class UI(Tk):
    def __init__(self, master=None, pos=None):
        Tk.__init__(self, master)
        self.__postgresservice = pos

        self.geometry('800x600')
        self.title('SQL Filler')

        self.dbname = StringVar(self)
        self.username = StringVar(self)

        self._main_label = get_main_label(self)
        self._account_frame = get_account_frame(master=self)
        self._table_frame = get_table_frame(master=self, dbnamevar=self.dbname, usernamevar=self.username)
        self._work_frame = get_main_frame(master=self)

        self.layout()

    def layout(self):
        self._main_label.grid(row=0, column=0, columnspan=2)
        self._account_frame.grid(row=1, column=0)
        self._table_frame.grid(row=2, column=0)
        self._work_frame.grid(row=1, column=1, rowspan=2)
        self.columnconfigure(index=0, weight=0, uniform='left', minsize=200)
        self.columnconfigure(index=1, weight=1, uniform='right', minsize=200)
        self.rowconfigure(0, weight=0, minsize=100)
        self.rowconfigure(index=2, weight=1, minsize=200)
        self.rowconfigure(index=3, weight=5, minsize=300)

    def connect(self, username, dbname):
        self.dbname.set(dbname)
        self.username.set(username)

    def disconnect(self):
        self.dbname.set('')
        self.username.set('')

    def try_connection(self, username, dbname):
        print(f"AppFrame/try_connection {self.master=}, {self.winfo_parent()=}")
        # result = self.master.try_connection(username, dbname)
        return False
