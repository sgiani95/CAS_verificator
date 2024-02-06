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

    # Your processing logic goes here...

    # Example processing logic:
    is_valid = validate_cas_number(cas_number)  # Assuming there's a validation function
    if is_valid:
        logging.info('CAS number is valid: %s', cas_number)
        # Additional processing if the CAS number is valid
    else:
        logging.info('Invalid CAS number: %s', cas_number)
        # Handle invalid CAS number case

    return jsonify({'message': 'CAS number processed successfully'})

# Example function for CAS number validation
def validate_cas_number(cas_number):
    # Validation logic goes here...
    # Return True if valid, False otherwise
    pass

if __name__ == '__main__':
    set_file_permissions()  # Call the function to set file permissions when the script is executed
    app.run(debug=True)
