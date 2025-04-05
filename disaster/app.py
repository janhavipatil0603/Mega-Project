from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('disaster_relief.db')
    conn.row_factory = sqlite3.Row  # Allows column names to be accessed as keys
    return conn

# Route to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    aadhar_number = data['aadhar_number']
    name = data['name']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO users (aadhar_number, name) VALUES (?, ?)', 
                   (aadhar_number, name))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User added successfully!"}), 201

# Route to add a distributor
@app.route('/add_distributor', methods=['POST'])
def add_distributor():
    data = request.get_json()
    name = data['name']
    distributor_status = data['distributor_status']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO distributors (name, distributor_status) VALUES (?, ?)', 
                   (name, distributor_status))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Distributor added successfully!"}), 201

# Route to add a response (user verification)
@app.route('/add_response', methods=['POST'])
def add_response():
    data = request.get_json()
    user_id = data['user_id']
    distributor_id = data['distributor_id']
    resources_received = data['resources_received']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO responses (user_id, distributor_id, resources_received) VALUES (?, ?, ?)', 
                   (user_id, distributor_id, resources_received))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Response added successfully!"}), 201

# Route to get all responses
@app.route('/get_responses', methods=['GET'])
def get_responses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM responses')
    responses = cursor.fetchall()
    conn.close()
    
    # Convert query result into a list of dictionaries
    responses_list = [dict(response) for response in responses]
    
    return jsonify(responses_list)

if __name__ == "__main__":
    app.run(debug=True)
