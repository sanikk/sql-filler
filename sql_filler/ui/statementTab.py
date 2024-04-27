import tkinter as tk
import tkinter.ttk as ttk
from sql_filler.ui.utils import get_container


"""
NOTE - OLD NOTES !
i just used the readymade file.

Playground for prepared statements.

https://www.postgresql.org/docs/current/sql-prepare.html

- Prepared statements only last for the duration of the current database session.

- Prepared statements potentially have the largest performance advantage when a single session is being used to execute
a large number of similar statements. The performance difference will be particularly significant if the statements
are complex to plan or rewrite, e.g., if the query involves a join of many tables or requires the application of
several rules. If the statement is relatively simple to plan and rewrite but relatively expensive to execute, the
performance advantage of prepared statements will be less noticeable.

https://www.postgresql.org/docs/current/view-pg-prepared-statements.html

- get info on prepared statements for the session

Educational tool? Show what statements are prepared serverside from queries?

Comparison for prepared statements? custom vs regular (vs raw?)
"""


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

        self.select_view = tk.Listbox(master=self.frame, selectmode='MULTIPLE')
        self.select_view.grid(row=2, column=0, sticky='NSEW')
        ttk.Scrollbar(master=self.frame, command=self.select_view.yview).grid(row=2, column=1, sticky='NSW')
        # self.frame.rowconfigure(2, weight=5)
        # self.frame.columnconfigure(0, weight=5)

    def refresh_statements(self, event):
        statements = self._data_service.statementtab_fill()
        print(f"{statements=}")
        self.select_view.delete(0, 'end')
        self.select_view.insert('end', *statements)


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
