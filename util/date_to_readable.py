from datetime import datetime


def date_to_readable(date_string):
    parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    return parsed_date.strftime("%d/%m/%Y %H:%M")
