import os
from dotenv import load_dotenv
from datetime import date

from api import API
from api.twilio import TwilioAPI
from models.appointment import Appointment
from util.date import get_today_date, get_tomorrow_date

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
""" Base URL for the API """
CONFIRMED_STATUS_ID = 3
""" Status ID for confirmed appointments """


api = API(BASE_URL)
api.auth(os.getenv("PLATFORM_USERNAME"), os.getenv("PLATFORM_PASSWORD"))

twilioAPI = TwilioAPI(
      os.getenv("TWILIO_ACCOUNT_SID"),
      os.getenv("TWILIO_ACCOUNT_TOKEN"),
      os.getenv("TWILIO_NUMBER_FROM")
    )

# date = get_today_date() para a data de hoje
date = get_tomorrow_date() # para a data de amanhã
data = api.get_appointments(date, CONFIRMED_STATUS_ID)
appointments = [Appointment.from_json(app) for app in data]

for appointment in appointments:
    if appointment.patient.cellphone:
        result = twilioAPI.send_appointment_reminder(
            appointment.patient.cellphone,
            f"Olá! Confirmamos o agendamento de {appointment.patient.name} no NPI (Núcleo da Pessoa Idosa) para amanhã, às {appointment.hour}. Qualquer dúvida, estamos à disposição."
        )
