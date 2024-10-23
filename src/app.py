import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure('Jackson')

# jackson_family.add_member({
#     'first_name': 'John',
#     'age': 33,
#     'lucky_numbers': [7, 13, 22]
# })
# jackson_family.add_member({
#     'first_name': 'Jane',
#     'age': 35,
#     'lucky_numbers': [10, 14, 3]
# })
# jackson_family.add_member({
#     'first_name': 'Jimmy',
#     'age': 5,
#     'lucky_numbers': [1]
# })

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    if members:
        return jsonify(members), 200
    else:
        return jsonify({'error': 'Not found'}), 404

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    response_body = {
        'id': member['id'],
        'age': member['age'],
        'first_name': member['first_name'],
        'lucky_numbers': member['lucky_numbers']
    }
    return jsonify(response_body), 200
    
@app.route('/member', methods=['POST'])
def create_member():
    member = request.json
    if not all(key in member for key in ['first_name', 'age', 'lucky_numbers']):
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        jackson_family.add_member(member)
        return jsonify({'message': 'Member created successfully', 'member': member}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# @app.route('/member/<int:id>', methods=['DELETE'])
# def delete_single_member(id):
#     member = jackson_family.get_member(id)
 
#     if member:
#         jackson_family.delete_member(id)
#         return jsonify({'done': True}), 200
#     else:
#         return jsonify({'error': 'Member not found'}), 404
    
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_family_member(id):
    deleted_member = jackson_family.delete_member(id)

    if deleted_member: 
        return jsonify({'done': True}), 200
    else: 
        return jsonify ({'Error': 'Member not found'}), 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
