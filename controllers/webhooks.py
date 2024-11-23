import logging
from flask import jsonify
from controllers.bookings import fetch_booking_details
from controllers.access_codes import create_access_code
from controllers.emails import send_email
from util.date_to_iso import date_to_iso
from util.date_to_readable import date_to_readable


def handle_create(req):
    booking_id = req.get("booking_id")
    booking_hash = req.get("booking_hash")

    logging.info(f"TRIGGER: a booking with id {booking_id} was created")

    try:
        booking_details = fetch_booking_details(
            booking_id=booking_id, booking_hash=booking_hash
        )

        access_code = create_access_code(
            name=f"Booking nr. {booking_id} for {booking_details['client_name']}",
            starts_at=date_to_iso(booking_details["start_date_time"], {"start": True}),
            ends_at=date_to_iso(booking_details["end_date_time"]),
            preferred_code_length=4,
        )

        send_email(
            client_name=booking_details["client_name"],
            client_email=booking_details["client_email"],
            code=access_code["code"],
            booking_start=date_to_readable(booking_details["start_date_time"]),
            booking_end=date_to_readable(booking_details["end_date_time"]),
            booking_event=booking_details["event_name"],
            template_id=1,
        )

        logging.info(
            f"SUCCESS: Access code {access_code['code']} successfully created for {booking_details['client_name']} and sent to their email address {booking_details['client_email']}"
        )

        return jsonify({"status": "create processed"}), 200

    except Exception as e:
        logging.error(
            f"ERROR: failed to handle webhook on trigger 'create' due to: {str(e)}"
        )
        return jsonify({"error": str(e)}), 500


def handle_update(req):
    booking_id = req.get("booking_id")
    logging.info(f"TRIGGER: a booking with id {booking_id} was updated")
    return jsonify({"status": "update processed"}), 200


def handle_cancel(req):
    booking_id = req.get("booking_id")
    logging.info(f"TRIGGER: a booking with id {booking_id} was cancelled")
    return jsonify({"status": "cancel processed"}), 200
