import requests
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Application, filters

TELEGRAM_BOT_TOKEN = '7325115939:AAHSS23Nev_PueQMOSSYv0YWoZQbroqMEuI'  # Replace with your actual token
chat_id = '@amirsoftwaretest'  # Replace with your numeric chat ID

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Привет! Я бот для отправки сообщений в ваш канал.')

def handle_message(update: Update, context: CallbackContext):
    message = update.message.text
    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(url, params=params)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")
        # Consider notifying the user about the error

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
