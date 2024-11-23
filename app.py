from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from util.verify_webhook_signature import verify_webhook_signature
from controllers.webhooks import handle_create, handle_update, handle_cancel

load_dotenv()

app = Flask(__name__)

port = int(os.getenv("PORT", 3000))


@app.route("/webhook-catcher", methods=["POST"])
@verify_webhook_signature
def webhook_catcher():
    req = request.get_json()

    notification_type = req.get("notification_type")

    if notification_type == "create":
        return handle_create(req)
    elif notification_type == "change":
        return handle_update(req)
    elif notification_type == "cancel":
        return handle_cancel(req)
    else:
        app.logger.info(f"Some other webhook was received: {notification_type}")
        return jsonify({"status": "ignored"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
