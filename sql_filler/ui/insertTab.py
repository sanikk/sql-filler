from tkinter.ttk import Entry, Button, Treeview, Frame, Scrollbar, Label, LabelFrame
from tkinter import Canvas, messagebox


class InsertTab:
    def __init__(self, master=None, data_service=None):
        self._data_service = data_service
        self._entry_boxes = []
        self.saved_values = {}
        self.showing_table = None

        self.frame = Frame(master=master)

        self.table_label = Label(master=self.frame, text="No table selected", font="Calibri 22", foreground='cyan')

        self.scrollable = None
        self.amount_box = None
        self.box_container = None
        self._make_scrollable_frame()

        self._grid()
        self._layout()

    def _make_scrollable_frame(self):
        scrollbar = Scrollbar(master=self.frame)
        self.scrollable = Canvas(master=self.frame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.scrollable.yview)
        self.scrollable.grid(row=2, column=0, sticky='NSEW')
        scrollbar.grid(row=2, column=1, sticky='NS')
        self.scrollable.rowconfigure(1, weight=0)

        controls_box = LabelFrame(master=self.frame)
        Label(master=controls_box, text="Amount").grid(row=0, column=0, sticky='E')
        self.amount_box = Entry(master=controls_box)
        self.amount_box.grid(row=0, column=1)
        Button(master=controls_box, text="Generate inserts",
                                      command=self._generate_insert_statements).grid(row=0, column=2)
        controls_box.grid(row=1, column=0, columnspan=2)
        self.box_container = Frame(master=self.scrollable)
        self.box_container.columnconfigure(0, weight=1)  # big/small button
        self.box_container.columnconfigure(1, weight=1)  # datatype label
        self.box_container.columnconfigure(2, weight=1)  # entry box

        self.scrollable.create_window((0, 0), window=self.box_container, anchor='nw')

    def _grid(self):
        self.table_label.grid(row=0, column=0, columnspan=2)
        pass

    def _layout(self):
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(0, weight=1)
        pass

    def switch_selected_table(self, new_selected_table: int):
        """
        Public function to switch db table shown in this tab.

        :return: None
        """
        if self.showing_table is not None:
            values = self._collect_values()
            if any(values):
                self.saved_values[self.showing_table] = values

        self.amount_box.delete(0, 'end')
        self._entry_boxes = [self.amount_box]
        for box in self.box_container.grid_slaves():
            box.destroy()

        self.showing_table = new_selected_table
        if new_selected_table is not None:
            self._populate_insert_columns_tab(new_table=new_selected_table)
        self._reset_scrollregion()

    def _populate_insert_columns_tab(self, new_table: int = None):
        if new_table is None or not isinstance(new_table, int):
            return

        column_list = self._data_service.inserttab_fill(table_number=new_table)
        if not column_list:
            return
        for column_data in column_list:
            self._make_single_row(column_data=column_data)
        filled_values = self.saved_values.get(self.showing_table, [])
        if filled_values and any(filled_values):
            self.amount_box.insert('end', filled_values[0])
            for val, box in zip(filled_values[1:], self._entry_boxes):
                box[1].insert('end', val)

    def _make_single_row(self, master=None, column_data=None):
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
            self._entry_boxes.append(val_box)
        else:
            # TODO tähän button jossa default tekstinä, painamalla saa kentän johon syöttää arvon
            val_box = Label(master=master, text=column_data["column_default"])
        val_box.grid(row=ordinal_position, column=2, sticky='EW')

    def _collect_values(self):
        values = [a.get() for a in self._entry_boxes]
        return values

    def _clean_values(self):
        # TODO make sure user input is cleanish
        pass

    def _generate_insert_statements(self):
        values = self._collect_values()
        resp = self._data_service.generate_insert_statements(table_number=self.showing_table, values=values)
        # dev thing, we have signal
        print(f"{resp=}")
        messagebox.showinfo("generated", resp)

    def _insert_values(self):
        pass

    def _discard_generated_values(self):
        pass

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
