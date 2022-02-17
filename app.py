import requests
import json
import flask
from flask import *

app = Flask(__name__)

@app.route("/send")
def start():
    url = f"https://ingame.id.supercell.com/api/account/login"
    em = request.args.get("email")
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-US,en;q=0.5",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"ingame.id.supercell.com",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"none",
        "Sec-Fetch-User":"?1",
        "TE":"trailers",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }

    data = {
        "email":em,
        "rememeber":"true",
        "lang":"en",
        "game":"magic",
        "env":"prod"
    }
    req = requests.post(url,headers=headers,data=data).json()
    print(req)
    if req["ok"] == True:
        return "Done Send Code!"
    if req["ok"] == False:
        return "Not Linked With Clash :("
@app.route("/login")
def log():
    emaill = request.args.get("email")
    pin = request.args.get("pin")
    url2 = f"https://ingame.id.supercell.com/api/account/login.validate"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "ingame.id.supercell.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }
    data2 = {
        "email": emaill,
        "pin": int(pin)
    }
    reqq = requests.post(url2, headers=headers, data=data2).json()
    return reqq
if __name__ == '__main__':             
    app.run(debug=True)   
