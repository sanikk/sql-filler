from tkinter.ttk import Entry, Button, Treeview, Frame, Scrollbar
from tkinter import Canvas
from sql_filler.ui.utils import get_container


class InsertTab:
    def __init__(self, master=None, ui=None):
        self.frame = Frame(master=master)
        self.frame.rowconfigure(1, weight=0)

        self.scrollbar = Scrollbar(master=self.frame)
        self.scrollable = Canvas(master=self.frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scrollable.yview)
        self.scrollable.grid(row=1, column=1)
        self.scrollbar.grid(row=1, column=2, sticky='NS')

        self.scrollable.rowconfigure(1, weight=1)
        # self.frame.rowconfigure(1, weight=1)

        self.box_container = Frame(master=self.scrollable)
        self.box_container.columnconfigure(0, weight=3) # big/small button
        self.box_container.columnconfigure(1, weight=1) # entry box
        self.box_container.grid(row=1, column=0)

        # Button(master=self.frame, text="Insert to DB", command=self.insert_values).grid(row=1, column=0)

        self._ui = ui
        self._entry_boxes = {}

    def populate_insert_columns_tab(self):
        column_list = self._ui.get_insert_tab()
        for column_data in column_list:
            self.make_single_row(column_data=column_data)

    def switch_selected_table(self):
        for box in self.box_container.grid_slaves():
            box.destroy()
        self.populate_insert_columns_tab()
        self._reset_scrollregion()

    def insert_values(self):
        pass

    def show_generated_values(self, master=None, column_names=None, data=None):
        pass
        # tree = Treeview(master=self, columns=column_names, displaycolumns='#all', selectmode='extended', height=20)

    def get_frame(self):
        """
        This one is need now for tab_switcher(ttk.Notebook) when adding the tab.

        :return:
        """
        return self.frame

    def make_single_row(self, master=None, column_data=None):
        if not master:
            master = self.box_container

        ordinal_position = column_data['ordinal_position']

        def expand():
            smallbutton.grid_forget()
            bigbutton.grid(row=ordinal_position, column=0)
            self._reset_scrollregion()

        smallbutton = Button(master=master, text=column_data["column_name"], command=expand)
        smallbutton.grid(row=ordinal_position, column=0)

        def shrink():
            bigbutton.grid_forget()
            smallbutton.grid(row=ordinal_position, column=0)
            self._reset_scrollregion()

        txt = '\n'.join([f"{key}: {column_data[key]}" for key in column_data.keys()])
        bigbutton = Button(master=master, text=txt, command=shrink)
        valbox = Entry(self.box_container, width=20)
        valbox.grid(row=ordinal_position, column=1)
        self._entry_boxes[ordinal_position] = valbox

    def _reset_scrollregion(self):
        # might need the bbox one too
        self.box_container.update()
        self.frame.update()
        self.scrollable.config(scrollregion=self.scrollable.bbox('all'))

