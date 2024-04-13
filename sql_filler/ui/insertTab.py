from tkinter.ttk import Frame, Label, Entry, Button, Treeview, LabelFrame
from sql_filler.ui.utils import get_container
import tkinter as tk
import tkinter.ttk as ttk


class InsertTab:
    def __init__(self, master=None, ui=None):
        self.frame = container = get_container(master=master, width=800, height=550)
        Button(master=self.frame, text="Insert to DB", command=self.insert_values).grid(row=1, column=0)
        self.box_container = LabelFrame(master=self.frame, text="Table Columns", width=750, height=1200)
        self.box_container.columnconfigure(0, weight=3)
        self.box_container.columnconfigure(1, weight=1)
        self.box_container.grid(row=2, column=0)

        self._ui = ui
        self._group = []
        self._values = None

    def populate_insert_columns_tab(self):
        column_list = self._ui.get_insert_tab()
        for column_data in column_list:
            self.make_single_row(column_data=column_data)

    def switch_selected_table(self):
        for box in self._group:
            box.grid_forget()
        self.populate_insert_columns_tab()

    def insert_values(self):
        pass

    def show_generated_values(self, master=None, column_names=None, data=None):
        pass
        # tree = Treeview(master=self, columns=column_names, displaycolumns='#all', selectmode='extended', height=20)

    def get_frame(self):
        return self.frame

    def make_single_row(self, master=None, column_data=None):
        if not master:
            master = self.box_container

        def expand():
            smallbutton.grid_forget()
            bigbutton.grid(row=0, column=0)

        smallbutton = ttk.Button(master=master, text=column_data["column_name"], command=expand)
        smallbutton.grid(row=column_data["ordinal_position"], column=0)

        def shrink():
            bigbutton.grid_forget()
            smallbutton.grid(row=0, column=0)

        txt = '\n'.join([f"{key}: {column_data[key]}" for key in column_data.keys()])
        bigbutton = ttk.Button(master=master, text=txt, command=shrink)
        valbox = ttk.Entry(self.box_container, width=20)
        self._group.append(valbox)
        valbox.grid(row=column_data["ordinal_position"], column=1)

