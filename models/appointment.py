from models.patient import Patient


class Appointment:
    """
    Appointment model

    Defines the Appointment class used for managing appointments.
    """

    def __init__(
        self,
        id: int,
        date: str,
        hour: str,
        status: str,
        local: str | None,
        patient: Patient,
    ):
        """
        Initializes an Appointment instance.

        Args:
            id (int): The appointment's unique identifier.
            date (str): The date of the appointment.
            hour (str): The time of the appointment.
            status (str): The status of the appointment.
            local (str | None): The location of the appointment.
            patient (Patient): The patient associated with the appointment.
        """
        self.appointment_id = id
        self.date = date
        self.hour = hour
        self.status = status
        self.local = local
        self.patient = patient

    @staticmethod
    def from_json(json_data):
        """
        Creates an Appointment instance from JSON data.

        Args:
            json_data (str): JSON data containing appointment information.
        Returns:
            Appointment: An instance of the Appointment class.
        """
        return Appointment(
            id=json_data["id"],
            date=json_data["date"],
            hour=json_data["hour"],
            status=json_data["status"]["nameGerund"],
            local=json_data.get("local", {}).get("name", None),
            patient=Patient.from_json(json_data["patient"]),
        )
