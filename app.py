from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to store CAS numbers and their attributes
# You can replace this with your actual database or data structure
CAS_DATABASE = {
    '12345-67-8': {'attribute': 'flammable'},
    '7732-18-5': {'attribute': 'not flammable'}
}

@app.route('/verify', methods=['POST'])
def verify_cas_number():
    if request.method == 'POST':
        cas_number = request.json.get('cas_number')
        print("Received CAS number:", cas_number)  # Debug statement

        if cas_number:
            # Check if the provided CAS number exists in the database
            if cas_number in CAS_DATABASE:
                print("CAS number found in database:", cas_number)  # Debug statement
                return jsonify({'message': f'CAS number {cas_number} is found in the database. Attribute: {CAS_DATABASE[cas_number]["attribute"]}'}), 200
            else:
                print("CAS number not found in database:", cas_number)  # Debug statement
                return jsonify({'message': f'CAS number {cas_number} is not found in the database'}), 404
        else:
            return jsonify({'error': 'No CAS number provided'}), 400
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
