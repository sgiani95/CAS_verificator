from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_number():
    number = request.form['number']
    # Placeholder response for now
    return 'Querying number: {}'.format(number)

if __name__ == '__main__':
    app.run(debug=True)
