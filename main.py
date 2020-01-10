import os
import datetime
from flask import Flask, request
import json

app = Flask(__name__)
#Added this comment
@app.route('/', methods=['GET', 'POST'])
def generate_date():
    content = request.json
    name = content['name']
    now = datetime.datetime.now().strftime("%d-%M-%Y")
    output_statement = name.title() + ", today's date is " + now
    return_json = {'response': output_statement}
    return json.dumps(return_json)

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    content = request.json
    first_number = content['first_number']
    second_number = content['second_number']
    sum = first_number + second_number
    output = "The sum of " + str(first_number) + " and " + str(second_number) + " is " + str(sum)
    return_json = {'response': output}
    return json.dumps(return_json)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4000, threaded = True)
