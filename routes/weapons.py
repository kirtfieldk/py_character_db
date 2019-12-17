from flask import jsonify
from models.weapons import Weapons
from middleware import db


def create_weapon(res):
    w1 = Weapons(res['name'], res['desc'], res['power'])
    w1.save_to_db()
    return w1.to_json(), 200


def delete_weapon(id):
    res = db.session.query(Weapons).filter_by(id=id).one()
    res.delete_db()
    return jsonify({
        'msg': 'success'
    }), 201

# Upgraded weapons +100 dmg


def upgrade_weapon(id):
    res = db.session.query(Weapons).filter_by(id=id).one()
    print(res.power)
    res.power += 100
    res.save_to_db()
    return jsonify({
        'data': res.to_json()
    })
