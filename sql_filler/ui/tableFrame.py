from tkinter import Listbox, Frame, END, Scrollbar
from sql_filler.ui.utils import get_container
from sql_filler.db_module import list_tables


def get_table_frame(master=None):
    container = get_container(master=master)

    lb = Listbox(container, height=12, width=30)
    Scrollbar(container, command=lb.yview).grid(row=0, column=1, sticky='W')
    # if master.is_connected():
    # tablenames = list_tables()
    # lb.insert(END, *tablenames)
    lb.grid(row=0, column=0)

    return container
