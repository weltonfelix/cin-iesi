import os
import requests
from dotenv import load_dotenv
from datetime import date

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


class Session:
    def __init__(self):
        self.username = os.getenv("PLATFORM_USERNAME")
        self.token = None

    def login(self):
        response = requests.post(
            f"{BASE_URL}/login",
            data={"login": self.username, "senha": os.getenv("PLATFORM_PASSWORD")},
        )
        self.token = response.json().get("access_token")


session = Session()
session.login()

# Give todays date in YYYY-MM-DD format
today = date.today()
todayDate = f"{today.year}-{today.month}-{today.day}"

data = requests.get(
    f"{BASE_URL}/schedule/{todayDate}",
    headers={"Authorization": f"Bearer {session.token}"},
).json()

appointments = data.get("data", [])
#print(data)
for appointment in appointments:
    print(
        f"Patient: {appointment['patient']['name']}, Time: {appointment['hour']}, Status: {appointment['status']['nameGerund']}"
    )
