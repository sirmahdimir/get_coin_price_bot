import telebot
import requests

# create a new bot in botfather and place the token here:
TOKEN = 'THE BOT TOKEN'
bot = telebot.TeleBot(TOKEN)
# pick a api url that response your desire symbol price (for ex. BTCUSDT):
URL = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

@bot.message_handler(commands=['start'])
def send_wellcome(message):
    bot.reply_to(message, '⚡wellcoeme to GCP-BOT!⚡\nplease just enter a symbol and we will show you the price\nfor example:\n👉 BTCUSDT 👈')

@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = str(message.text)
    symbol = symbol.upper()

    response = requests.get(f'https://www.binance.com/api/v3/ticker/price?symbol={symbol}')# use a f_str to replace your desire symbol with default symbol

    if response.status_code == 200:
        data = response.json()
        price = data['price']
        bot.reply_to(message, f"✅ {data['symbol']} price is:\n💲{price}💲")

    elif response.status_code == 400:
        bot.reply_to(message, '❗The Symbol is not found ❗')

    else:
        bot.reply_to(message, '❌A mistake has occurred❌')


bot.infinity_polling()