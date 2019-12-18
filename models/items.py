from flask import jsonify
from middleware import db
from models.errors import Errors


class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    # area = db.Column(db.Integer, db.ForeignKey('areas.id'))
    desc = db.Column(db.String(250), nullable=False)
    character = db.Column(db.Integer, db.ForeignKey('character.id'))

    def to_json(self):
        return{
            'name': self.name,
            'desc': self.desc,
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
            item = cls.query.filter_by(id=id).first()
            return jsonify({
                'success': True,
                'count': 1,
                'data': item.to_json()
            }), 200
        except AttributeError:
            return Errors('Unable To Find item', 404).to_json()

    @classmethod
    def all_item(cls):
        try:
            items = cls.query.all()
            return jsonify({
                'success': True,
                'count': len(items),
                'data': list(map(lambda x: x.to_json(), items))
            }), 200
        except AttributeError:
            return Errors('Unable To Find items', 404).to_json()
