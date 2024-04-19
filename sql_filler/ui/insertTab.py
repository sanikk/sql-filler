from tkinter.ttk import Entry, Button, Treeview, Frame, Scrollbar
from tkinter import Canvas, Label


class InsertTab:
    def __init__(self, master=None, ui=None):
        self.frame = Frame(master=master)

        self.frame.rowconfigure(0, weight=0)
        self.table_label = Label(master=self.frame, text="No table selected", font="Calibri 22", fg='cyan')
        self.table_label.grid(row=0, column=0, columnspan=2)

        self.frame.rowconfigure(1, weight=1)
        self.scrollbar = Scrollbar(master=self.frame)
        self.scrollable = Canvas(master=self.frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scrollable.yview)
        self.scrollable.grid(row=1, column=0, sticky='NS')
        self.scrollbar.grid(row=1, column=1, sticky='NS')
        self.scrollable.rowconfigure(1, weight=0)

        self.generate_button = Button(master=self.frame, text="Generate inserts",
                                      command=self.generate_insert_statements)
        self.generate_button.grid(row=1, column=2)

        self.box_container = Frame(master=self.scrollable)
        self.box_container.columnconfigure(0, weight=1) # big/small button
        self.box_container.columnconfigure(1, weight=1) # entry box
        self.box_container.columnconfigure(2, weight=1)  # entry box

        self.scrollable.create_window((0, 0), window=self.box_container, anchor='nw')
        self.box_container.bind("<Map>", self._reset_scrollregion())

        # Button(master=self.frame, text="Insert to DB", command=self.insert_values).grid(row=1, column=0)

        self._ui = ui
        self._entry_boxes = []

    def populate_insert_columns_tab(self):
        column_list = self._ui.get_insert_tab()
        if not column_list:
            return
        self._entry_boxes.clear()
        for column_data in column_list:
            self.make_single_row(column_data=column_data)

    def switch_selected_table(self):
        for box in self.box_container.grid_slaves():
            box.destroy()
        self.populate_insert_columns_tab()
        self._reset_scrollregion()

    def _collect_values(self):
        print(f"{self._entry_boxes}")
        values = [box.get() for box in self._entry_boxes]
        return values

    def generate_insert_statements(self):
        values = self._collect_values()
        self._ui.generate_insert_statements(values)

    def insert_values(self):
        pass

    def discard_generated_values(self):
        pass

    def show_generated_values(self, master=None, column_names=None, data=None):
        pass
        # tree = Treeview(master=self, columns=column_names, displaycolumns='#all', selectmode='extended', height=20)

    def get_frame(self):
        """
        This one is needed now for tab_switcher(ttk.Notebook) when adding the tab.

        :return:
        """
        return self.frame

    def make_single_row(self, master=None, column_data=None):
        if not master:
            master = self.box_container
        ordinal_position = column_data['ordinal_position']

        # small button/datatype label area (replaces big button)
        def expand():
            smallbutton.grid_forget()
            datatype_label.grid_forget()
            bigbutton.grid(row=ordinal_position, column=0, columnspan=2)
            self._reset_scrollregion()
        datatype_label = Label(master=master, text=column_data["data_type"])
        smallbutton = Button(master=master, text=column_data["column_name"], command=expand)
        smallbutton.grid(row=ordinal_position, column=0)
        datatype_label.grid(row=ordinal_position, column=1)

        # big button area (replaces small button/da..)
        def shrink():
            bigbutton.grid_forget()
            smallbutton.grid(row=ordinal_position, column=0)
            datatype_label.grid(row=ordinal_position, column=1)
            self._reset_scrollregion()
        txt = '\n'.join([f"{key}: {column_data[key]}" for key in column_data.keys()])
        bigbutton = Button(master=master, text=txt, command=shrink)

        # entry box area
        valbox = Entry(self.box_container, width=20)
        valbox.grid(row=ordinal_position, column=2)
        self._entry_boxes.append(valbox)

    def _reset_scrollregion(self):
        # might need the bbox one too
        self.box_container.update()
        self.frame.update()
        # self.scrollbar.
        self.scrollable.config(scrollregion=self.scrollable.bbox('all'))

