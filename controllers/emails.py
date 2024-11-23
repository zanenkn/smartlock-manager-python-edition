import os
import requests
import logging


def send_email(
    client_name,
    client_email,
    code,
    booking_start,
    booking_end,
    booking_event,
    template_id,
):
    API_KEY = os.getenv("BREVO_API_KEY")

    email_data = {
        "to": [
            {
                "email": client_email,
                "name": client_name,
            },
        ],
        "templateId": template_id,
        "params": {
            "clientName": client_name,
            "code": code,
            "bookingStart": booking_start,
            "bookingEnd": booking_end,
            "bookingEvent": booking_event,
        },
    }

    try:
        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            json=email_data,
            headers={
                "accept": "application/json",
                "api-key": API_KEY,
                "content-type": "application/json",
            },
        )
        response.raise_for_status()

        logging.info("BrevoAPI: email sent successfully")
        return response.json()
    except requests.RequestException as error:
        error_message = (
            f"Email could not be sent to {client_email}: "
            f"{error.response.json() if error.response else str(error)}"
        )
        raise Exception(error_message) from error
