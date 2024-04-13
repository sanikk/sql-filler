import tkinter
from tkinter.ttk import Frame, Label, Entry, Button, Treeview, LabelFrame
from sql_filler.ui.utils import get_container

import tkinter.ttk as ttk


class InsertTab:
    def __init__(self, master=None, ui=None):
        self.frame = get_container(master=master, width=800, height=550)
        ttk.Button(master=self.frame, text="Insert to DB", command=self.insert_values).grid(row=1, column=0)
        self.box_container = ttk.LabelFrame(master=self.frame, text="Table Columns", width=750, height=1200)
        self.box_container.grid(row=2, column=0)

        self._ui = ui
        self._group = []

    def populate_insert_columns_tab(self):
        column_list = self._ui.get_insert_tab()
        for column_data in column_list:
            new_box = SingleColumnBox(master=self.box_container, column_data=column_data)
            self._group.append(new_box)
            new_box.grid(row=column_data["ordinal_position"], column=0)

    def switch_selected_table(self):
        for box in self._group:
            box.hide()
        # bindaa tämä siihen selectediin tauluissa
        self.populate_insert_columns_tab()

    def insert_values(self):
        pass

    def show_generated_values(self, master=None, column_names=None, data=None):
        pass
        # tree = Treeview(master=self, columns=column_names, displaycolumns='#all', selectmode='extended', height=20)

    def get_frame(self):
        return self.frame

    def make_single_column_box(self, column_data):
        """
        Makes an expandable button+entry box from a column row.

        :param column_data:
        table_name, table_id, column_name, ordinal_position, column_default, is_nullable, data_type,
        generation_expression, is_updatable, character_maximum_length

        :return:
        """
        container = Frame(master=self.box_container)

        def expand_this():
            pass
        ttk.Button(container, text=column_data["column_name"], command=expand_this).grid(row=0, column=0)
        ttk.Entry(container, width=20).grid(row=0, column=1)

        return container


class SingleColumnBox:
    # not worth a class.
    # we'll just do dynamic buttons and shit
    def __init__(self, master=None, column_data=None):
        self.frame = Frame(master=master)

        def expand_this():
            pass
        self.button = ttk.Button(self.frame, text=column_data["column_name"], command=self.expand)
        self.expanded_button = self.get_expanded_button(column_data=column_data)
        self.value = ttk.Entry(self.frame, width=20)
        self.button.grid(row=0, column=0)
        self.value.grid(row=0, column=1)

    def grid(self, row, column):
        self.frame.grid(row=row, column=column)

    def get_value(self):
        return self.value.get()

    def get_expanded_button(self, column_data=None):
        container = Frame(self.frame)
        txt = ''
        for key in column_data.keys():
            txt += f"{key}: {column_data[key]}\n"
        ttk.Button(master=container, text=txt, command=self.shrink).grid(row=0, column=0)
        return container

    def expand(self):
        self.button.grid_forget()
        self.expanded_button.grid(row=0, column=0)

    def shrink(self):
        self.expanded_button.grid_forget()
        self.button.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()
