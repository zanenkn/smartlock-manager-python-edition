import hashlib
import os
from util.json_rpc_request import json_rpc_request
from util.get_token import get_token


def fetch_booking_details(booking_id, booking_hash):
    try:
        secret_key = os.getenv("SIMPLYBOOK_SECRET_KEY")
        sign_data = f"{booking_id}{booking_hash}{secret_key}"
        sign = hashlib.md5(sign_data.encode()).hexdigest()

        params = {
            "id": booking_id,
            "sign": sign,
        }

        token = get_token()

        return json_rpc_request(method="getBookingDetails", params=params, token=token)
    except Exception as error:
        raise Exception(
            f"Booking details for booking nr. {booking_id} could not be fetched: {error}"
        )
