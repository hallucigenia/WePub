# -*- coding:utf8 -*-
__author__ = 'fansly'

import hashlib
import time
import lxml
from lxml import etree
from reply import TextReply

from flask import Flask, request, make_response


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
        xml_data=request.data
        wx_xml=etree.fromstring(xml_data)
		# print(etree.tostring(wx_xml,pretty_print=True))
        wx_msgType=wx_xml.find('MsgType').text
        wx_fromUser=wx_xml.find('FromUserName').text
        wx_toUser=wx_xml.find('ToUserName').text

        if wx_msgType == 'text':
            wx_content=wx_xml.find('Content').text
            content=wx_content.encode('utf-8')
            print(content)
            if content == '天气':
                return TextReply(wx_fromUser,wx_toUser,'北京天气挺好的！').render()
            else:
                return TextReply(wx_fromUser,wx_toUser,wx_content).render()
        elif wx_msgType == 'image':
            return 'success'
        else:
            return 'success'

    if __name__ == '__main__':
        app.run()
