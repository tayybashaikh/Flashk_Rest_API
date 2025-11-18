from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory users list
users = []


# 1. GET - Get all user
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200



# 2. POST - Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added successfully"}), 201



# 3. PUT - Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id < 0 or user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    users[user_id] = data
    return jsonify({"message": "User updated successfully"}), 200



# 4. DELETE - Delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id < 0 or user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    
    users.pop(user_id)
    return jsonify({"message": "User deleted successfully"}), 200


# Run the app
if __name__ == '__main__':
    app.run(debug=True)