from flask import request
from flask import Flask
import requests
import os
from time import time 

app = Flask(__name__)

BOT_API = os.environ["BOT_API"]
CHAT_ID = os.environ["CHAT_ID"]

backoff = 30 # seconds
last = 0


@app.route('/', methods=['GET'])
def notify():
    global last
    message = request.args.get('m')
    if not message:
        return "try ?m=your-message", 400

    current_time = int(time())
    if current_time - last < backoff:
        return "Not so fast", 429

    last = current_time

    res = requests.post(
        f"https://api.telegram.org/bot{BOT_API}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": message,
            "disable_notification": False
        }
    )
    if not res.ok:
        return "Oops!", 500

    return 'Ok!', 200
