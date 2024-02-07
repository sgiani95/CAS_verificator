from flask import Flask, render_template, request

app = Flask(__name__)

# Load data from default_cas_list.csv into a dictionary
cas_list = {}
with open('default_cas_list.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cas_list[row[0]] = row[1]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_number():
    number = request.form['number']
    # Query the number in the cas_list dictionary
    result = cas_list.get(number, 'Number not found')
    return result

if __name__ == '__main__':
    app.run(debug=True)
