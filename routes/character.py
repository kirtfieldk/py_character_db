from flask import jsonify
from middleware import db
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
