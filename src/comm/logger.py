import logging
import time
import os
import config

#level CRITICAL  ERROR WARNING INFO DEBUG NOTSET

class fileLogger(object):
    """ The logger of the system. """
    def __init__(self, file, level="DEBUG"):
        """ Initialize the varialbes. """
        self.file = file
        self.level = getattr(logging, level)
        self.log = False
    
    def startLogging(self):
        """ Start the logger. """
        self.logger = logging.basicConfig(filename=self.file, level=self.level)
        self.log = True
        return True
    
    def stopLogging(self):
        """ Stop the logger. """
        self.log = False
    
    
    def logMessage(self, message, level):
        """ Log a message. """
        if self.log:
            getattr(logging, level.lower())('{0} {1}'.format(time.strftime('%d/%m/%Y %H:%M:%S', time.localtime()), message))
        else:
            pass
        
    def error(self,message):
        self.logMessage(message, 'ERROR') 
        
    def waring(self,message):
        self.logMessage(message, 'WARNING') 
        
    def info(self,message):
        self.logMessage(message, 'INFO')
        
    def debug(self,message):
        self.logMessage(message, 'DEBUG')

log = fileLogger(file=os.path.join(os.getcwd(),'log.txt'),level=config.log_level)