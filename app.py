from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

def check_cas_number(cas_number):
    with open('default_cas_list.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['CAS Number'] == cas_number:
                return row['Attributes']  # Return the attributes of the CAS number if found
    return None  # Return None if the CAS number is not found

@app.route('/verify', methods=['POST'])
def verify_cas_number():
    cas_number = request.json.get('cas_number')
    if cas_number:
        attributes = check_cas_number(cas_number)
        if attributes:
            return jsonify({'message': f'CAS number {cas_number} is present. Attributes: {attributes}'}), 200
        else:
            return jsonify({'message': f'CAS number {cas_number} is not present.'}), 404
    else:
        return jsonify({'error': 'No CAS number provided.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
