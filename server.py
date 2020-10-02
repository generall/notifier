from flask import request
from flask import Flask
import requests
import os
app = Flask(__name__)

BOT_API = os.environ["BOT_API"]
CHAT_ID = os.environ["CHAT_ID"]

@app.route('/', methods=['GET'])
def notify():
    message = request.args.get('m')
    if not message:
        return "try ?m=your-message", 400
    requests.post(
        f"https://api.telegram.org/bot{BOT_API}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": message,
            "disable_notification": False
        }
    )
    return 'Ok!', 200
