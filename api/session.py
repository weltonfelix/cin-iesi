class Session:
    """
    Manages user session and authentication.
    """

    def __init__(self, base_url: str, username: str):
        """
        Initializes the session with base URL and username.

        Args:
            base_url (str): The base URL of the API.
            username (str): The username for authentication.
        """
        self.base_url = base_url
        self.username = username
        self.token: str = None

    def login(self, password: str):
        """
        Authenticates the user and retrieves an access token.

        Args:
            password (str): The user's password.
        """
        from api import API

        response = API.post_login(self.username, password, self.base_url)

        if response is None or "access_token" not in response:
            raise Exception("Login failed: Invalid response from server.")

        self.token = response.get("access_token")
