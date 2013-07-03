# -*- coding:utf-8 -*-
import tornado.gen
import tornado.options
import tornado.web
from base import BaseHandler
import forms
from web.helper import hash_password

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