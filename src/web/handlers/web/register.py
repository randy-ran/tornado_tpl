# -*- coding:utf-8 -*-
import tornado.gen
import tornado.options
import tornado.web
from base import BaseHandler
import forms

class RegisterHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        form = forms.RegistrationForm()
        form.email.data="my@oubk.com"
        form.birth_date_month.data=4
        form.subscribe.data=True
        return self.render("register.html",form=form)
    
    #@tornado.gen.engine
    def check_invite(self, invite_code, callback):
        callback(True)
        #self.write("check_invite,%s" % invite_code)
        '''
        if self.settings['invite_only']:
            if invite_code:
                #Check database to see if invite code is valid.
                spec = {'code': invite_code}
                invite_doc = yield self._invite_check(spec) #motor.Op(self.db.invites.find_one, spec)
                if invite_doc:
                    #invite = Invite(invite_doc)
                    #if invite.redeemed_count < invite.total_count or invite.total_count < 0:
                    #Make sure that there are invites left, -1 = unlimited
                    callback(True)

            callback(False)
        else:
            callback(True)
        '''
    
    def _invite_check(self,spec):
        return True
    
    #@tornado.gen.engine
    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        if self.current_user:
            self.redirect('/')
            return
        
        #invite_code = self.get_argument('invite', None)
        #is_valid_invite = yield tornado.gen.Task(self.check_invite, invite_code)
        
        #if not is_valid_invite:
        #    self.redirect('/register')
        #    return
        
        form = forms.RegistrationForm(self)
        if not form.validate():
            self.render("register.html", form=form)
            return
        
        self.write("Hello,%s" % form.email.data)
        #password_hash = helper.hash_password(form.password.data)
        
        