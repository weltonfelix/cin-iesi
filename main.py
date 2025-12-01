import os
import requests
from dotenv import load_dotenv
from datetime import date

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
CONFIRMED_STATUS_ID = 3


class Session:
    username: str = os.getenv("PLATFORM_USERNAME")

    def __init__(self):
        self.token: str = None

    def login(self):
        response = requests.post(
            f"{BASE_URL}/login",
            data={"login": self.username, "senha": os.getenv("PLATFORM_PASSWORD")},
        )
        self.token = response.json().get("access_token")


class Patient:
    def __init__(
        self,
        id: int,
        name: str,
        cellphone: str,
        is_whatsapp: bool,
        email: str,
        gender: str | None,
    ):
        self.patient_id = id
        self.name = name
        self.cellphone = cellphone
        self.is_whatsapp = is_whatsapp
        self.email = email
        self.gender = gender

    @staticmethod
    def from_json(json_data):
        return Patient(
            id=json_data["id"],
            name=json_data["name"],
            cellphone=json_data["cellphone"],
            is_whatsapp=json_data["flagWhatsapp"] == 1,
            email=json_data["email"],
            gender=json_data["gender"],
        )


class Appointment:
    def __init__(
        self,
        id: int,
        date: str,
        hour: str,
        status: str,
        local: str | None,
        patient: Patient,
    ):
        self.appointment_id = id
        self.date = date
        self.hour = hour
        self.status = status
        self.local = local
        self.patient = patient

    @staticmethod
    def from_json(json_data):
        return Appointment(
            id=json_data["id"],
            date=json_data["date"],
            hour=json_data["hour"],
            status=json_data["status"]["nameGerund"],
            local=json_data.get("local", {}).get("name", None),
            patient=Patient.from_json(json_data["patient"]),
        )


session = Session()
session.login()

# Give todays date in YYYY-MM-d format
today = date.today()
todayDate = f"{today.year}-{today.month}-{today.day}"

data = requests.get(
    f"{BASE_URL}/schedule/{todayDate}",
    headers={"Authorization": f"Bearer {session.token}"},
    params={"status": CONFIRMED_STATUS_ID},
).json()

appointments = [Appointment.from_json(app) for app in data.get("data", [])]

# TODO: Connect to Twilio and send messages to patients
for appointment in appointments:
    if appointment.patient.cellphone:
        print(
            f"Patient: {appointment.patient.name}, Time: {appointment.hour}, Status: {appointment.status}, phone: {appointment.patient.cellphone}"
        )
