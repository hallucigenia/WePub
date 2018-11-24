# -*- coding:utf8 -*-
__author__ = 'fansly'

import re
import json
import time
import hashlib
import requests

from flask import Flask, request, make_response

import xml.etree.ElementTree as ET

WX_TOKEN='fancy'

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/wechat_api/', methods = ['GET', 'POST'] )
def wechat():
    if request.method == 'GET':
        token = WX_TOKEN
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
            response.headers['content-type'] = 'text'
            return make_response(echostr)

    else:
        xml = ET.fromstring(request.data)
        toUser = xml.find('ToUserName').text
        fromUser = xml.find('FromUserName').text
        msgType = xml.find("MsgType").text
        createTime = xml.find("CreateTime")

        if msgType == 'text':
            content=xml.find('Content').text
            content=content.encode('utf-8')
            return reply_text(fromUser, toUser, reply(fromUser, content))
        else:
            return reply_text(fromUser, toUser, "嗯？我听不太懂")


def reply_text(to_user, from_user, content):
    return """
    <xml>
        <ToUserName><![CDATA[{}]]></ToUserName>
        <FromUserName><![CDATA[{}]]></FromUserName>
        <CreateTime>{}</CreateTime>
        <MsgType><![CDATA]></MsgType>
        <Content><![CDATA[{}]]></Content>
    </xml>
    """.format(to_user, from_user, int(time.time() * 1000), content)


def reply(openid, msg):
    data = {"key": "81dd4902254b4714a8acaa2685da1afd", "info": msg, "userid": openid}
    r = requests.post('http://openapi.tuling123.com/openapi/api', data)
    text = json.loads(r.text)
    return text['text'].encode('utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
