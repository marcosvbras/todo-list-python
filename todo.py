# coding=utf-8
from flask import Flask, jsonify, request, abort
from tasks import TaskDAO
import pymongo

app = Flask('todoapp')
client = pymongo.MongoClient('mongodb://localhost')
database = client.todo_list
tasks_dao = TaskDAO(database)
tasks = []


@app.route('/tasks')
def list():
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def create():
    data = request.json
    title = data.get('title', None)
    description = data.get('description', None)

    if not title or not description:
        abort(400)

    data['id'] = 1
    data['done'] = False
    tasks.append(data)
    return jsonify(data), 201
