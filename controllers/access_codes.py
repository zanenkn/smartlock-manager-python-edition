import os
import requests
import logging


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
