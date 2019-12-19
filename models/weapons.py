from flask import jsonify
from middleware import db
from models.errors import Errors


class Weapons(db.Model):
    __tablename__ = 'weapons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    desc = db.Column(db.String(250), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))

    def to_json(self):
        return {
            'name': self.name,
            'desc': self.desc,
            'power': self.power
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        try:
            weapon = cls.query.filter_by(id=id).first()
            return jsonify({
                'success': True,
                'count': 1,
                'data': weapon.to_json()
            }), 200
        except AttributeError:
            return Errors('Unable To Find weapon', 404).to_json()

    @classmethod
    def all_weapons(cls):
        try:
            weapon = cls.query.all()
            return jsonify({
                'success': True,
                'count': len(weapon),
                'data': list(map(lambda x: x.to_json(), weapon))
            }), 200
        except AttributeError:
            return Errors('Unable To Find weapon', 404).to_json()
