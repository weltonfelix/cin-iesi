import os
from dotenv import load_dotenv
from datetime import date

from api import API
from models.appointment import Appointment
from util.date import get_today_date

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
""" Base URL for the API """
CONFIRMED_STATUS_ID = 3
""" Status ID for confirmed appointments """


api = API(BASE_URL)
api.auth(os.getenv("PLATFORM_USERNAME"), os.getenv("PLATFORM_PASSWORD"))

date = get_today_date()
data = api.get_appointments(date, CONFIRMED_STATUS_ID)
appointments = [Appointment.from_json(app) for app in data]

# TODO: Connect to Twilio and send messages to patients
for appointment in appointments:
    if appointment.patient.cellphone:
        print(
            f"Patient: {appointment.patient.name}, Time: {appointment.hour}, Status: {appointment.status}, phone: {appointment.patient.cellphone}"
        )
