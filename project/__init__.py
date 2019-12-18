from flask import request, Flask, jsonify
from middleware import db
from models.weapons import Weapons
from models.area import Areas
from models.character import Character
from models.items import Items
from routes.generic import add, delete, get
from routes.weapons import upgrade_weapon
from routes.character import add_weapon, add_item
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///story.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

#ADMIN METHODS#
#################
@app.route('/api/v1/admin/weapon', methods=['POST'])
def weapon():
    if request.method == 'POST':
        return add(Weapons, request.get_json())
    return jsonify({"ll": "ll}"})


@app.route('/api/v1/admin/area/<id>', methods=['DELETE', 'GET'])
def admin_add_area(id):
    if request.method == 'DELETE':
        return delete(Areas, id)
    if request.method == 'GET':
        return Areas.find_by_id(id)
    return jsonify({'msg': 'm'}), 200


@app.route('/api/v1/admin/weapons/<id>', methods=['GET', 'DELETE', 'PUT'])
def select_weapon(id):
    if request.method == 'DELETE':
        return delete(Weapons, id)
    if request.method == 'PUT':
        return upgrade_weapon(id)
    if request.method == 'GET':
        return Weapons.find_by_id(id)
    return jsonify({"ll": "ll}"})


@app.route('/api/v1/admin/area', methods=['POST'])
def areas():
    if request.method == 'POST':
        return add(Areas, request.get_json())
    return jsonify({'msg': 'm'}), 200


@app.route('/api/v1/admin/items', methods=['GET', 'POST'])
def admin_items():
    if request.method == 'POST':
        return add(Items, request.get_json())
    if request.method == 'GET':
        return Items.all_item()
    return jsonify({"msg": "ed"})


@app.route('/api/v1/admin/items/<id>', methods=['GET', 'DELETE', 'PUT'])
def admin_item(id):
    if request.method == 'DELETE':
        return delete(Items, id)
    # if request.method == 'PUT':
    #     return upgrade_weapon(id)
    if request.method == 'GET':
        return Items.find_by_id(id)
    return jsonify({"ll": "ll}"})

#END OF ADMIN METHODS#
@app.route('/api/v1/weapons', methods=['GET'])
def get_weapons():
    if request.method == 'GET':
        return Weapons.all_weapons()
    return jsonify({'msg': 'lllll'}), 200


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


@app.route('/api/v1/character', methods=['POST', 'GET'])
def character():
    if request.method == 'POST':
        return add(Character, request.get_json())
    if request.method == 'GET':
        return Character.all_areas()


@app.route('/api/v1/<id>/addweapon', methods=['POST'])
def add_character_weapon(id):
    return add_weapon(id, request.get_json())


@app.route('/api/v1/<id>/additem', methods=['POST'])
def add_character_item(id):
    return add_item(id, request.get_json())
