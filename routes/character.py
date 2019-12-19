from flask import jsonify
from flask_login import current_user, logout_user, login_user
from middleware import db, bycrpt
from models.character import Character
from models.weapons import Weapons
from models.items import Items
from models.errors import Errors


def add_weapon(id, req):
    try:
        res = db.session.query(Character).filter_by(id=id).one()
        w1 = Weapons(name=req['name'], desc=req['desc'],
                     power=req['power'], owner=res)
        w1.save_to_db()
        return jsonify({
            'msg': "success",
            'data': res.to_json()
        })
    except KeyError:
        return Errors("Missing Key Values", 400).to_json()


def add_item(id, req):
    try:
        res = db.session.query(Character).filter_by(id=id).one()
        w1 = Items(name=req['name'], desc=req['desc'], objs=res)
        w1.save_to_db()
        return jsonify({
            'msg': "success",
            'data': res.to_json()
        })
    except KeyError:
        return Errors("Missing Key Values", 400).to_json()


def create_character(req):
    try:
        if current_user.is_authenticated:
            return Errors("Already logedin", 400).to_json()
        password = bycrpt.generate_password_hash(
            req['password']).decode('utf-8')
        admin = Character(name=req['username'], password=password)
        admin.save_to_db()
        return admin.to_json()
    except KeyError:
        return Errors("Username Already Taken", 400).to_json()


def login(username, password):
    if current_user.is_authenticated:
        return Errors("Already logedin", 400).to_json()
    user = db.session.query(Character).filter_by(name=username).first()
    if user and bycrpt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'success': True, "msg": "Login {}".format(username)})
    return Errors("Could Not Login", 404).to_json()


def logout():
    logout_user()
    return jsonify({"msg": "Successful logout"})
