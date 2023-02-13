import os
import telebot
import yfinance as yf
# the bot is called @etherscan_bot
# the channel is called @etherscan_channel
# the bot is hosted on a raspberry pi
import requests
import json
import time
from telepot.loop import MessageLoop


API_KEY =  '6153820587:AAEqcniVriPTaZCgfM7CaMVxm2qiW2vG4YM'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def greet(message):
  bot.reply_to(message, "L investigates contracts for B/S taxes, liquidity, MP, and whether it is a Hp or not.")

#Trick client into 
@bot.message_handler(commands=['safe'])
def greet(message):
  bot.reply_to(message, "Fetching Request....")

@bot.message_handler(commands=['trend'])
def greet(message):
  bot.reply_to(message, "Fetching Request....")

@bot.message_handler(commands=['eth'])
def greet(message):
  bot.reply_to(message, "Fetching Request....")


# Trick ends

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if command == '/hi':
        bot.sendMessage(chat_id, str("hi there"))
    elif command == '/time':
        bot.sendMessage(chat_id, str(time.ctime()))
    elif command == '/price':
        response = requests.get("https://api.coinmarketcap.com/v1/ticker/ethereum/")
        response = json.loads(response.text)
        bot.sendMessage(chat_id, str(response[0]['price_usd']))
    elif command == '/supply':
        response = requests.get("https://api.etherscan.io/api?module=stats&action=ethsupply&apikey=UXK21DC853UCRHKRP4XXGHEGHEXY5JJ2WI")
        response = json.loads(response.text)
        bot.sendMessage(chat_id, str(response['result']))
    elif command == '/hashrate':
        response = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_hashrate&apikey=UXK21DC853UCRHKRP4XXGHEGHEXY5JJ2WI")
        response = json.loads(response.text)
        bot.sendMessage(chat_id, str(response['result']))
    elif command == '/difficulty':
        response = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag=latest&boolean=true&apikey=UXK21DC853UCRHKRP4XXGHEGHEXY5JJ2WI")
        response = json.loads(response.text)
        bot.sendMessage(chat_id, str(response['result']['difficulty']))
    elif command == '/block':
        response = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=UXK21DC853UCRHKRP4XXGHEGHEXY5JJ2WI")
        response = json.loads(response.text)
        bot.sendMessage(chat_id, str(response['result']))
    elif command == '/uncle':
        response = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag=latest&boolean=true&apikey=UXK21DC853UCRHKRP4XXGHEGHEXY5JJ2WI")
        response = json.loads(response.text)
        bot.sendMessage(chat_id, str(response['result']['uncles']))
    elif command == '/gasprice':
        response = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey=UXK21DC853UCRHKRP4XXGHEGHEXY5JJ2WI")
        response = json.loads(response.text)
        bot.sendMessage(chat_id, str(response['result']))
    elif command == '/tx':
        response = requests.get("https://api.etherscan.io/api?module=proxy&action=eth__getBlockByNumber&tag=latest&boolean=true&apikey=UXK21DC853UCRHKRP4XXGHEGHEXY5JJ2WI")
bot.polling()