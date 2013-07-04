# -*- coding:utf-8 -*-
import tornado.gen
import tornado.options
import tornado.web
from base import BaseHandler
import time
from comm.logger import log

class DevGenHandler(BaseHandler):
    @tornado.gen.engine
    def check_invite(self, invite_code, callback):
        time.sleep(1)
        log.error('2')
        callback(True)

    #@tornado.web.asynchronous
    #@tornado.gen.engine
    def get(self):
        if self.current_user:
            self.redirect('/')
            return
        log.error('1')
        #invite_code = self.get_argument('invite', None)
        is_valid_invite = True # yield tornado.gen.Task(self.check_invite, invite_code)
        log.error('3')
        if is_valid_invite:
            item = {}
            item['Success']=True
            item['num']=200
            item['Message']="test 中文 json"
            item['time']= int(time.time())

            dic=[]
            dic.append(item)
            dic.append(item)
            
            self.write(tornado.escape.json_encode(dic))
            #self.render("gen1.html")
        else:
            self.render("gen2.html")