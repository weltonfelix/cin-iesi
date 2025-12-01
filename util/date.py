def get_today_date() -> str:
    """
    Returns today's date in YYYY-MM-D format.

    Returns:
        str: Today's date as a string in the format YYYY-MM-D.
    """
    from datetime import date

    today = date.today()
    return f"{today.year}-{today.month}-{today.day}"
