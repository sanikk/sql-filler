from tkinter import Tk
from sql_filler.UI.accountFrame import get_account_frame
from sql_filler.UI.tableFrame import get_table_frame
from sql_filler.UI.mainFrame import get_main_frame
from sql_filler.UI.utils import get_main_label


class UI(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.geometry('800x600')
        ##############################################################################################################
        # jos haluaisi tehdä wm_grid operaation se tehtäisiin tässä ja näin, ilmeisesti                              #
        #                                                                                                            #
        # self.grid(requestedWidthGridUnits, requestedHeightGridUnits, sizePerUnit, sizePerUnit)                     #
        #                                                                                                            #
        # docs: Tk.wm_grid(baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)                           #
        # WIDTHINC and HEIGHTINC are the width and height of a grid unit in pixels. BASEWIDTH and BASEHEIGHT are the #
        # number of grid units requested in Tk_GeometryRequest.                                                      #
        ##############################################################################################################
        self.title('SQL Filler')

        self._username = None
        self._dbname = None

        self._main_label = get_main_label(self)
        self._account_frame = get_account_frame(master=self)
        self._table_frame = get_table_frame(master=self)
        self._work_frame = get_main_frame(master=self)

        self.layout()

    def layout(self):
        self._main_label.grid(row=0, column=0, columnspan=2)
        self._account_frame.grid(row=1, column=0)
        self._table_frame.grid(row=2, column=0)
        self._work_frame.grid(row=1, column=1, rowspan=2)
        self.columnconfigure(index=0, weight=0, uniform='left', minsize=200)
        self.columnconfigure(index=1, weight=1, uniform='right', minsize=200)
        self.rowconfigure(0, weight=0, minsize=100)
        self.rowconfigure(index=2, weight=1, minsize=200)
        self.rowconfigure(index=3, weight=5, minsize=300)

    def get_dbname(self):
        return self._dbname

    def get_username(self):
        return self._username

    def is_connected(self):
        return self._dbname is not None and self._username is not None

    def connect(self, username, dbname):
        self._dbname = dbname
        self._username = username

