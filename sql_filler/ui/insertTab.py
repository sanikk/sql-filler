from tkinter.ttk import Frame, Label, Entry, Button, Treeview, LabelFrame
from sql_filler.ui.utils import get_container
import tkinter as tk
import tkinter.ttk as ttk


class InsertTab:
    # NEW TODO FIXME luonnostelmaa
    def __init__(self, master=None, ui=None):
        self.frame = get_container(master=master, width=800, height=550)
        Button(master=self.frame, text="Insert to DB", command=self.insert_values).grid(row=0, column=0)
        self.box_container = LabelFrame(master=self.frame, text="Table Columns", width=750)
        self.room_reserver, val = self._box_a_column()
        self.room_reserver.grid(row=1, column=0)

        self._ui = ui
        self._values = None

    def _box_a_column(self, master=None, column_id=None, column_name=None, column_data=None):
        # jokainen on pieni laatikko josta saa klikkaamalla isomman laatikon jossa on lisäinfoa,
        # pienessä laatikossa nimi ja entry field lukumäärälle
        # label ja entry

        # 0     1
        # |    |sb
        small_box = Frame(master=None, width=750, height=100)
        val = None
        if column_name:
            Label(master=small_box, text=column_name).grid(row=0, column=0)
            val = Entry(master=small_box)
            val.grid(row=0, column=1)
        return small_box, val

    def populate_insert_columns_tab(self):

        values = []
        column_list = self._ui.get_insert_tab()
        for column_id, column_name, column_data in column_list:

            boxi = self.info_box(column_id, column_name, column_data)

            values.append((column_id, boxi))

        self._values = values

    def insert_values(self):
        if self._values:
            self._ui.insert_values(self._values)

    def show_generated_values(self, master=None, column_names=None, data=None):
        tree = Treeview(master=self, columns=column_names, displaycolumns='#all', selectmode='extended', height=20)

    def get_frame(self):
        return self.frame


if __name__ == '__main__':
    testeri = tk.Tk()
    testeri.title('testeri')
    testeri.geometry('800x600')
    it = InsertTab(master=testeri, ui=None)
    it.get_frame().grid(row=0, column=0)
    testeri.mainloop()




