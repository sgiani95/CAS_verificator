from flask import Flask, request, jsonify

app = Flask(__name__)

# Your other routes and functions go here...

if __name__ == '__main__':
    app.run(debug=True)
