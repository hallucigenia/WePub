# -*- coding: utf-8 -*-
__author__ = 'fansly'


def wechat_response(data):
    xml = ET.fromstring(request.data)
    toUser = xml.find('ToUserName').text
    fromUser = xml.find('FromUserName').text
    msgType = xml.find("MsgType").text

    if msgType == 'text':
        content = xml.find('Content').text
        return reply_text(
            fromUser, toUser, get_response(
                fromUser, content))
    else:
        return reply_text(fromUser, toUser, "嗯？我听不太懂")



def reply_text(to_user, from_user, content):
    reply = """
    <xml><ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    <FuncFlag>0</FuncFlag></xml>
    """
    response = make_response(reply % (to_user, from_user,
                                      str(int(time.time())), content))
    response.content_type = 'application/xml'
    return response