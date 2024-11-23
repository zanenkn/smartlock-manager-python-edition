from flask import jsonify


def handle_create(request):
    print(f"TRIGGER: a booking with id {request.booking_id} was created")
    return jsonify({"status": "create processed"}), 200


def handle_update(request):
    print(f"TRIGGER: a booking with id {request.booking_id} was updated")
    return jsonify({"status": "update processed"}), 200


def handle_cancel(request):
    print(f"TRIGGER: a booking with id {request.booking_id} was cancelled")
    return jsonify({"status": "cancel processed"}), 200
