__author__ = 'Hernan Y.Ke'
import pymongo

client = pymongo.MongoClient('localhost', 27017)

testdb = client.test
testdb.person.drop()

#Add
person1=dict(name="ke",age=20)
testdb.person.insert(person1)
person = testdb.person.find_one()

if person:
    print('{} {}'.format(person['name'],person['age']) )

for db in client.database_names():
    print('{}'.format(db))
client.close()

