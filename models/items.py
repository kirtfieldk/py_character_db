from flask import jsonify
from middleware import db
from models.errors import Errors

class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    area = db.relationship('Area', backref='area', lazy=True)
    desc = db.Column(db.String(250), nullable=False)
    character = db.relationship('Character', backref='character', lazy=True)

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def __repr__(self):
        return jsonify({
            'name': self.name,
            'desc': self.desc,
            'area': self.area[0].name,
            'character': self.chracter[0].name
        })

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()
    @classmethod
    def find_by_id(cls, id):
        try:
            item = cls.query.filter_by(id=id).first()
            return jsonify({
                'success': True,
                'count': 1,
                'data': item
            }), 200
        except AttributeError:
            return Errors('Unable To Find item', 404).to_json()