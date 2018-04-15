# coding=utf-8
import pymongo
from bson.objectid import ObjectId


class TaskDAO:

    def __init__(self, database):
        self.database = database
        self.tasks = self.database.tasks

    def create(self, task):
        pass

    def list(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
