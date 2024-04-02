from tkinter import Label, Frame


def get_container(text=None, master=None, columnspan=1, rowspan=1):
    container = Frame(master=master, highlightthickness=5, highlightbackground='yellow')
    if text:
        Label(master=container, text=text, font='Calibri 22').grid(row=0, column=0, columnspan=columnspan,
                                                                   rowspan=rowspan)
    return container


def get_main_label(master=None):
    main_label = Label(master=master, text='SQL Filler', fg='purple', font='Calibri 24')
    return main_label
