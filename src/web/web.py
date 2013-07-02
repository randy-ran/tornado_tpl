# -*- coding:utf-8 -*-
import config
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import logging
from tornado.options import define, options
from handlers.web.register import RegisterHandler
#from handlers.admin.member import MemberHandler
from handlers.web.index import IndexHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/register", RegisterHandler),
            #(r"/admin/member_list(?:(?:/?)$|/)(\d+)?", MemberHandler),
        ]
        
        settings = dict(
            cookie_secret="12oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
#            xsrf_cookies=True,
#            ui_modules= {"Post": PostModule},
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
   
def Main():
    print 'starting web server...'
    tornado.options.parse_command_line()
    logging.getLogger().setLevel(logging.DEBUG)
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(config.web_port)
    #init_environment()
    print 'wait for connecting...'
    tornado.ioloop.IOLoop.instance().start()
