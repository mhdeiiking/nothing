import requests
import uuid
from uuid import uuid4
import telebot
token = "5247038079:AAFVfl9iJnqRVxnBS08R7h9WVqWCwbIsgsQ"
bot = telebot.TeleBot(token)
url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
@bot.message_handler(commands=["start"])
def login(message):
    bot.send_message(message.chat.id,f"<strong>Hi ,\n== === ==\nWellcome to Login Instagram Bot\nSend User:pass Now !\n== === ==\nBy : @trprogram</strong>",parse_mode="html")
@bot.message_handler(func=lambda message:True)
def loginNow(message):
    msg = message.text
    bot.send_message(message.chat.id,"Wait ..")
    username = msg.split(":")[0]
    password = msg.split(":")[1]
    uid = str(uuid4())
    data = {
        "password":password,
        "username":username,
        "device_id":uid,
        "from_req":"false",
        '_csrftoken': 'missing',
        'login_attempt_countn': '0'
    }
    req = requests.post(url,headers=headers,data=data)
    if 'logged_in' in req.text:
        coc = req.cookies
        print(f"""\n{coc}\n""")
        id = coc["ds_user_id"]
        ses = coc["sessionid"]
        bot.send_message(message.chat.id,f"<strong>Done Login Sir .\nSession Id : {ses}\nID : {id}</strong>",parse_mode="html")
    if 'challenge_required' in req.text:
        bot.send_message(message.chat.id, f"<strong>Done Login Sir , But Secureid Account ..</strong>", parse_mode="html")
    if "bad_password" in req.text:
        bot.send_message(message.chat.id,f"<strong>Error Login Sir .</strong>",parse_mode="html")
bot.polling()
