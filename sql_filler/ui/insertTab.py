from tkinter.ttk import Entry, Button, Frame, Label, LabelFrame
from tkinter import messagebox

from sql_filler.ui.tableFrame import TableFrame
from sql_filler.ui.utils import make_scrollable_frame


# TODO something wrong with saved values. The first field gets filled with spam.
class InsertTab:
    def __init__(self, master=None, data_service=None):
        self._data_service = data_service

        self._entry_boxes = []
        self.saved_values = {}
        self.showing_table = None

        self.frame = Frame(master=master)

        self.controls_box = None
        self.amount_box = None
        self.controls_box, self.amount_box = self._make_controls_box(master=self.frame)
        self.table_frame = TableFrame(master=self.frame, data_service=data_service, insert_tab=self)

        self.scrollable = None
        self.box_container = None
        self.scrollable, self.box_container = make_scrollable_frame(master=self.frame, row=0, column=1, rowspan=2)
        self.box_container.columnconfigure(0, weight=1)  # big/small button
        self.box_container.columnconfigure(1, weight=1)  # datatype label
        self.box_container.columnconfigure(2, weight=1)  # entry box

        self._grid()
        self._layout()

    def _grid(self):
        self.controls_box.grid(row=0, column=0)
        self.table_frame.grid(row=1, column=0, sticky='ew')

    def _layout(self):
        self.frame.rowconfigure(1, weight=1) # scrollable
        self.frame.columnconfigure(1, weight=1)

    def _make_controls_box(self, master=None):
        controls_box = LabelFrame(master=master)
        Label(master=controls_box, text="Amount").grid(row=0, column=0, sticky='E')
        amount_box = Entry(master=controls_box)
        amount_box.grid(row=0, column=1)
        Button(master=controls_box, text="Generate inserts",
               command=self._generate_insert_statements).grid(row=1, column=0, columnspan=2)
        return controls_box, amount_box

    def switch_selected_table(self, selected: int):
        """
        Public function to switch db table shown in this tab.

        :return: None
        """
        self._save_filled_values()

        self._clear_box_container()

        self.showing_table = selected
        if selected is not None:
            self._populate_insert_columns_tab(new_table=selected)
        self._reset_scrollregion()

    def _save_filled_values(self):
        if self.showing_table is not None:
            amount = self.amount_box.get()
            values = self._collect_values()
            print(f"{values=}, {amount=}, {self.showing_table=}")
            if any(values):
                self.saved_values[self.showing_table] = (amount, values)
                print(f"{self.saved_values=}")

    def _load_filled_values(self):
        filled_values = self.saved_values.get(self.showing_table, [])
        if filled_values and any(filled_values):
            self.amount_box.insert('end', filled_values[0])
            for val, box in zip(filled_values[1:], self._entry_boxes):
                box[1].insert('end', val)

    def _clear_box_container(self):
        self.amount_box.delete(0, 'end')
        self._entry_boxes = []
        for box in self.box_container.grid_slaves():
            box.destroy()

    def _get_amount(self):
        amount = self.amount_box.get()
        if amount:
            try:
                amount = int(amount)
            except ValueError:
                amount = 0
        return amount

    def _populate_insert_columns_tab(self, master=None, new_table: int = None):
        if not master:
            master = self.box_container
        if not isinstance(new_table, int):
            return
        column_list = self._data_service.inserttab_fill(table_number=new_table)
        if not column_list:
            return
        for column_data in column_list:
            self._make_single_row(master=master, column_data=column_data)
        self._fill_values_from_storage()


    def _make_single_row(self, master=None, column_data=None):
        column_number = column_data['ordinal_position']
        small_button_params = {'row': column_number, 'column': 0, 'sticky': 'EW'}
        big_button_params = {'row': column_number, 'column': 0, 'columnspan': 2, 'sticky': 'W'}
        datatype_label_params = {'row': column_number, 'column': 1}

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
            self._entry_boxes.append((column_number, val_box))
        else:
            # TODO tähän button jossa default tekstinä, painamalla saa kentän johon syöttää arvon
            val_box = Label(master=master, text=column_data["column_default"])
        val_box.grid(row=column_number, column=2, sticky='EW')

    def _collect_values(self):
        values = [(i, a.get()) for i, a in self._entry_boxes]
        return values

    def _clean_values(self):
        # TODO make sure user input is cleanish
        pass

    def _generate_insert_statements(self):
        raw_amount = self.amount_box.get()
        amount = 0
        if raw_amount:
            try:
                amount = int(raw_amount)
            except ValueError:
                return
        base_strings = self._collect_values()
        resp = self._data_service.generate_insert_statements(table_number=self.showing_table, amount=amount,
                                                             base_strings=base_strings)
        # TODO we need better feedback to user
        if resp:
            messagebox.showinfo("generated", str(resp))

    def get_frame(self):
        """
        Public function to access tab's Frame object.

        This one is needed now for tab_switcher(ttk.Notebook) when adding the tab.

        :return: tkinter.ttk.Frame
        """
        return self.frame

    def refresh_tables(self):
        self.table_frame.refresh_tables()

    def _reset_scrollregion(self):
        self.box_container.update()
        self.frame.update()
        self.scrollable.config(scrollregion=self.scrollable.bbox('all'))
