from tkinter.ttk import Entry, Button, Treeview, Frame, Scrollbar, Label, LabelFrame
from tkinter import Canvas, messagebox


class InsertTab:
    def __init__(self, master=None, data_service=None):
        self._data_service = data_service
        self._entry_boxes = []
        self.saved_values = {}
        # this should know which table it's showing for storing purposes
        self.showing_table = None

        self.frame = Frame(master=master)
        self.frame.rowconfigure(0, weight=0)
        self.table_label = Label(master=self.frame, text="No table selected", font="Calibri 22", foreground='cyan')
        self.table_label.grid(row=0, column=0, columnspan=2)

        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.scrollbar = Scrollbar(master=self.frame)
        self.scrollable = Canvas(master=self.frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.scrollable.yview)
        self.scrollable.grid(row=2, column=0, sticky='NSEW')
        self.scrollbar.grid(row=2, column=1, sticky='NS')
        self.scrollable.rowconfigure(1, weight=0)

        self.control_box = LabelFrame(master=self.frame)
        Label(master=self.control_box, text="Amount").grid(row=0, column=0, sticky='E')
        self.amount_box = Entry(master=self.control_box)
        self.amount_box.grid(row=0, column=1)
        self.generate_button = Button(master=self.control_box, text="Generate inserts",
                                      command=self._generate_insert_statements)
        self.generate_button.grid(row=0, column=2)
        self.control_box.grid(row=1, column=0, columnspan=2)

        self.box_container = Frame(master=self.scrollable)
        self.box_container.columnconfigure(0, weight=1) # big/small button
        self.box_container.columnconfigure(1, weight=1) # datatype label
        self.box_container.columnconfigure(2, weight=1)  # entry box

        self.scrollable.create_window((0, 0), window=self.box_container, anchor='nw')

    def switch_selected_table(self, new_selected_table):
        """
        Public function to switch db table shown in this tab.

        Clears old table info from box_container, and fills it with new info.

        Finally we update both contained frames(self.frame and self.box_container) and then scrollbar scroll area.

        :return: None
        """
        values = self._collect_values()
        if values and self.showing_table:
            self.saved_values[self.showing_table] = values


        self.amount_box.delete(0, 'end')
        self._entry_boxes.clear()
        for box in self.box_container.grid_slaves():
            box.destroy()

        self.showing_table = new_selected_table
        self._populate_insert_columns_tab()
        self._reset_scrollregion()

    def _populate_insert_columns_tab(self):
        self.selected_table, column_list = self._data_service.get_insert_tab()
        print(f"{self.selected_table=} now")
        if not column_list:
            return
        amount, filled_values = self.filled_values.get(self.selected_table, ('', {}))
        print(f"{amount=}, {filled_values=}")
        if amount:
            self.amount_box.insert('end', amount)

        for i, column_data in enumerate(column_list):
            self._make_single_row(column_data=column_data,
                                  filled_data=filled_values.get(i))

    def _make_single_row(self, master=None, column_data=None, filled_data=None):
        if not master:
            master = self.box_container
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
            if filled_data:
                val_box.insert('end', filled_data)
            self._entry_boxes.append((column_data["ordinal_position"], val_box))
        else:
            # TODO tähän button jossa default tekstinä, painamalla saa kentän johon syöttää arvon
            val_box = Label(master=master, text=column_data["column_default"])
        val_box.grid(row=ordinal_position, column=2, sticky='EW')

    def _collect_values(self):
        returnable = [self.amount_box.get() + a[1] for a in self._entry_boxes]
        print(f"{returnable=}")
        # returnable = {tupl[0]: tupl[1].get() for tupl in self._entry_boxes if tupl[1].get()}
        #if returnable:
        #    return int(self.amount_box.get()), returnable

    def _clean_values(self):
        # TODO make sure user input is cleanish
        pass

    def _generate_insert_statements(self):
        amount, values = self._collect_values()
        resp = self._ui.generate_insert_statements(table_number=self.selected_table, amount=amount, base_strings=values)
        # dev thing, we have signal
        messagebox.showinfo("generated", resp)

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
