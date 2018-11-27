import os
import sys

preurl = "mongodb://localhost:27017/"

class BaseConfig(object):
    DEBUG = False
    WELCOME_TEXT = "感谢关注MONO工作室[可爱]\n我可以为您提供各种生活服务\n"


class DevelopmentConfig(BaseConfig):
   MONGO_URI = preurl + 'mongo-dev.db'


class ProductionConfig(BaseConfig):
   MONGO_URI = preurl + 'mongo.db'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}