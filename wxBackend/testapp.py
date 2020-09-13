import tornado.ioloop
import tornado.web
import hashlib
import web
import requests
import time
import os

import recieve
import generateResponseText as grt


# ----------------------------------------------------------------
# 基本配置
# ----------------------------------------------------------------
PORT = 8000
APPID = 'wx63a775ce1f72fbcd'  # 公众号ID
APPSECRET = '9f9e596b13d6d5439e0b11b00ec9c415'  # 公众号密钥
REDIRECT_URI = 'http://c2m.tq.yhlcps.com/backend/getUserInfo'  # 回调URL，需要在公众号中配置
SCOPE = 'snsapi_userinfo'  # 弹出授权页面，可通过openid拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# Handlers
# ----------------------------------------------------------------
class Hello(tornado.web.RequestHandler):
    def get(self):
        res = self.get_query_arguments('drop')
        print(res)
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/backend/hello", Hello),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    print(f'server start at {PORT}......')
    tornado.ioloop.IOLoop.current().start()
