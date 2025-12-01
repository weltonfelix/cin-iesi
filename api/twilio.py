from twilio.rest import Client

class TwilioAPI:
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        """
        Initializes the Twilio API client.

        Args:
            account_sid (str): The Twilio Account SID.
            auth_token (str): The Twilio Auth Token.
            from_number (str): The Twilio phone number to send messages from.
        """
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_appointment_reminder(self, to_number: str, message: str) -> str:
        """
        Sends an appointment reminder SMS to the specified phone number.

        Args:
            to_number (str): The recipient's phone number.
            from_number (str): The sender's Twilio phone number.
            message (str): The message content.
        """
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=f"+55{to_number}"
            )
            return message.sid
        except Exception as e:
            print(f"Failed to send message to {to_number}: {e}")
            return ""
