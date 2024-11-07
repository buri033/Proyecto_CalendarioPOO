from fastapi import FastAPI

from Calendar.functions.get_service import get_calendar_service
from Calendar.routes.calendar import routes_calendar

app = FastAPI()
app.include_router(routes_calendar, prefix="/calendar")
get_calendar_service()

app.include_router(routes_calendar, prefix="/calendar")

