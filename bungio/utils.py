import datetime


def get_now_with_tz() -> datetime.datetime:
    """
    Returns the timezone aware current datetime

    Returns:
        Timezone aware datetime
    """

    return datetime.datetime.now(tz=datetime.timezone.utc)
