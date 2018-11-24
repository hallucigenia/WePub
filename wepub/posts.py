# -*- coding:utf-8 -*-

text_str = '''<xml>
                <ToUserName>![CDATA[%s]]</ToUserName>
                <FromUserName>![CDATA[%s]]</FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType>![CDATA[text]]</MsgType>
                <Content>![CDATA[%s]]</Content>
                </xml>'''

def reply_post(type):

    if type == 'text':
         return text_str
