from flask import Flask, render_template, request, jsonify
import subprocess as sp
import json
from shlex import split
import os

app = Flask(__name__)


# Insert app.route for root  Directory to check Status for


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/startservice', methods=['POST'])
def start_services():
    os.system(". /home/pea/workspace/portal/start.sh")
    res = json.dumps({"status":200})
    return res

@app.route('/stopservice', methods=['POST'])
def stop_services():
    os.system(". /home/pea/workspace/portal/stop.sh")
    res = json.dumps({"status":200})
    return res


@app.route('/statusservice', methods=['POST'])
def status_services():
    print 'Status'
    result = os.system(". /home/pea/workspace/portal/status.sh")
    res = json.dumps({"status":200,"result":result})
    print res
    return res


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
