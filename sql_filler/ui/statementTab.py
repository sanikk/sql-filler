import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import Button, Label
from sql_filler.ui.utils import get_container, make_scrollable_frame


class StatementTab:
    def __init__(self, master=None, data_service=None):
        self._data_service = data_service
        self.frame = get_container(text="Statements tab", master=master)
        self.frame.bind('<Map>', self.refresh_statements)

        button_frame = ttk.LabelFrame(master=self.frame)
        button_frame.grid(row=1, column=0)
        ttk.Button(master=button_frame, command=self.edit_list_item, text='edit').grid(row=0, column=0)
        ttk.Button(master=button_frame, command=self.copy_list_item, text='copy').grid(row=0, column=1)
        ttk.Button(master=button_frame, command=self.del_list_item, text='delete').grid(row=0, column=2)
        ttk.Button(master=button_frame, command=self.execute_list_item, text='execute').grid(row=0, column=3)

        # big/small vars
        scrollable, box_container = make_scrollable_frame(master=self.frame, row=2, column=0)
        self.scrollable = scrollable
        self.box_container = box_container

    def refresh_statements(self, event):
        self._clear_statements_view()
        self._populate_statements_tab()

    def _clear_statements_view(self):
        for box in self.box_container.grid_slaves():
            box.destroy()

    def edit_list_item(self):
        pass

    def copy_list_item(self):
        pass

    def del_list_item(self):
        pass

    def execute_list_item(self):
        pass

    def get_frame(self):
        return self.frame

    def grid(self):
        self.frame.grid()

    def _show_generated_values(self, master=None, column_names=None, data=None):
        pass
        # saf

    def _populate_statements_tab(self):
        statements_list = self._data_service.statementtab_fill()
        for i, (query, values) in enumerate(statements_list):
            self._make_single_row(master=self.box_container, row=i+1, query=query, values=values)
        self._reset_scrollregion()

    def _make_single_row(self, master=None, row=None, query=None, values=None):
        statement_label = Label(master=master, text=query)
        statement_label.grid(row=row, column=0)
        value_label = Label(master=master, text=values)
        value_label.grid(row=row, column=1)
        #small_button_params = {'row': row, 'column': 1, 'sticky': 'EW'}
        #big_button_params = {'row': row, 'column': 1, 'columnspan': 2, 'sticky': 'W'}
        #statement_label_label_params = {'row': row, 'column': 1}

        # small button/datatype label area (replaces big button)
        #def expand():
        #    smallbutton.grid_forget()
        #    bigbutton.grid(big_button_params)
        #    self._reset_scrollregion()
        #smallbutton = Button(master=master, text=values, command=expand)
        #smallbutton.grid(small_button_params)

        #def shrink():
        #    bigbutton.grid_forget()
        #    smallbutton.grid(small_button_params)
        #    self._reset_scrollregion()
        #big_button_text = '\n'.join([f"{key}: {values[key]}" for key in values.keys()])
        #bigbutton = Button(master=master, text=big_button_text, command=shrink)

    def _reset_scrollregion(self):
        self.box_container.update()
        self.frame.update()
        self.scrollable.config(scrollregion=self.scrollable.bbox('all'))

