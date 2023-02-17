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

  data = response.json()
  cryptos =  data['data']
  price_list = []
  for key in cryptos.keys():
    price_list.append({
      'name': cryptos[key][0]['name'],
      'symbol': cryptos[key][0]['symbol'],
      'price': cryptos[key][0]['quote']['USD']['price']
    })
  return price_list


def send_message():
  data = get_price()
  message = ''
  for crypto in data:
    msg = f"Name: {crypto['name']}\nSymbol: {crypto['symbol']}\nPrice in USD: {crypto['price']}\n\n"
    message += msg
  bot.send_message(chat_id=223203746, text=message)
  time.sleep(10)  # Sleep for an hour

while True:
  send_message()