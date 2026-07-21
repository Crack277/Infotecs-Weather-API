
from datetime import datetime, timedelta


def get_time_now():
    """Получаем время на данный момент."""
    time = datetime.now().replace(microsecond=0)
    return time


def nearest_time(time: datetime):
    """Округляем время до ближайшего часа, формата: %Y-%m-%dT%H:%M."""
    if time.minute >= 30:
        near_time = time.replace(minute=0) + timedelta(hours=1)
    else:
        near_time = time.replace(minute=0)

    formatted_time = near_time.strftime("%Y-%m-%dT%H:%M")

    return formatted_time