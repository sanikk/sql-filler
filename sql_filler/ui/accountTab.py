from tkinter.ttk import Label, Entry, Button, Frame, LabelFrame


class AccountTab:
    # we need filler
    # https://www.postgresql.org/docs/9.0/functions-info.html
    def __init__(self, master=None, data_service=None):
        self._data_service = data_service

        self.frame = Frame(master=master)

        Label(master=self.frame, text="Username").grid(row=1, column=0)
        self._username_entry_box = Entry(master=self.frame)
        self._username_entry_box.grid(row=2, column=0)

        Label(master=self.frame, text="Database name").grid(row=3, column=0)
        self._dbname_entry_box = Entry(master=self.frame)
        self._dbname_entry_box.grid(row=4, column=0)

        Button(master=self.frame, text="Connect", command=self.connect).grid(row=1, column=1, sticky='EW', rowspan=2)
        self.disconnect_button = Button(master=self.frame, text="Disconnect", command=self.disconnect,
                                    state='disabled')
        self.disconnect_button.grid(row=3, column=1, sticky='EW', rowspan=2)

    def connect(self):
        dbname, username = self.get_entry_values()

        if dbname and username and self._data_service.account_new(dbname, username):
            self.disconnect_button.configure(state='normal')

    def disconnect(self):
        self._data_service.account_close()
        self.disconnect_button.configure(state='disabled')

    def grid(self, row, column, sticky):
        """
        Passthrough method for ui->self.frame
        :param row:
        :param column:
        :param sticky:
        :return:
        """
        self.frame.grid(row=row, column=column, sticky=sticky)

    def get_entry_values(self):
        if self._dbname_entry_box and self._username_entry_box:
            return self._dbname_entry_box.get(), self._username_entry_box.get()
        return None, None

    def get_frame(self):
        return self.frame
