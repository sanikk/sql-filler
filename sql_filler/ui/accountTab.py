from tkinter.ttk import Label, Entry, Button, Frame, LabelFrame


class AccountTab:
    # we need filler
    # https://www.postgresql.org/docs/9.0/functions-info.html
    def __init__(self, master=None, data_service=None, ui=None):
        self.frame = Frame(master=master)
        self._username_entry_box = None
        self._database_entry_box = None
        self.unconnected_box = self.unconnected(master=self.frame)
        self.unconnected_box.grid(row=1, column=0, rowspan=2)

        Button(master=self.frame, text="Connect", command=self.connect).grid(row=1, column=1, sticky='EW')
        self.disconnector = Button(master=self.frame, text="Disconnect", command=self.disconnect,
                                   state='disabled')

        self.disconnector.grid(row=2, column=1, sticky='EW')

        self._data_service = data_service
        self._ui = ui

    def unconnected(self, master=None):
        connected_box = LabelFrame(master=self.frame)
        Label(master=connected_box, text="Username").grid(row=1, column=0)
        self._username_entry_box = Entry(master=connected_box)
        self._username_entry_box.grid(row=2, column=0)

        Label(master=connected_box, text="Database name").grid(row=3, column=0)
        self._dbname_entry_box = Entry(master=connected_box)
        self._dbname_entry_box.grid(row=4, column=0)
        return connected_box

    def connect(self):
        dbname, username = self.get_entry_values()

        if dbname and username and self._data_service.account_new(dbname, username):
            self._ui.set_tabs_state('normal')
            self.disconnector.configure(state='normal')

    def disconnect(self):
        self._data_service.account_close()
        self._ui.set_tabs_state('disabled')
        self.disconnector.configure(state='disabled')

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
