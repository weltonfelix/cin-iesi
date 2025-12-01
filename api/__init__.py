import requests
from .session import Session

ALL_CALENDARS_ID=0

class API:
    """
    Handles API interactions including authentication and data retrieval.
    """

    def __init__(self, base_url: str, session: Session | None = None):
        """
        Initializes the API with base URL and optional session.

        Args:
            base_url (str): The base URL of the API.
            session (Session | None): An optional authenticated session.
        """
        self.base_url = base_url
        self.session = session

    def auth(self, username: str, password: str) -> Session:
        """
        Authenticates the user and creates a session.

        Args:
            username (str): The username for authentication.
            password (str): The password for authentication.

        Returns:
            Session: An authenticated session object.
        """
        self.session = Session(self.base_url, username)
        self.session.login(password)
        return self.session

    @staticmethod
    def post_login(username: str, password: str, base_url: str) -> Session | None:
        """
        Sends a login request to the API.

        Args:
            username (str): The username for authentication.
            password (str): The password for authentication.
            base_url (str): The base URL of the API.

        Returns:
            Session | None: The session object if login is successful, None otherwise.
        """
        try:
            return requests.post(
                f"{base_url}/login",
                data={"login": username, "senha": password},
            ).json()
        except requests.RequestException:
            print(f"An error occurred during login")
            return None

    def get_appointments(self, date: str, status_id: int | None = None) -> list[dict]:
        """
        Retrieves appointments for a given date and status.

        Args:
            date (str): The date for which to retrieve appointments in YYYY-MM-d format.
            status_id (int): The status ID to filter appointments.
        """
        if not self.session or not self.session.token:
            raise Exception("Session is not authenticated. Please login first.")

        try:
            response = requests.get(
                f"{self.base_url}/schedule/{date}",
                headers={"Authorization": f"Bearer {self.session.token}"},
                params={"status": status_id, "idCalendar": ALL_CALENDARS_ID},
            )
            return response.json().get("data", [])
        except requests.RequestException:
            print(f"An error occurred while fetching appointments for {date}")
            return []
