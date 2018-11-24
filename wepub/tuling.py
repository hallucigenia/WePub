# -*- coding:utf-8 -*-
__author__ = 'fansly'

import os
import json
import requests

TULING_KEY = os.getenv('TULING_KEY')


def get_response(openid, msg):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    dat = {
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": TULING_KEY,
            "userId": openid
        }
    }
    dat = json.dumps(dat)
    r = requests.post(api, data=dat).json()

    mesage = r['results'][0]['values']['text']
    print(r['results'][0]['values']['text'])
    return mesage
