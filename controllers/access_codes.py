import os
import requests
import logging
import re


def create_access_code(name, starts_at, ends_at, preferred_code_length):
    headers = {
        "Authorization": f"Bearer {os.getenv('SEAM_API_KEY')}",
        "Content-Type": "application/json",
    }

    payload = {
        "device_id": os.getenv("SEAM_DEVICE_ID"),
        "timezone": "Europe/Paris",
        "name": name,
        "starts_at": starts_at,
        "ends_at": ends_at,
        "preferred_code_length": preferred_code_length,
    }

    try:
        response = requests.post(
            "https://connect.getseam.com/access_codes/create",
            json=payload,
            headers=headers,
        )
        response.raise_for_status()

        logging.info("SeamAPI: new access code created")
        return response.json().get("access_code")

    except requests.RequestException as e:
        error_message = (
            f"Access code could not be created: "
            f"{e.response.json() if e.response and e.response.content else str(e)}"
        )
        raise Exception(error_message) from e


def find_code_by_booking_id(code_list, booking_id):
    for code in code_list:
        match = re.search(r"Booking nr\.\s*(\d+)\s*for", code["name"])
        if match and match.group(1) == str(booking_id):
            return code
    return None


def get_access_code_from_booking_id(booking_id):
    headers = {
        "Authorization": f"Bearer {os.getenv('SEAM_API_KEY')}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.get(
            "https://connect.getseam.com/access_codes/list",
            params={"device_id": os.getenv("SEAM_DEVICE_ID")},
            headers=headers,
        )
        response.raise_for_status()

        access_code_list = response.json().get("access_codes", [])

        access_code = find_code_by_booking_id(access_code_list, booking_id)

        logging.info(
            f"SeamAPI: {f"access code located for booking {booking_id}" if access_code else f"no access code attached to booking ${booking_id}"}"
        )

        return access_code

    except requests.RequestException as error:
        error_message = (
            f"Access code for booking nr. {booking_id} could not be found:"
            f"{error.response.json() if error.response and error.response.content else str(error)}"
        )
        raise Exception(error_message) from error
