from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

# Function to set file permissions for app.log
def set_file_permissions():
    log_file_path = 'app.log'  # Specify the path to the log file
    permissions = 0o644  # Define the desired permissions (read and write for owner, read-only for others)
    os.chmod(log_file_path, permissions)  # Set the permissions of the log file

# Configure logging to output to a file
logging.basicConfig(filename='app.log', level=logging.INFO)

# Route for processing CAS numbers
@app.route('/process', methods=['POST'])
def process_cas_number():
    cas_number = request.json.get('cas_number')
    logging.info('Processing CAS number: %s', cas_number)

    # Verify the CAS number
    is_valid = verify_cas_number(cas_number)

    if is_valid:
        logging.info('CAS number is valid: %s', cas_number)
        response = {'message': f'CAS number {cas_number} is valid'}
    else:
        logging.info('Invalid CAS number: %s', cas_number)
        response = {'message': f'CAS number {cas_number} is invalid'}

    return jsonify(response)

# Function to verify CAS number
def verify_cas_number(cas_number):
    # Example: Check if the CAS number has the correct format (for demonstration purposes)
    if len(cas_number) == 9:  # Example: CAS number must be 9 characters long
        return True
    else:
        return False

if __name__ == '__main__':
    set_file_permissions()  # Call the function to set file permissions when the script is executed
    app.run(debug=True)
