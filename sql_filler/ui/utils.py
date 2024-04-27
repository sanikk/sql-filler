from tkinter import Canvas
from tkinter.ttk import Scrollbar, Label, Frame


def get_container(master=None, text=None, columnspan=1, rowspan=1):
    container = Frame(master=master, style='Container.TFrame')
    # highlightthickness=5, highlightbackground='yellow')
    if text:
        Label(master=container, text=text, font='Calibri 22').grid(row=0, column=0, columnspan=columnspan,
                                                                   rowspan=rowspan)
    return container


def get_main_label(master=None):
    main_label = Label(master=master, text='SQL Filler', font='Calibri 24', foreground='purple')
    return main_label


def make_scrollable_frame(master=None, row=None, column=None, rowspan=1, columnspan=1):
    """
    Makes a scrollable frame. Self contained function, just needs the parent window as param.

    :return: scrollable(tk.Canvas), box_container(Frame)
    """
    scrollbar = Scrollbar(master=master)
    scrollable = Canvas(master=master, yscrollcommand=scrollbar.set)
    scrollbar.config(command=scrollable.yview)
    scrollable.grid(row=row, column=column, sticky='NSEW', rowspan=rowspan, columnspan=columnspan)
    scrollbar.grid(row=row, column=column + 1, sticky='NS', rowspan=rowspan)
    scrollable.rowconfigure(1, weight=0)

    box_container = Frame(master=scrollable)

    scrollable.create_window((0, 0), window=box_container, anchor='nw')
    return scrollable, box_container

