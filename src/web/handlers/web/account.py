# -*- coding:utf-8 -*-
import tornado.gen
import tornado.options
import tornado.web
from base import BaseHandler
import forms
from web.helper import hash_password
import web.models.UserModel as m
import orm.connection as db
from pprint import pprint
from comm.logger import log

class LoginHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        form = forms.LoginForm()
        form.remember.data=True
        return self.render("login.html",form=form)

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        if self.current_user:
            self.redirect('/')
            return
        
        form = forms.LoginForm(self)
        if not form.validate():
            self.render("login.html", form=form)
            return
        
        email = form.email.data
        password = form.password.data #hash_password(form.password.data)
        if email=='randy@oubk.com' and password=='123456':
            user_dic = {'id': 1,'screen_name': form.email.data}
            self.login_user(user_dic, form.remember.data)
            self.redirect('/')
        else:
            form.errors['invalid'] = True
        
        self.render("login.html", form=form)

class LogoutHandler(BaseHandler):
    def get(self):
        self.logout_user()

class RegisterHandler(BaseHandler):
    def get(self):
        form = forms.RegistrationForm()
        form.email.data="my@oubk.com"
        form.birth_date_month.data=4
        form.subscribe.data=True
        return self.render("register.html",form=form)
    
    @tornado.gen.engine
    def check_invite(self, invite_code, callback):
        callback(False)
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
    
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self, *args, **kwargs):
        if self.current_user:
            self.redirect('/')
            return
        
        invite_code = self.get_argument('invite', None)
        is_valid_invite = yield tornado.gen.Task(self.check_invite, invite_code)
        
        if not is_valid_invite:
            self.redirect('/login')
            return
        
        form = forms.RegistrationForm(self)
        if not form.validate():
            self.render("register.html", form=form)
            return
        
        id =1# m.add_member()
        #self.write("Hello,%s" % form.email.data)
        self.redirect('/%s' % id)
        #password_hash = helper.hash_password(form.password.data)