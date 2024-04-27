from tkinter import Canvas, Label, Frame
from tkinter.ttk import Scrollbar


def get_container(master=None, text=None, columnspan=1, rowspan=1):
    container = Frame(master=master, highlightthickness=5, highlightbackground='yellow')
    if text:
        Label(master=container, text=text, font='Calibri 22').grid(row=0, column=0, columnspan=columnspan,
                                                                   rowspan=rowspan)
    return container


def get_main_label(master=None):
    main_label = Label(master=master, text='SQL Filler', fg='purple', font='Calibri 24')
    return main_label


def make_scrollable_frame(master=None):
    """
    Makes a scrollable frame. Self contained function, just needs the parent window as param.

    :param master:
    :return: scrollable(tk.Canvas), box_container(Frame)
    """
    scrollbar = Scrollbar(master=master)
    scrollable = Canvas(master=master, yscrollcommand=scrollbar.set)
    scrollbar.config(command=scrollable.yview)
    scrollable.grid(row=2, column=0, sticky='NSEW')
    scrollbar.grid(row=2, column=1, sticky='NS')
    scrollable.rowconfigure(1, weight=0)

    box_container = Frame(master=scrollable)
    box_container.columnconfigure(0, weight=1)  # big/small button
    box_container.columnconfigure(1, weight=1)  # datatype label
    box_container.columnconfigure(2, weight=1)  # entry box

    scrollable.create_window((0, 0), window=box_container, anchor='nw')
    return scrollable, box_container

