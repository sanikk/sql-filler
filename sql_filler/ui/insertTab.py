from tkinter.ttk import Frame, Label, Entry, Button, Treeview, LabelFrame
from sql_filler.ui.utils import get_container
import tkinter as tk
import tkinter.ttk as ttk


class InsertTab:
    # NEW TODO FIXME luonnostelmaa
    def __init__(self, master=None, ui=None):
        self.frame = container = get_container(master=master, width=800, height=550)
        Button(master=self.frame, text="Insert to DB", command=self.insert_values).grid(row=1, column=0)
        self.box_container = LabelFrame(master=self.frame, text="Table Columns", width=750, height=1200)
        self.box_container.grid(row=2, column=0)

        self._ui = ui
        self._group = []
        self._values = None

    def populate_insert_columns_tab(self):
        column_list = self._ui.get_insert_tab()
        for column_data in column_list:
            new_box = self.make_single_column_box(column_data)
            # new_label = Label(master=self.box_container, text=column_data["column_name"])
            # self._group.append(new_label)
            new_box.grid(row=column_data["ordinal_position"], column=0)

    def switch_selected_table(self):
        for box in self._group:
            # kato mallia accountista
            box.grid_forget()
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

