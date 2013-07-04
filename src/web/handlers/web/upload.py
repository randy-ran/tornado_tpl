# -*- coding:utf-8 -*-
import tornado.gen
import tornado.options
import tornado.web
from base import BaseHandler
import time
import os.path, random, string
from comm.logger import log

class UploadHandler(BaseHandler):
    def get(self):
        self.write('upload file!')
        
    def post(self):
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        extension = os.path.splitext(original_fname)[1]
        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        final_filename= fname+extension
        directory = os.path.join(os.getcwd(),"uploads/")
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        output_file = open(directory + final_filename,'wb')
        output_file.write(file1['body'])
        
        self.finish("file" + final_filename + " is uploaded")