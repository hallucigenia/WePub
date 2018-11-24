# -*- coding:utf8 -*-

import hashlib
import time
import posts

from flask import Flask, request, make_response
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    return "hello world!"

@app.route('/wechat_api/', methods = ['GET', 'POST'] )
def wechat():
    if request.method == 'GET':
        token = 'fancy'
        # your token in here
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        s = [timestamp,nonce,token]
        s.sort()
        # 字典排序
        s = ''.join(s)
        if hashlib.sha1(s.encode('utf-8')).hexdigest() == signature:
            # 对接受的请求转换为utf-8后进行sha1加密
            response = make_response(echostr)
            response.headers['content-type'] = 'text'
            return response

    if request.method == 'POST':
        xmldata = request.args
        xml_rec = et.fromstring(xmldata)

        ToUser = xml_rec.find('ToUserName').text
        FromUser = xml_rec.find('FromUserName').text
        MsgType = xml_rec.find('MsgType').text
        Content = xml_rec.find('Content').text
        MsgId = xml_rec.find('MsgId').text

        return post.reply_post(MsgType) % (fromUser, ToUser, int(time()), Content)

if __name__ == '__main__'
    app.run()
