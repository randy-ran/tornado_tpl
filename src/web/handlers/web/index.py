# -*- coding:utf-8 -*-
import tornado.options
import tornado.web
from base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        #self.redirect('/admin')
        if self.current_user:
            return self.render("authenticated/index.html")
        else:
            return self.render("index.html")