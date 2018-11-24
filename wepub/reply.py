# -*- coding:utf-8 -*-

import time
class TextReply(object):
	TEMPLATE=u"""
	<xml>
    <ToUserName><![CDATA[{target}]]></ToUserName>
    <FromUserName><![CDATA[{source}]]></FromUserName>
    <CreateTime>{time}</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[{content}]]></Content>
    </xml>
	"""

	def __init__(self, target,source,content):
		self.target=target
		self.source=source
		self.content=content
		self.time=int(time.time())

	def render(self):
		return TextReply.TEMPLATE.format(target=self.target,source=self.source,time=self.time,content=self.content)
