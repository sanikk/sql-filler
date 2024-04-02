from tkinter import Frame, Menu, ttk, Button, NSEW, Label
from sql_filler.ui.utils import get_container


def get_main_frame(master):
    container = Frame(master=master, highlightthickness=5, highlightbackground='yellow', width=800, height=600)

    menu_bar(container).grid(row=0, column=0)
    return container


def menu_bar(master=None):
    tab_switcher = ttk.Notebook(master=master)

    example_tab1 = Frame(master=master, highlightthickness=5, highlightbackground='yellow', width=800, height=550)
    Button(master=example_tab1, text='tab1button').grid(row=1, column=0)
    example_tab2 = Frame(master=master, highlightthickness=5, highlightbackground='yellow', width=800, height=550)
    Button(master=example_tab2, text='tab2button').grid(row=1, column=0)

    tab_switcher.add(table_info_tab(master=master), text='table info')
    tab_switcher.add(insert_tab(master=master), text='insert data')
    tab_switcher.add(db_info_tab(master=master), text='db info')
    # tab_switcher.add(example_tab2, text='2')
    tab_switcher.add(settings_tab(master=master), text='settings')
    return tab_switcher


def settings_tab(master=None):
    container = get_tab_container()
    Button(master=container, text='settings button').grid(row=1, column=0)
    return container


def insert_tab(master=None):
    container = get_tab_container(master)
    return container


def table_info_tab(master=None):
    container = get_tab_container(master)
    return container


def db_info_tab(master=None):
    container = get_tab_container(master)
    return container


def get_tab_container(master=None):
    return Frame(master=master, highlightthickness=5, highlightbackground='yellow', width=800, height=550)


def selected_table_label(master=None):
    return Label(master=master, text=f'Selected table {master}')
