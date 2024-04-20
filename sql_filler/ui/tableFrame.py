from tkinter import Listbox, Scrollbar

from sql_filler.ui.utils import get_container


class TableFrame:
    def __init__(self, master=None, data_service=None, ui=None):
        self._data_service = data_service
        self._ui = ui

        self.frame = get_container(master=master)
        self.lb = Listbox(self.frame, height=12, width=30)
        self.lb.bind('<<ListboxSelect>>', self.switch_selected_table)
        Scrollbar(self.frame, command=self.lb.yview).grid(row=0, column=1, sticky='W')
        self.lb.grid(row=0, column=0)

    def update_tables(self):
        self.lb.delete(0, 'end')
        content = self._ui.get_table_names()
        if not content:
            content = []
        self.lb.insert('end', *content)

    def grid(self, row, column, sticky):
        """
        Passthrough method ui->self.frame

        :param sticky:
        :param row:
        :param column:
        :return:
        """
        self.frame.grid(row=row, column=column, sticky=sticky)

    def switch_selected_table(self, event):
        self._ui.switch_selected_table()
        # selected=event.widget.curselection()

    def get_selected_table(self) -> int:
        idxs = self.lb.curselection()
        if len(idxs) == 1:
            return idxs[0]
        return -1
