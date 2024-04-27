import tkinter as tk
import tkinter.ttk as ttk
from sql_filler.ui.utils import get_container


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

        # big/small vars
        self.scrollable = None
        self.amount_box = None
        self.box_container = None



    def refresh_statements(self, event):
        statements = self._data_service.statementtab_fill()
        print(f"{statements=}")
        #self.select_view.delete(0, 'end')
        #self.select_view.insert('end', *statements)


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
