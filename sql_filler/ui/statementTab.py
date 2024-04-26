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

        button_frame = ttk.LabelFrame(master=self.frame)
        button_frame.grid(row=1, column=0)

        self.select_view = tk.Listbox(master=self.frame, selectmode='MULTIPLE')
        self.select_view.grid(row=2, column=0, sticky='NSE')
        ttk.Scrollbar(master=self.frame, command=self.select_view.yview).grid(row=2, column=1, sticky='NSW')

    def get_frame(self):
        return self.frame

    def grid(self):
        self.frame.grid()

    def _show_generated_values(self, master=None, column_names=None, data=None):
        pass
        # saf
