from tkinter import Tk
import tkinter as tk
import tkinter.ttk as ttk

from sql_filler.ui.accountTab import AccountTab
from sql_filler.ui.insertTab import InsertTab
from sql_filler.ui.statementTab import StatementTab

from sql_filler.ui.utils import get_main_label


class UI:
    def __init__(self, master=None, data_service=None):
        self.frame = Tk()
        self.frame.geometry('800x600')
        self.frame.title('SQL Filler')

        self._data_service = data_service

        self._main_label = get_main_label(master=self.frame)
        self._main_label.grid(row=0, column=0, columnspan=1)

        self.menu = self.get_menu_bar(master=self.frame, data_service=data_service)
        self.menu.grid(row=1, column=0)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.insert_tab = None
        self.account_tab = None
        self.statement_tab = None

        # self._style()
        # self._grid()
        # self._layout()

    def get_menu_bar(self, master=None, data_service=None):

        tab_switcher = ttk.Notebook(master=master)

        self.account_tab = AccountTab(master=master, data_service=data_service, ui=self)
        tab_switcher.add(self.account_tab.get_frame(), text='account tab')

        self.insert_tab = InsertTab(master=master, data_service=data_service)
        tab_switcher.add(self.insert_tab.get_frame(), text='column data tab', state='disabled')

        self.statement_tab = StatementTab(master=master, data_service=data_service)
        tab_switcher.add(self.statement_tab.get_frame(), text='statements tab', state='disabled')

        # tab_switcher.add(self.db_info_tab(master=master), text='db info')

        # tab_switcher.add(self.settings_tab(master=master), text='settings')

        return tab_switcher

    def set_tabs_state(self, state):
        for tab in self.menu.tabs()[1:]:
            self.menu.tab(tab, state=state)

    # def _style(self):
    #     # TODO not doing anything really just now
    #     app_style = ttk.Style()
    #     app_style.theme_use('clam')
    #     app_style.configure('Container.TFrame', borderwidth=5)
    #     # app_style.configure('border', borderwidth=5)
    #     # app_style.configure('focus', focuscolor='yellow', focusthickness=5)
    #     # app_style.configure('.', font='Symbols Nerd Font')
    #     # app_style.configure('.', font='Source Code Pro')
    #
    # def _grid(self):
    #     self._main_label.grid(row=0, column=0, columnspan=2)
    #     self._account.grid(row=1, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
    #     self._table.grid(row=2, column=0, sticky=tk.N+tk.E)
    #     self._work.grid(row=1, column=1, rowspan=2)
    #
    # def _layout(self):
    #     self.frame.columnconfigure(index=0, weight=0)
    #     self.frame.columnconfigure(index=1, weight=0)
    #     self.frame.rowconfigure(0, weight=0)
    #     self.frame.rowconfigure(index=1, weight=0)
    #     self.frame.rowconfigure(index=2, weight=0)
    #
    # def generate_insert_statements(self, table_number, amount, base_strings):
    #     """
    #     This should be useful here. We need to update another frame in workFrame.
    #
    #     """
    #     return self._data_service.generate_insert_statements(table_number=table_number, amount=amount,
    #                                                          base_strings=base_strings)
    #
    # def discard_generated_values(self):
    #     """
    #     Probably not needed here. Put this in the generated_values tab.
    #
    #     :return:
    #     """
    #     self._data_service.discard_generated_values()
    #     self._work.discard_generated_values()

    # passthrough function for main.py so far
    def mainloop(self):
        self.frame.mainloop()
