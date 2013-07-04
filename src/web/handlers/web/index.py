# -*- coding:utf-8 -*-
import tornado.options
import tornado.web
from base import BaseHandler
import web.models.UserModel as m
import orm.connection as db
from comm.logger import log

class IndexHandler(BaseHandler):
    def get(self):
        #db.InitDB()
        db_user = m.get_user_first()
        if self.current_user:
            return self.render("authenticated/index.html",user=db_user)
        else:
            return self.render("index.html",user=db_user)