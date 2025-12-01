class Patient:
    """
    Patient model

    Defines the Patient class used in appointment handling.
    """

    def __init__(
        self,
        id: int,
        name: str,
        cellphone: str,
        is_whatsapp: bool,
        email: str,
        gender: str | None,
    ):
        """
        Initializes a Patient instance.

        Args:
            id (int): The patient's unique identifier.
            name (str): The patient's name.
            cellphone (str): The patient's cellphone number.
            is_whatsapp (bool): Indicates if the patient uses WhatsApp.
            email (str): The patient's email address.
            gender (str | None): The patient's gender.
        """
        self.patient_id = id
        self.name = name
        self.cellphone = cellphone
        self.is_whatsapp = is_whatsapp
        self.email = email
        self.gender = gender

    @staticmethod
    def from_json(json_data: str) -> "Patient":
        """
        Creates a Patient instance from JSON data.

        Args:
            json_data (str): JSON data containing patient information.
        Returns:
            Patient: An instance of the Patient class.
        """
        return Patient(
            id=json_data["id"],
            name=json_data["name"],
            cellphone=json_data["cellphone"],
            is_whatsapp=json_data["flagWhatsapp"] == 1,
            email=json_data["email"],
            gender=json_data["gender"],
        )
