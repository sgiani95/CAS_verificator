from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verify', methods=['GET', 'POST'])  # Allow both GET and POST requests to /verify
def verify_cas_number():
    if request.method == 'POST':
        cas_number = request.json.get('cas_number')
        if cas_number:
            # Perform CAS number verification logic here
            # Example: check if the CAS number is present in a database
            # Replace the following lines with your verification logic
            if cas_number == '12345-67-8':
                return jsonify({'message': 'CAS number is valid'}), 200
            else:
                return jsonify({'message': 'CAS number is not valid'}), 404
        else:
            return jsonify({'error': 'No CAS number provided'}), 400
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
