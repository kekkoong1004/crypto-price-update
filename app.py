import os
from dotenv import load_dotenv
load_dotenv()
import telebot
import requests
import time

telegram_API = os.getenv('telegram_API')
crypto_API = os.getenv('CRYPTO_API')
bot = telebot.TeleBot(telegram_API)

def get_price():
  headers = {'X-CMC_PRO_API_KEY': crypto_API, 'Accepts': 'application/json'}

  url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

  parameters = {'symbol': 'ADA,ALGO,APE,BTC,DOGE,DOT,ETH,SD,SHIB,SOL,TON,XRP'}

  response = requests.get(url, headers=headers, params=parameters)

    #   bitcoin_price = data['data']['1']['quote']['USD']['price']
    #   eth_price = data['data']['1027']['quote']['USD']['price']
    #   price_list = {
    #     'BTC_price' : data['data']['1']['quote']['USD']['price'],
    #     'Eth_price' : data['data']['1027']['quote']['USD']['price']
    #   }

  data = response.json()
  price = data['data']
  return price

# print(get_price())


@bot.message_handler()
def send_message(message):
  while True:
    bot.send_message(chat_id=message.chat.id, text=f'Bitcoin price now is USD ${telegram_API}')
    time.sleep(3600)  # Sleep for an hour

bot.polling()