from flask import jsonify
from controllers.bookings import fetch_booking_details


def handle_create(req):
    booking_id = req.get("booking_id")
    booking_hash = req.get("booking_hash")

    booking_details = fetch_booking_details(
        booking_id=booking_id, booking_hash=booking_hash
    )

    print(f"TRIGGER: a booking with id {booking_id} was created")
    print(f"{booking_details}")
    return jsonify({"status": "create processed"}), 200


def handle_update(req):
    booking_id = req.get("booking_id")
    print(f"TRIGGER: a booking with id {booking_id} was updated")
    return jsonify({"status": "update processed"}), 200


def handle_cancel(req):
    booking_id = req.get("booking_id")
    print(f"TRIGGER: a booking with id {booking_id} was cancelled")
    return jsonify({"status": "cancel processed"}), 200
