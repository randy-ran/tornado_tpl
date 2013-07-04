# -*- coding:utf-8 -*-
import orm.connection as db
from comm.logger import log
from sqlalchemy import *
import math
import time


def get_page_info(page_no,page_size,record_count):
    pageno=int(page_no)
    pos=page_size * (pageno-1)
    page_count=int(math.ceil(math.floor(record_count)/page_size))
    return (page_no,pos,record_count,page_count)

def add_user():
    session=db.NewSession()
    try:
        user = db.Users(username=time.time(),password='1234567',email='randy2@oubk.com')
        session.add(user)
        session.commit()
        return user.id
        #return user
    except Exception,ex:
        log.error(str(ex))
        print str(ex)
        return None
    finally:
        session.close()

def get_user_first():
    session=db.NewSession()
    try:
        user = session.query(db.Users).first()
        return user
    except Exception,ex:
        log.error(str(ex))
        return None
    finally:
        session.close()

def get_user_list(page_no,page_size):
    session=db.NewSession()
    try:
        if page_no is None:
            page_no=1
        lst_count=session.query(db.Users).count()
        page_info=get_page_info(page_no,page_size,lst_count)
        lst=session.query(db.Users).order_by(desc(db.Users.create_date)).slice(page_info[1],page_info[1]+page_size).all()
        return (page_info,lst)
    except Exception,ex:
        log.error(str(ex))
        return None
    finally:
        session.close()