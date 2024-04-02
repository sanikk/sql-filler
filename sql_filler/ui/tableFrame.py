from tkinter import Listbox, Frame, END, Scrollbar
from sql_filler.ui.utils import get_container
from sql_filler.db_module import list_tables


def get_table_frame(master=None, dbnamevar=None, usernamevar=None):
    container = Frame(master=master, highlightthickness=5, highlightbackground='yellow')
    lb = Listbox(container, height=12, width=30)
    Scrollbar(container, command=lb.yview).grid(row=0, column=1, sticky='W')
    if usernamevar.get():
        # FIXME encapsulation? access to db?
        tablenames = list_tables(usernamevar.get())
        lb.insert(END, *tablenames)
    lb.grid(row=0, column=0)
    return container
