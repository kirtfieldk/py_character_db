from flask import jsonify
from sqlalchemy.orm.exc import NoResultFound
from middleware import db
from models.area import Areas
from models.errors import Errors


def add_area(res):
    try:
        a1 = Areas(res['name'], res['desc'])
        a1.save_to_db()
        return jsonify({
            'msg': 'Success',
            'data': a1.to_json()
        })
    except KeyError:
        return Errors("Required Keys Missing", 400).to_json()


def get_areas():
    res = db.session.query(Areas).all()
    return jsonify({
        'msg': 'Success',
        'count': res.length,
        "data": list(map(lambda x: x.to_json, res))
    })


def delete_area(id):
    try:
        res = db.session.query(Areas).filter_by(id=id).one()
        res.delete_db()
        return jsonify({
            "msg": "Success"
        }), 200
    except NoResultFound:
        return Errors("Unable to find area", 400).to_json()
