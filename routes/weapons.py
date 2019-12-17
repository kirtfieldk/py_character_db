from flask import jsonify
from models.weapons import Weapons
from middleware import db


# Upgraded weapons +100 dmg


def upgrade_weapon(id):
    res = db.session.query(Weapons).filter_by(id=id).one()
    print(res.power)
    res.power += 100
    res.save_to_db()
    return jsonify({
        'data': res.to_json()
    })
