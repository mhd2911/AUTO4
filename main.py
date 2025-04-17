from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7974658962:AAGyaruAweaZsjTDU8C_C1fW9LRTimtbPrs"
CHANNEL = "@trading_alert_mhd"

@app.route('/', methods=['POST'])
def send_signal():
    data = request.json
    symbol = data.get("symbol", "N/A")
    direction = data.get("direction", "N/A")
    entry = data.get("entry", "N/A")
    target = data.get("target", "N/A")
    stop = data.get("stop", "N/A")

    message = f"تنبيه تداول\n" \
              f"العملة: {symbol}\n" \
              f"النوع: {direction}\n" \
              f"الدخول: {entry}\n" \
              f"الهدف: {target}\n" \
              f"وقف الخسارة: {stop}"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, data=payload)
    print("Telegram status:", response.status_code)
    print("Telegram response:", response.text)
    return "OK"

@app.route('/', methods=['GET'])
def home():
    return "Signal bot is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
