import logging
from flask import jsonify
from controllers.bookings import fetch_booking_details
from controllers.access_codes import create_access_code
from util.date_to_iso import date_to_iso


def handle_create(req):
    booking_id = req.get("booking_id")
    booking_hash = req.get("booking_hash")

    booking_details = fetch_booking_details(
        booking_id=booking_id, booking_hash=booking_hash
    )

    access_code = create_access_code(
        name=f"Booking nr. {booking_id} for {booking_details['client_name']}",
        starts_at=date_to_iso(booking_details["start_date_time"], {"start": True}),
        ends_at=date_to_iso(booking_details["end_date_time"]),
        preferred_code_length=4,
    )

    logging.info(f"TRIGGER: a booking with id {booking_id} was created")
    return jsonify({"status": "create processed"}), 200


def handle_update(req):
    booking_id = req.get("booking_id")
    logging.info(f"TRIGGER: a booking with id {booking_id} was updated")
    return jsonify({"status": "update processed"}), 200


def handle_cancel(req):
    booking_id = req.get("booking_id")
    logging.info(f"TRIGGER: a booking with id {booking_id} was cancelled")
    return jsonify({"status": "cancel processed"}), 200
