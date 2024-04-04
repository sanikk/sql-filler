from ui.ui import UI
from services.postgresservice import PostgresService

pos = PostgresService()

ui = UI(pos=pos)
ui.mainloop()

