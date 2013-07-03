from datetime import datetime
from handlers.web.base import Model

class User(Model):
    _id = None
    created = datetime.utcnow()
    email = None
    password_hash = None
    invite_code = None
    facebook_id = None
    twitter_id = None
    screen_name = None
    birth_date = None
    zipcode = None
    gender = 0
    opt_in = False