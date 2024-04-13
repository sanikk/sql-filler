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

    def grid(self, row, column):
        """
        Passthrough method ui->self.frame

        :param row:
        :param column:
        :return:
        """
        self.frame.grid(row=row, column=column)

    def switch_selected_table(self, event):
        self._ui.switch_selected_table()

    def get_selected_table(self):
        idxs = self.lb.curselection()
        return idxs


        # When a user changes the selection, a <<ListboxSelect>> virtual event is generated. You can bind to this to take any action you need. Depending on your application, 
        # you may also want to bind to a double-click <Double-1> event and use it to invoke an action with the currently selected item.

# lbox.bind("<<ListboxSelect>>", lambda e: updateDetails(lbox.curselection()))
# lbox.bind("<Double-1>", lambda e: invokeAction(lbox.curselection()))

