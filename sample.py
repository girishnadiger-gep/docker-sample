from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def sample():
    content = request.json
    name = content['name']
    final_name = "Hey, " + name
    return json.dumps({'response':final_name})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5500, threaded = True, debug = True)
