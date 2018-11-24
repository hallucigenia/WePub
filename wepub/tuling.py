# -*- coding:utf-8 -*-
__author__ = 'fansly'

import os
import json
import requests

TULING_KEY = os.getenv('TULING_KEY')

def get_response(openid, msg):
    inputText = {'text': msg}
    userInfo = {'apiKey': TULING_KEY, 'userId': openid}
    perception = {'inputText': inputText}
    data = {'perception': perception, 'userInfo': userInfo}
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    response = requests.post(url=url, data=json.dumps(data))
    response.encoding = 'utf-8'
    result = response.json()
    answer = result['results'][0]['values']['text']
    return answer
