from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock target list, replace with your actual target list
target_list = ["target1", "target2", "target3"]

def validate_cas_number(cas_number):
    # Implement CAS number validation logic using regex
    # Return True if valid, False otherwise
    pass

def match_cas_numbers(cas_numbers):
    results = {}
    for cas_number in cas_numbers:
        if validate_cas_number(cas_number):
            matches = [target for target in target_list if cas_number in target]
            results[cas_number] = matches if matches else "Not found"
        else:
            results[cas_number] = "Invalid CAS number"
    return results

@app.route('/check', methods=['POST'])
def check_cas_numbers():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    cas_numbers = data.get('cas_numbers')
    if not cas_numbers:
        return jsonify({'error': 'CAS numbers not provided'}), 400

    results = match_cas_numbers(cas_numbers)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)  # Remove debug=True when deploying to production
