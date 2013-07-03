# -*- coding:utf-8 -*-
import tornado.options
import tornado.web
from base import BaseHandler
from pprint import pprint

class IndexHandler(BaseHandler):
    def get(self):
        if self.current_user:
            return self.render("authenticated/index.html")
        else:
            return self.render("index.html")