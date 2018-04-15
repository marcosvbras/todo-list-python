# coding=utf-8
import pymongo
import json
from bson import json_util
from bson.objectid import ObjectId


class TaskDAO:

    def __init__(self, database):
        self.database = database
        self.task_collection = self.database.task

    def create(self, data):
        task = {
            'title': data.get('title'),
            'description': data.get('description'),
            'done': False
        }

        inserted_id = self.task_collection.insert_one(task).inserted_id
        task = self.task_collection.find_one({ '_id': ObjectId(inserted_id) })

        return json.loads(json_util.dumps(task))

    def list(self):
        tasks = self.task_collection.find().sort('done', pymongo.ASCENDING)
        return json.loads(json_util.dumps(tasks))

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
