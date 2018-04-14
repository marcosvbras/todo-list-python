# coding=utf-8
from flask import Flask, jsonify

app = Flask('todoapp')

tasks = [
    {
        'id': 1, 'title': 'Título', 'description': 'Descrição', 'state': False
    }
]


@app.route('/tasks')
def list():
    return jsonify(tasks)
