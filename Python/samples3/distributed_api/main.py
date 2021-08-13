#!/usr/bin/env python3

import json

# load data from json file
with open('data.txt', 'rb') as data_file:
    data_tasks = json.load(data_file)

def dump_data_to_file(file_name, data_tasks):
    with open(file_name, 'w') as f:
        json.dump(data_tasks, f, ensure_ascii=False, indent=4)

# flask
from flask import Flask, flash, redirect, render_template, request, session, abort, Response
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"

# Main table - displays all data with statuses
@app.route("/table/")
def show_table():
    return render_template('table.html',lst=data_tasks['tasks'])

# GET requests for taking tasks: GET /getapi/
@app.route('/get_task/', methods=['GET'])
def gettasks():
    worker_name = request.args.get("worker_name")
    not_solved_tasks = [ ts for ts in data_tasks['tasks'] if (ts['taskStatus'] == "Ready to start") ]
    task = not_solved_tasks[0]
    task['taskStatus'] = f"{worker_name} is working on it"
    dump_data_to_file('data.txt', data_tasks)
    response = { "task_to_solve": task['taskNumber'] }
    json_response=json.dumps(response)
    response=Response(json_response,content_type='application/json; charset=utf-8')
    response.headers.add('content-length',len(json_response))
    response.status_code=200
    return response

# POST api: POST /updateapi/
@app.route('/post_task/', methods = ['POST'])
def update_data():
    worker_name = request.args.get("worker_name")
    task = request.args.get("task")
    answer = request.args.get("answer")
    these_tasks = [ ts for ts in data_tasks['tasks'] if ts['taskNumber'] == task ]
    for task in these_tasks:
        task['taskResult'] = answer
        task['taskStatus'] = f"Solved by {worker_name}"
    dump_data_to_file('data.txt', data_tasks)
    json_response=json.dumps(answer)
    response=Response(json_response,content_type='application/json; charset=utf-8')
    response.headers.add('content-length',len(json_response))
    response.status_code=200
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
