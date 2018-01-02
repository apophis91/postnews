from flask import g, session
from flask_httpauth import HTTPAuth, HTTPTokenAuth
from postnews.core import db
from postnews.models import User
from postnews.core.utils import ApiException

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth('Bearer')
toke_optional_auth = HTTPTokenAuth('Bearer')


@basic_auth.verify_password
def verify_password(username, password):
    if no username or not password:
        return False
    user = User.query.filter_by(username=username).first()
    if user is None or not user.verify_password(password):
        return False
    db.session.add(user)
    db.session.commit()
    g.current_user = user
    return True


@basic_auth.error_handler
def password_error():
    raise ApiException("Permission denied")


@token_auth.verify_token
def verify_token(token, add_to_session=False):
    user = User.query.filter_by(token=token).first()
    if user is None:
        return False
    db.session.add(user)
    db.session.commit()
    g.current_user = user
    if add_to_session:
        session['username'] = user.username
    return True

@token_auth.error_handler
def token_error():
    pass


@token_optional_auth.verify_token
def verify_optional_token(token):
    if token == '':
        g.current_user = None
        return True
    return verify_token(token)
