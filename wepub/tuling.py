import requests
import json

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
            "apiKey": '81dd4902254b4714a8acaa2685da1afd',
            "userId": openid
        }
    }
    dat = json.dumps(dat)
    r = requests.post(api, data=dat).json()

    mesage = r['results'][0]['values']['text']
    print(r['results'][0]['values']['text'])
    return mesage
