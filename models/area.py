from flask import jsonify
from middleware import db
from models.errors import Errors

class Areas(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    desc = db.Column(db.String(250), nullable=False)
    character = db.relationship('Characters', backref='character', lazy=True)
    item = db.relationship('Items', backref='items', lazy = True)
    weapon = db.relationship('Weapons', backref='weapon', lazy=True)

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def to_json(self):
        return {
            'name': self.name,
            'desc': self.desc,
            'character': list(map(lambda x: x, self.character)),
            'weapons': list(map(lambda x: x, self.weapon))
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
                'count': 1,
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
                'count': 1,
                'data': list(map(lambda x: x.to_json(), area))
            }), 200
        except AttributeError:
            return Errors('Unable To Find area', 404).to_json()   