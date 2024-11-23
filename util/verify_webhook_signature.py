import hashlib
import hmac
import json
import os
from flask import request, jsonify


def verify_webhook_signature(func):
    """
    Decorator function to verify the webhook signature.
    """

    def wrapper(*args, **kwargs):
        signature = request.headers.get("X-Signature")

        payload = json.dumps(request.get_json(), separators=(",", ":"))

        secret = os.getenv("SIMPLYBOOK_SECRET_KEY")

        calculated_signature = hmac.new(
            secret.encode(), payload.encode(), hashlib.sha256
        ).hexdigest()

        if signature == calculated_signature:
            return func(*args, **kwargs)
        else:
            return (
                jsonify({"error": "Invalid signature"}),
                401,
            )

    return wrapper
