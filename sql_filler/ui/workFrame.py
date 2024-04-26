from sql_filler.ui.utils import get_container
from sql_filler.ui.insertTab import InsertTab
import tkinter as tk
from tkinter import ttk


class WorkFrame:
    # TODO Last reorg went this far.
    #  workFrame:
    #  Things happening in one tab should influence what another tab would show.
    #  But so far we have one tab for filling column info, another for showing generated statements and
    #  selecting + running them. This we can update from data_service. Have tab switch run refresh on the new shown tab,
    #  load new state from data_service.

    def __init__(self, master=None, data_service=None):
        self.frame = get_container(master=master)
        self.insert_tab = None
        self.statements_tab = None

        self.menu = self.get_menu_bar(master=self.frame, data_service=data_service)
        self.menu.grid(row=0, column=0)

    def get_menu_bar(self, master=None, data_service=None):
        tab_switcher = ttk.Notebook(master=master)

        tab_switcher.add(self.table_info_tab(master=master), text='table info')
        # tab_switcher.add(self.insert_tab(master=master), text='insert data')
        self.insert_tab = InsertTab(master=master, data_service=data_service)
        tab_switcher.add(self.insert_tab.get_frame(), text='column data tab')
        self.statements_tab = StatementsTab(master=master, data_service=data_service)
        tab_switcher.add(self.statements_tab.get_frame(), text='statements tab')
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

    # ?
    def selected_table_label(self, master=None):
        return ttk.Label(master=master, text=f'Selected table {master}')

    # Passthrough functions because workframe handles this for now
    def switch_selected_table(self, selected: int = None):
        """
        Passthrough function for now. I want this to update other tabs too when they have the functionality.

        None needs to pass through so we can clear inserttab.

        :param selected:
        :return:
        """

        if isinstance(selected, int) or selected is None:
            self.insert_tab.switch_selected_table(new_selected_table=selected)

    # ?
    def discard_generated_values(self):
        self.insert_tab.discard_generated_values()


class StatementsTab:
    def __init__(self, master=None, data_service=None):
        self._data_service = data_service
        self.frame = get_container(text="Statements tab", master=master)

    def get_frame(self):
        return self.frame

    def grid(self):
        self.frame.grid()
