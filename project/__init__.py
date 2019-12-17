from flask import request, Flask, jsonify
from middleware import db
from models.weapons import Weapons
from models.area import Areas
from routes.weapons import create_weapon, delete_weapon, upgrade_weapon
from routes.area import add_area, get_areas, delete_area

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
@app.route('/api/v1/admin/weapon', methods=['POST'])
def weapon():
    if request.method == 'POST':
        return create_weapon(request.get_json())
    return jsonify({"ll": "ll}"})


@app.route('/api/v1/weapon/<id>', methods=['DELETE', 'PUT'])
def select_weapon(id):
    if request.method == 'DELETE':
        return delete_weapon(id)
    if request.method == 'PUT':
        return upgrade_weapon(id)
    return jsonify({"ll": "ll}"})


@app.route('/api/v1/weapons', methods=['GET'])
def get_weapons():
    if request.method == 'GET':
        return Weapons.all_weapons()
    return jsonify({'msg': 'lllll'}), 200


@app.route('/api/v1/admin/weapons/<id>', methods=['GET', 'DELETE', 'PUT'])
def select_weapons(id):
    return jsonify({'msg': 'm'}), 200

####Admin Add Area####
@app.route('/api/v1/admin/area', methods=['POST'])
def areas():
    if request.method == 'POST':
        return add_area(request.get_json())
    return jsonify({'msg': 'm'}), 200


@app.route('/api/v1/admin/area/<id>', methods=['DELETE'])
def admin_add_area(id):
    if request.method == 'DELETE':
        return delete_area(id)
    return jsonify({'msg': 'm'}), 200


@app.route('/api/v1/area', methods=['GET'])
def get_areas():
    if request.method == 'GET':
        return Areas.all_areas()
    return jsonify({'msg': 'm'}), 200


@app.route('/api/v1/items', methods=['GET', 'POST'])
def get_items():
    return jsonify({'msg': 'a'}), 200


@app.route('/api/v1/items/<id>', methods=['GET', 'PUT', 'DELETE'])
def select_items(id):
    return jsonify({'msg': 'd'}), 200


@app.route('/api/v1/areas/<id>', methods=['GET', 'PUT', 'DELETE'])
def select_areas(id):
    return jsonify({'msg': 'ss'}), 200
