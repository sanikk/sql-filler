from tkinter.ttk import Frame, Label, Entry, Button, Treeview, LabelFrame
from sql_filler.ui.utils import get_container
import tkinter as tk
import tkinter.ttk as ttk


class InsertTab:
    # NEW TODO FIXME luonnostelmaa
    def __init__(self, master=None, ui=None):
        self.frame = container = get_container(master=master, width=800, height=550)
        Button(master=self.frame, text="Insert to DB", command=self.insert_values).grid(row=1, column=0)
        self.box_container = LabelFrame(master=self.frame, text="Table Columns", width=750, height=1200)
        self.box_container.grid(row=2, column=0)

        self._ui = ui
        self._group = []
        self._values = None

    def populate_insert_columns_tab(self):
        column_list = self._ui.get_insert_tab()
        for column_data in column_list:
            new_label = Label(master=self.box_container, text=column_data["column_name"])
            self._group.append(new_label)
            new_label.grid(row=column_data["ordinal_position"], column=0)

    def switch_selected_table(self):
        for box in self._group:
            # kato mallia accountista
            box.grid_forget()
        # bindaa tämä siihen selectediin tauluissa
        self.populate_insert_columns_tab()

    def insert_values(self):
        pass

    def show_generated_values(self, master=None, column_names=None, data=None):
        pass
        # tree = Treeview(master=self, columns=column_names, displaycolumns='#all', selectmode='extended', height=20)

    def get_frame(self):
        return self.frame


if __name__ == '__main__':
    # data_service = TesterDataService()
    testeri = tk.Tk()
    testeri.title('testeri')
    testeri.geometry('800x600')

    # it = InsertTab(master=testeri, ui=None, data_service_injection=data_service)
    # it.get_frame().grid(row=0, column=0)

    testeri.mainloop()


