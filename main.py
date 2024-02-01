from os import system 
import os,sys,time,requests
import random, telebot, os
from time import sleep
from telebot import types
import requests
from os import system 
import os,sys,time,requests
import pyrogram
import random
from pyrogram import client
from pyrogram import *
from pyrogram.types import *
import requests
from time import sleep
from pyrogram.raw import functions
from pyrogram.errors import FloodWait ,BadRequest
start_pin = False
clickscount = 0
idd = ""
token = input("[+]Enter bot token : ")
admin = input("[+]Enter your id : ")
with open("info.txt","a") as login:
    login.write(f"{token}\n{admin}")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['admin'])
def send_tool(message):
    global idd , start_pin , admin
    keyo = telebot.types.InlineKeyboardMarkup(row_width=1)
    if start_pin == False and str(message.from_user.id) in admin:
        itembtn1 = telebot.types.InlineKeyboardButton('Add account', callback_data="Add")#done
        itembtn2 = telebot.types.InlineKeyboardButton('Delete All account',callback_data="Dacc")#done
        itembtn3 = telebot.types.InlineKeyboardButton('Click count',callback_data="clickss")#done
        itembtn4 = telebot.types.InlineKeyboardButton('Pin',callback_data="pinn")#done
        status_new = telebot.types.InlineKeyboardButton(f'pinnid : {idd}',callback_data="aaa")#done
        status_ch = telebot.types.InlineKeyboardButton(f'Send Number file',callback_data="sendd")#done
        itembtn5 = telebot.types.InlineKeyboardButton('Start',callback_data="ss")
        itembtn6 = telebot.types.InlineKeyboardButton('Stop',callback_data="st")#tofe x
        itembtn100 = telebot.types.InlineKeyboardButton(f'❌ STOPPED ❌',callback_data="c14dq")
        keyo.add(itembtn1,itembtn2,itembtn3,itembtn4,status_new,status_ch,itembtn5,itembtn6,itembtn100)#(py_iq)
        bot.send_message(message.chat.id, "- admin 💳 " , reply_markup = keyo)
    elif start_pin == True and str(message.from_user.id) in admin:
        itembtn1 = telebot.types.InlineKeyboardButton('Add account', callback_data="Add")#done
        itembtn2 = telebot.types.InlineKeyboardButton('Delete All account',callback_data="Dacc")#done
        itembtn3 = telebot.types.InlineKeyboardButton('Click count',callback_data="clickss")#done
        itembtn4 = telebot.types.InlineKeyboardButton('Pin',callback_data="pinn")#done
        status_new = telebot.types.InlineKeyboardButton(f'pinnid : {idd}',callback_data="aaa")#done
        status_ch = telebot.types.InlineKeyboardButton(f'Send Number file',callback_data="sendd")#done
        itembtn5 = telebot.types.InlineKeyboardButton('Start',callback_data="ss")
        itembtn6 = telebot.types.InlineKeyboardButton('Stop',callback_data="st")#tofe x
        itembtn100 = telebot.types.InlineKeyboardButton(f'✅ STARTED ✅',callback_data="c14dq")
        keyo.add(itembtn1,itembtn2,itembtn3,itembtn4,status_new,status_ch,itembtn5,itembtn6,itembtn100)#(py_iq)
        bot.send_message(message.chat.id, "- admin 💳 " , reply_markup = keyo)
@bot.callback_query_handler(func=lambda call: True )
def answer(call):
    global idd , start_pin , clickscount
    try:
        if call.data == "ss":
            start_pin = True
            bot.send_message(call.message.chat.id,"Done ~ Start")
            system("php run.php")
        if call.data == "st":
            start_pin = False
            bot.send_message(call.message.chat.id,"Done ~ Stop")
            system("php stop.php")
        if call.data == "Add" :
            botbod = bot.send_message(call.message.chat.id,"Send the Session (Onle one Session)",parse_mode="MARKDOWN")
            bot.register_next_step_handler(botbod,addd)
        if call.data == "Dacc":
            Deleta_acc = bot.send_message(call.message.chat.id,"Are u sure? Y/n ??",parse_mode="MARKDOWN")
            bot.register_next_step_handler(Deleta_acc,deleteeee)
        if call.data == "pinn":
            pin_user = bot.send_message(call.message.chat.id,"Send the username without @",parse_mode="MARKDOWN")
            bot.register_next_step_handler(pin_user,pino)
        if call.data == "sendd":
            try:
                document = open('Number.txt', 'rb')
                w = len(open("Number.txt").readlines())
                bot.send_document(call.message.chat.id,document,caption=f"- The Number  : {w}")
            except:
                bot.send_document(call.message.chat.id,document,caption=f"- The Number  : 0")
        if call.data == "clickss":
            bot.send_message(call.message.chat.id,f"*_Click Count_* : * {clickscount} *",parse_mode="MARKDOWN")
                    
    except: 
        pass
def pino(message):
    global idd
    cid = message.chat.id
    req = requests.get(f"https://t.me/{message.text}").text
    if "tgme_username_link" not in req:
        bot.send_message(message.chat.id,"This username is in use !!")
    else:
        idd = message.text
        with open("Number.txt","w+") as a:
            a.write(str(idd))
        bot.send_message(message.chat.id,"Done ~ /admin")
def deleteeee(message):
    cid = message.chat.id
    suree = message.text
    if suree == "Y":
        bot.send_message(message.chat.id,"Done")
        os.system("rm Number.txt")
    elif suree == "n":
        bot.send_message(message.chat.id,"Done")
    else :
        pass
def addd(message):
    cid = message.chat.id
    num_new= message.text
    with open("Number.txt","a") as kl :
        kl.write(num_new+"\n")
        kl.close()
    bot.send_message(message.chat.id,"Done")
bot.polling(none_stop=True)

# >Done<
# - User : @{mk}
# - Clicks : {clickscount}
# - Saved : Account
# - Number : {app.get_me().phone_number}
# ===========================
# * Mustafa ~ @Py_Iq