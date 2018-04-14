# coding=utf-8
from flask import Flask, jsonify

app = Flask('todoapp')

tasks = []


@app.route('/tasks')
def list():
    return jsonify(tasks)
