from tkinter import Listbox, Scrollbar

from sql_filler.ui.utils import get_container


class TableFrame:
    def __init__(self, master=None):
        self.frame = get_container(master=master)
        self.lb = Listbox(self.frame, height=12, width=30)
        Scrollbar(self.frame, command=self.lb.yview).grid(row=0, column=1, sticky='W')
        self.lb.grid(row=0, column=0)
