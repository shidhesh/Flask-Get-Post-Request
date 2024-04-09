#Post-request_Data_Get_Post.py  this file use for post request update atomatic

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = [
        { "id":1, "name":"Sidheshwar", "city":"Pune", "Edu":"BCS" },
        {"id":2, "name":"Rohit", "city":"Mumbai", "Edu":"BTech" }
        ]

# Home route
@app.route('/')
def home():
    return 'Welcome to my Flask API!'

# Endpoint to get all data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Endpoint to get a specific item by ID
@app.route('/data/<int:id>', methods=['GET'])
def get_item(id):
    item = next((item for item in data if item['id'] == id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# Endpoint to add a new item
@app.route('/data', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify({'message': 'Item added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
