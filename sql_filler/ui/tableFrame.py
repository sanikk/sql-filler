from tkinter import Listbox, Scrollbar

from sql_filler.ui.utils import get_container


class TableFrame:
    # TODO color code status of table. are there generated inserts or filled data.
    def __init__(self, master=None, data_service=None, insert_tab=None):
        self._data_service = data_service
        self._insert_tab = insert_tab

        self.frame = get_container(master=master)
        self.lb = Listbox(self.frame, height=12, width=30, selectmode='BROWSE')
        self.lb.bind('<<ListboxSelect>>', self.switch_selected_table)
        Scrollbar(self.frame, command=self.lb.yview).grid(row=0, column=1, sticky='NSW')
        self.lb.grid(row=0, column=0)

    def update_tables(self):
        self.lb.delete(0, 'end')
        content = self._data_service.get_table_names()
        if content:
            self.lb.insert('end', *content)

    def grid(self, row, column, sticky):
        """
        Passthrough method ui->self.frame
        """
        self.frame.grid(row=row, column=column, sticky=sticky)

    def switch_selected_table(self, event):
        table_as_string = event.widget.curselection()
        if table_as_string and len(table_as_string) == 1:
            try:
                table_as_number = int(table_as_string[0])
                self._insert_tab.switch_selected_table(selected=table_as_number)

            except ValueError:
                # TODO this should not happen. log this
                print(f"tableFrame switch ValueError: {table_as_string=}")
                return
        else:
            # TODO this should not happen. log this?
            #  listbox sometimes sends () as tuple
            return


    # def get_selected_table(self) -> int:
    #     idxs = self.lb.curselection()
    #     if len(idxs) == 1:
    #         return idxs[0]
    #     return -1
