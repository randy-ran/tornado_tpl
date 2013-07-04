# -*- coding:utf-8 -*-
import orm.connection as db
from comm.logger import log
from sqlalchemy import *
import math
import time

def AddComments(dicItem):
    session = db.NewSession()
    try:
        model = db.Comments(dicItem)
        session.add(model)
        session.commit()
        return model.id
    except Exception,ex:
        log.error(str(ex))
        return None
    finally:
        session.close()

def GetCommentsList(pageNumber,pageSize):
    session=db.NewSession()
    try:
        if pageNumber is None:
            pageNumber=1
        pos=pageSize * (pageNumber-1)
        lst=session.query(db.Comments).order_by(desc(db.Comments.like)).slice(pos,pos+pageSize).all()
        return lst
    except Exception,ex:
        log.error(str(ex))
        return None
    finally:
        session.close()