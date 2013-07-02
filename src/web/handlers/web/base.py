# -*- coding:utf-8 -*-
import tornado.options
import tornado.web

from tornado.options import options
from tornado.database import Connection
import os

class BaseHandler(tornado.web.RequestHandler):
      pass