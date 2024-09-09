from flask import Flask, request, jsonify, render_template
import requests

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    title = request.json.get('title')
    description = request.json.get('description')

    if title and description:
        send_to_telegram(title, description)
        return jsonify({'status': 'Message sent to Telegram'})
    else:
        return jsonify({'error': 'Title and description must be provided'}), 400


def send_to_telegram(title, description):
    message = f'<b>{title}</b>\n\n{description}'
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': CHAT_ID,
        'parse_mode': 'HTML',
        'text': message
    }
    requests.post(url, params=params)

if __name__ == '__main__':
    app.run(debug=True)

