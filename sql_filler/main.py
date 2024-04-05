from ui.ui import UI
from services.postgresservice import PostgresService
from services.data_service import DataService

pos = PostgresService()
dataservice = DataService(pos)
ui = UI(dataservice=dataservice)
ui.mainloop()

