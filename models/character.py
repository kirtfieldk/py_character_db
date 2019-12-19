from flask import jsonify
from middleware import db
from models.errors import Errors


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    item = db.relationship('Items', backref='objs', lazy=True)
    weapon = db.relationship('Weapons', backref='owner', lazy=True)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def to_json(self):
        return {
            'name': self.name,
            'password': self.password,
            'weapons': list(map(lambda x: x.to_json(), self.weapon)),
            'items': list(map(lambda x: x.to_json(), self.item)),
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
            area = cls.query.filter_by(id=id).first()
            return jsonify({
                'success': True,
                'count': len(area),
                'data': area.to_json()
            }), 200
        except AttributeError:
            return Errors('Unable To Find area', 404).to_json()

    @classmethod
    def all_areas(cls):
        try:
            area = cls.query.all()
            return jsonify({
                'success': True,
                'count': len(area),
                'data': list(map(lambda x: x.to_json(), area))
            }), 200
        except AttributeError:
            return Errors('Unable To Find area', 404).to_json()
