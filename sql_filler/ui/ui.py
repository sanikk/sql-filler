from tkinter import Tk
from tkinter.ttk import Notebook

from sql_filler.ui.accountTab import AccountTab
from sql_filler.ui.insertTab import InsertTab
from sql_filler.ui.statementTab import StatementTab

from sql_filler.ui.utils import get_main_label


class UI:
    def __init__(self, master=None, data_service=None):
        self._data_service = data_service

        self.frame = Tk()
        self.frame.geometry('800x600')
        self.frame.title('SQL Filler')
        self._main_label = get_main_label(master=self.frame)

        self._insert_tab = None
        self._account_tab = None
        self._statement_tab = None

        self._menu = self.get_menu_bar(master=self.frame, data_service=data_service)
        self._menu.bind('<<NotebookTabChanged>>', self.tab_change_chores)

        # self._style()
        self._grid()
        self._layout()

    def tab_change_chores_old(self, event):
        selected_tab = event.widget.index(event.widget.select())
        # if selected_tab == 0:
            # account tab
        if selected_tab == 1:
            # insert tab
            self._insert_tab.refresh_tables()
        if selected_tab == 2:
            # statement tab
            self._statement_tab.refresh_statements()

    def tab_change_chores(self, event):
        selected_tab = event.widget.tab(event.widget.select(), 'text')
        if selected_tab == 'generate inserts':
            self._insert_tab.refresh_tables()
        if selected_tab == 'prepared inserts':
            self._statement_tab.refresh_statements()

    def get_menu_bar(self, master=None, data_service=None):
        tab_switcher = Notebook(master=master)

        self._insert_tab = InsertTab(master=master, data_service=data_service)
        self._account_tab = AccountTab(master=master, data_service=data_service)
        tab_switcher.add(self._account_tab.get_frame(), text='account')

        tab_switcher.add(self._insert_tab.get_frame(), text='generate inserts')

        self._statement_tab = StatementTab(master=master, data_service=data_service)
        tab_switcher.add(self._statement_tab.get_frame(), text='prepared inserts')

        # tab_switcher.add(self.db_info_tab(master=master), text='db info')
        # tab_switcher.add(self.settings_tab(master=master), text='settings')
        return tab_switcher

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
    def _grid(self):
        self._main_label.grid(row=0, column=0, columnspan=1)
        self._menu.grid(row=1, column=0)

    def _layout(self):
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)

    # passthrough function for main.py so far
    def mainloop(self):
        self.frame.mainloop()
