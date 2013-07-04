# -*- coding:utf-8 -*-
from sqlalchemy import *
import config
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from lib2to3.pgen2.tokenize import Double
from sqlalchemy.engine.base import Engine
from sqlalchemy.dialects.mysql import *
import sqlalchemy.orm.session
import sqlalchemy.sql.expression
import time
from comm.logger import log

engine=create_engine("mysql://" + config.db_mysql_user + ":" + config.db_mysql_password +  "@" + config.db_mysql_server + "/" + config.db_mysql_dbname + "?charset=utf8",echo=config.server_log_toscreen)

Base = declarative_base()
def NewSession():
    return Session(bind=engine)

#metadata=MetaData()
#metadata.bind=engine
#tbl_client_summary=Table("tbl_client_summary",metadata,autoload=True)
#tbl_member=Table("tbl_member",metadata,autoload=True)

class Users(Base):
    __table_args__ = {
        'mysql_engine': 'MyISAM',
        'mysql_charset': 'utf8'
    }
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50),nullable=False,index=True,unique=True)
    password = Column(String(50),nullable=False)
    #phone_number = Column(String(50),default='')
    #member_level = Column(Integer,nullable=False,default=0)
    longitude = Column(Float,default=0)
    #latitude = Column(Float,default=0)
    fullname = Column(String(50),default='')
    age = Column(String(20),default='')
    #birthday = Column(Integer,default=0)
    create_date = Column(Integer,default=0)
    last_update = Column(Integer,default=0)
    email = Column(String(150),default='')

class Comments(Base):
    __table_args__ = {
        'mysql_engine': 'MyISAM',
        'mysql_charset': 'utf8'
    }
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    title = Column(String(255),nullable=False)
    like = Column(Integer,default=0)
    img_path = Column(String(255),nullable=False)
    status_id = Column(Integer,default=0)
    user_id = Column(Integer,default=0)
    comment_total = Column(Integer,default=0)
    create_date = Column(Integer,default=0)
    last_update = Column(Integer,default=0)
 
def InitDB():
    result=False
    while not result:
        try:
            Base.metadata.create_all(engine)
            result=True
        except Exception,ex:
            log.error(str(ex))
            log.debug('wait 5 seconds for retry...')
            time.sleep(5)       

def DbToProto(source,prototype):
    protoEntity=prototype()
    for item in prototype.DESCRIPTOR.fields:
        if hasattr(source, item.name):            
            setattr(protoEntity, item.name, getattr(source, item.name))
    return protoEntity

def CopyDbToProto(source,protoEntity):
    for item in type(protoEntity).DESCRIPTOR.fields:
        if hasattr(source, item.name):            
            setattr(protoEntity, item.name, getattr(source, item.name))

def ProtoToDb(prototype,dbEntity):
    for item in prototype.DESCRIPTOR.fields:
        if item.type!=item.TYPE_MESSAGE:
            if hasattr(dbEntity, item.name):
                setattr(dbEntity, item.name, getattr(prototype, item.name))
    return dbEntity
