from flask import jsonify


def handle_create(req):
    booking_id = req.get("booking_id")
    print(f"TRIGGER: a booking with id {booking_id} was created")
    return jsonify({"status": "create processed"}), 200


def handle_update(req):
    booking_id = req.get("booking_id")
    print(f"TRIGGER: a booking with id {booking_id} was updated")
    return jsonify({"status": "update processed"}), 200


def handle_cancel(req):
    booking_id = req.get("booking_id")
    print(f"TRIGGER: a booking with id {booking_id} was cancelled")
    return jsonify({"status": "cancel processed"}), 200
