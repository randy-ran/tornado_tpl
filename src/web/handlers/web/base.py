# -*- coding:utf-8 -*-
import tornado.options
import tornado.web

from tornado.options import options
from tornado.database import Connection
import os
from web.helper import to_json
from pprint import pprint

USER_COOKIE_NAME = "user"

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_json = self.get_secure_cookie(USER_COOKIE_NAME)
        if user_json:
            return tornado.escape.json_decode(user_json)
        else:
            return None
    
    def get_current_username(self,key='id'):
        user_json = self.get_current_user()
        if user_json:
            return user_json[key]
        else:
            return None
    
    def login_user(self, user, remember=False):
        expires = None
        if remember:
            expires = 90

        self.set_secure_cookie(USER_COOKIE_NAME,tornado.escape.json_encode(user), expires_days=expires)

    def logout_user(self):
        self.clear_cookie(USER_COOKIE_NAME)
        self.redirect('/')

    def get_current_user_async(self, callback):
        user = self.get_secure_cookie(USER_COOKIE_NAME)
        callback(user)