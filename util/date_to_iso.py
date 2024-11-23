from datetime import datetime, timedelta
import pytz


def date_to_iso(date_string, options=None):
    if options is None:
        options = {}

    start = options.get("start", False)

    paris_tz = pytz.timezone("Europe/Paris")

    date_with_timezone = paris_tz.localize(
        datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    )

    if start:
        date_with_timezone = date_with_timezone - timedelta(minutes=5)

    return date_with_timezone.astimezone(pytz.UTC).isoformat()
