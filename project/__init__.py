from flask import requests, Flask, jsonify
from middleware import db

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///story.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/api/v1/admin/weapons', methods=['GET', 'POST'])
def get_weapons():

    return jsonify({'msg': 'success'}), 200


@app.route('/api/v1/admin/weapons/<id>', methods=['GET', 'DELETE', 'PUT'])
def select_weapons(id):
    return jsonify({'msg': 'success'}), 200


@app.route('/api/v1/items', methods=['GET', 'POST'])
def get_items():
    return jsonify({'msg': 'success'}), 200


@app.route('/api/v1/items/<id>', methods=['GET', 'PUT', 'DELETE'])
def select_items(id):
    return jsonify({'msg': 'success'}), 200


@app.route('/api/v1/area', methods=['GET', 'POST'])
def get_areas():
    return jsonify({'msg': 'success'}), 200


@app.route('/api/v1/areas/<id>', methods=['GET', 'PUT', 'DELETE'])
def select_areas(id):
    return jsonify({'msg': 'success'}), 200
