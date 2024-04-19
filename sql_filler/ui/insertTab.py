from tkinter.ttk import Entry, Button, Treeview, Frame, Scrollbar, Label
from tkinter import Canvas


class InsertTab:
    def __init__(self, master=None, ui=None):
        self.frame = Frame(master=master)

        self.frame.rowconfigure(0, weight=0)
        self.table_label = Label(master=self.frame, text="No table selected", font="Calibri 22", foreground='cyan')
        # titles are purple & cyan now for that CGA/EGA look.
        self.table_label.grid(row=0, column=0, columnspan=2)

        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.scrollbar = Scrollbar(master=self.frame)
        self.scrollable = Canvas(master=self.frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scrollable.yview)
        self.scrollable.grid(row=2, column=0, sticky='NSEW')
        self.scrollbar.grid(row=2, column=1, sticky='NS')
        self.scrollable.rowconfigure(1, weight=0)

        self.generate_button = Button(master=self.frame, text="Generate inserts",
                                      command=self._generate_insert_statements)
        self.generate_button.grid(row=1, column=0)

        self.box_container = Frame(master=self.scrollable)
        self.box_container.columnconfigure(0, weight=1) # big/small button
        self.box_container.columnconfigure(1, weight=1) # datatype label
        self.box_container.columnconfigure(2, weight=1)  # entry box

        self.scrollable.create_window((0, 0), window=self.box_container, anchor='nw')

        # Button(master=self.frame, text="Insert to DB", command=self.insert_values).grid(row=1, column=0)

        self._ui = ui
        # self._entry_boxes = []
        self._test_dict = {}

    def switch_selected_table(self):
        """
        Public function to switch db table shown in this tab.

        Clears old table info from box_container, and fills it with new info.

        Finally we update both contained frames(self.frame and self.box_container) and then scrollbar scroll area.

        :return: None
        """
        for box in self.box_container.grid_slaves():
            box.destroy()
        self._populate_insert_columns_tab()
        self._reset_scrollregion()

    def _populate_insert_columns_tab(self):
        column_list = self._ui.get_insert_tab()
        if not column_list:
            return
        # self._entry_boxes.clear()
        self._test_dict.clear()
        for column_data in column_list:
            self._make_single_row(column_data=column_data)

    def _make_single_row(self, master=None, column_data=None):
        if not master:
            master = self.box_container
        # ordinal position = column_index = order the column rows are in box_container.
        ordinal_position = column_data['ordinal_position']
        small_button_params = {'row': ordinal_position, 'column': 0, 'sticky': 'EW'}
        big_button_params = {'row': ordinal_position, 'column': 0, 'columnspan': 2, 'sticky': 'W'}
        datatype_label_params = {'row': ordinal_position, 'column': 1}

        # small button/datatype label area (replaces big button)
        def expand():
            smallbutton.grid_forget()
            datatype_label.grid_forget()
            bigbutton.grid(big_button_params)
            self._reset_scrollregion()
        datatype_label = Label(master=master, text=column_data["data_type"])
        smallbutton = Button(master=master, text=column_data["column_name"], command=expand)
        smallbutton.grid(small_button_params)
        datatype_label.grid(datatype_label_params)

        # big button area (replaces small button/datatype label)
        def shrink():
            bigbutton.grid_forget()
            smallbutton.grid(small_button_params)
            datatype_label.grid(datatype_label_params)
            self._reset_scrollregion()
        big_button_text = '\n'.join([f"{key}: {column_data[key]}" for key in column_data.keys()])
        bigbutton = Button(master=master, text=big_button_text, command=shrink)

        # value box area
        if not column_data["column_default"]:
            val_box = Entry(self.box_container)
            # self._entry_boxes.append(val_box)
            self._test_dict[column_data["column_name"]] = val_box
        else:
            # TODO tähän button jossa default tekstinä, painamalla saa kentän johon syöttää arvon
            val_box = Label(master=master, text=column_data["column_default"])
        val_box.grid(row=ordinal_position, column=2, sticky='EW')

    def _collect_values(self):
        return {k: v.get() for k,v in self._test_dict.items()}
        # return {i: box.get() for i, box in self._test_dict}

    def _generate_insert_statements(self):
        values = self._collect_values()
        self._ui.generate_insert_statements(values)

    def _insert_values(self):
        pass

    def _discard_generated_values(self):
        pass

    def _show_generated_values(self, master=None, column_names=None, data=None):
        pass
        # tree = Treeview(master=self, columns=column_names, displaycolumns='#all', selectmode='extended', height=20)

    def get_frame(self):
        """
        Public function to access tab's Frame object.

        This one is needed now for tab_switcher(ttk.Notebook) when adding the tab.

        :return: tkinter.ttk.Frame
        """
        return self.frame

    def _reset_scrollregion(self):
        self.box_container.update()
        self.frame.update()
        self.scrollable.config(scrollregion=self.scrollable.bbox('all'))
