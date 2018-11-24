# -*- coding:utf8 -*-
import hashlib
import time
from flask import Flask, request, make_response
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.debug = True

@app.route("/otherpage/")
def otherpage():
    return "otherpage!"

@app.route("/")
def hello():
    return "main page!"

@app.route('/wechat_api/', methods = ['GET', 'POST'] )
def wechat_auth():
    if request.method == 'GET':
        token = 'fancy'
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        s = [timestamp,nonce,token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            response = make_response(echostr)
            response.headers['content-type'] = 'text'
            return response
