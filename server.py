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

@app.route('/startservice')
def start_services():
    os.system("/etc/init.d/volttron start")
    res = json.dumps({"status":200})
    return res

@app.route('/stopservice')
def stop_services():
    os.system("/etc/init.d/volttron stop")
    res = json.dumps({"status":200})
    return res


@app.route('/statusservice')
def status_services():
    print 'Status'
    result = os.system("/etc/init.d/volttron status")
    res = json.dumps({"status":200,"result":result})
    print res
    return res


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
