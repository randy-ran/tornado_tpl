import hashlib
import config
try:
    import json
except ImportError:
    import simplejson as json

def hash_password(password):
    salt = "xl8moEeQSNa0t8WUzBM4VQ==" #config['password_salt']
    return hashlib.sha512(password + salt).hexdigest()


def _json_date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def to_json(obj):
    return json.dumps(obj, default=_json_date_handler)

def from_json(json_str):
    return json.loads(json_str)