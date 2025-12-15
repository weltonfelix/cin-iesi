def get_today_date() -> str:
    """
    Returns today's date in YYYY-MM-D format.

    Returns:
        str: Today's date as a string in the format YYYY-MM-D.
    """
    from datetime import date

    today = date.today()
    return f"{today.year}-{today.month}-{today.day}"

def get_tomorrow_date() -> str:
    """
    Returns tomorrow's date in YYYY-MM-D format.

    Returns:
        str: tomorrow's date as a string in the format YYYY-MM-D.
    """

    from datetime import date, timedelta

    tomorrow = date.today() + timedelta(days=1)
    return f"{tomorrow.year}-{tomorrow.month}-{tomorrow.day}"