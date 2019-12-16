from flask import request, Flask, jsonify
from middleware import db
from routes.weapons import create_weapon, delete_weapon
from models.weapons import Weapons

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///story.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()




# WEAPONS #
###########
@app.route('/api/v1/weapon', methods=['GET', 'POST'])
def weapon():
    if request.method == 'POST':
        return create_weapon(request.get_json())
    if request.method == 'GET':
        return Weapons.all_weapons()
    return jsonify({"ll": "ll}"})
@app.route('/api/v1/weapon/<id>', methods=['DELETE'])
def select_weapon(id):
    if request.method == 'DELETE':
        return delete_weapon(id)
    return jsonify({"ll": "ll}"})

@app.route('/api/v1/admin/weapons', methods=['GET', 'POST'])
def get_weapons():
    # return get_weapons()
    return jsonify({'msg': 'lllll'}), 200


@app.route('/api/v1/admin/weapons/<id>', methods=['GET', 'DELETE', 'PUT'])
def select_weapons(id):
    return jsonify({'msg': 'm'}), 200


@app.route('/api/v1/items', methods=['GET', 'POST'])
def get_items():
    return jsonify({'msg': 'a'}), 200


@app.route('/api/v1/items/<id>', methods=['GET', 'PUT', 'DELETE'])
def select_items(id):
    return jsonify({'msg': 'd'}), 200


@app.route('/api/v1/area', methods=['GET', 'POST'])
def get_areas():
    return jsonify({'msg': 's'}), 200


@app.route('/api/v1/areas/<id>', methods=['GET', 'PUT', 'DELETE'])
def select_areas(id):
    return jsonify({'msg': 'ss'}), 200


