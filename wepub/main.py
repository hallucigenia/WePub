# -*- coding:utf8 -*-
__author__ = 'fansly'

import re
import json
import time
import hashlib
import requests

from flask import Flask, request, make_response
from tuling import get_response
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
            response = make_response(schostr)
            response.headers['content-type'] = 'text'
            return response

    else:
        xml = ET.fromstring(request.data)
        toUser = xml.find('ToUserName').text
        fromUser = xml.find('FromUserName').text
        msgType = xml.find("MsgType").text
        createTime = xml.find("CreateTime")

        if msgType == 'text':
            content=xml.find('Content').text
            return reply_text(fromUser, toUser, get_response(fromUser, content))
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
