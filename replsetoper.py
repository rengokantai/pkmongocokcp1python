__author__ = 'Hernan Y.Ke'
from pymongo import  MongoClient
import time

client = MongoClient(['localhost:27000','localhost:27001','localohst:27002'],replicaSet='replSet')
collection = client.test.person
collection.drop()

collection.insert_one(dict(name="Ke",age=10))
for x in range(5):
    try:
        print(collection.find_one())
    except Exception as e:
        pass
    time.sleep(6)