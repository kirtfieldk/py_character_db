from flask import jsonify
from middleware import db
from models.errors import Errors


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    # area = db.relationship('Area', backref='areas', nullable=False)
    # item = db.relationship('Items', backref='items', lazy = True)
    # weapon = db.relationship('Weapons', backref='weapon', lazy=True)

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {
            'name': self.name,
            'desc': self.desc,
            # 'area': self.area[0].name,
            # 'character': list(map(lambda x: x, self.character)),
            # 'weapons': list(map(lambda x: x, self.weapon))
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
