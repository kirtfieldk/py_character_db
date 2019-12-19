# GENERIC ADD DELETE GET Functions
from flask import jsonify
from sqlalchemy.orm.exc import NoResultFound
from middleware import db
from models.errors import Errors
from models.character import Character
from models.items import Items
from models.weapons import Weapons


def add(table, res):
    try:
        if table is Items:
            print("Calles")
            o1 = table(res['name'], res['desc'])
        if table is Character:
            o1 = table(res['name'])
        if table is Weapons:
            o1 = table(res['name'], res['desc'], res['power'])
        o1.save_to_db()
        return jsonify({
            'msg': 'success',
            'data': o1.to_json()
        })
    except KeyError:
        return Errors("Required Keys Missing", 400).to_json()


def delete(table, id):
    try:
        res = db.session.query(table).filter_by(id=id).one()
        res.delete_db()
        return jsonify({
            "msg": "Success"
        }), 200
    except NoResultFound:
        return Errors("Unable to find area", 400).to_json()


def get(table):
    res = db.session.query(table).all()
    return jsonify({
        'msg': 'Success',
        'count': res.length,
        "data": list(map(lambda x: x.to_json(), res))
    })
