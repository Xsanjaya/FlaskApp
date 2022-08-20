import json
from flask import request
from flask_login import current_user, login_required
from models.User import User
from models import db
from utils import text2hash
from utils.auth_handler import AuthHandler

auth = AuthHandler()

def index():
    users = db.session.query(User).all()
    
    result = {
        "success" : True,
        "message" : "User All",
        "data"    : [ dict(user.list()) for user in users ]
    }
    return json.dumps(result)


def register():
    req = request.json
    name     = req['name']
    email    = req['email']
    password = auth.hash_password( req['password'] )
    token    = text2hash(email)

    try:
        user = User(name=name, email=email, password=password, token=token)
        
        db.session.add(user)
        db.session.commit()

        result = {
            "success" : True,
            "message" : "Create User",
            "data"    : [user.profile()]
        }

    except Exception as err:
        result = {
            "success" : False,
            "message" : "Create User Error",
            "data"    : [str(err)]
        }

    return json.dumps(result)


@login_required
def show(userId):
    if current_user.is_authenticated:
        resp = {"result": 200,
                "data": current_user.to_json()}
    else:                                                                                                                    
        resp = {"result": 401,
                "data": {"message": "user no login"}}

    return json.dumps(resp)

def update(userId):
    return 'success'


def destroy(userId):
    return 'success'