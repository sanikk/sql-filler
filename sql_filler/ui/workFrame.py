from sql_filler.ui.utils import get_container
from sql_filler.ui.insertTab import InsertTab
import tkinter as tk
from tkinter import ttk


class WorkFrame:
    def __init__(self, master=None, ui=None):
        self.frame = get_container(master=master)
        self.insert_tab = None
        self.menu = self.get_menu_bar(ui=ui)
        self.menu.grid(row=0, column=0)
        self._ui = ui

    def get_menu_bar(self, master=None, ui=None):
        if not master:
            master = self.frame
        tab_switcher = ttk.Notebook(master=master)

        tab_switcher.add(self.table_info_tab(master=master), text='table info')
        # tab_switcher.add(self.insert_tab(master=master), text='insert data')
        self.insert_tab = InsertTab(master=master, ui=ui)
        tab_switcher.add(self.insert_tab.get_frame(), text='insert data')
        tab_switcher.add(self.db_info_tab(master=master), text='db info')
        # tab_switcher.add(tab, text='text')
        tab_switcher.add(self.settings_tab(master=master), text='settings')

        # tab_switcher.add(get_container(text='size', master=master, width=800, height=550))
        return tab_switcher

    def settings_tab(self, master=None):
        container = get_container(text="Settings", master=master)
        ttk.Button(master=container, text='settings button').grid(row=1, column=0)
        return container

    def table_info_tab(self, master=None):
        container = get_container(text="Table info", master=master)
        tb = tk.Text(master=container, width=60, height=20)
        tb.grid(row=2, column=0)
        return container

    def db_info_tab(self, master=None):
        container = get_container(text="DB Info", master=master)
        return container

    def grid(self, row, column, rowspan):
        """
        Passthrough method ui->self.frame

        :param row:
        :param column:
        :param rowspan:
        :return:
        """
        self.frame.grid(row=row, column=column, rowspan=rowspan)

    def selected_table_label(self, master=None):
        return ttk.Label(master=master, text=f'Selected table {master}')

    def switch_selected_table(self):
        self.insert_tab.switch_selected_table()

    def discard_generated_values(self):
        self.insert_tab.discard_generated_values()

