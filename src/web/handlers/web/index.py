# -*- coding:utf-8 -*-
import tornado.options
import tornado.web
from base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        #self.redirect('/admin')
        self.write("Hello, world")