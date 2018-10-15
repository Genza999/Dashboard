import csv
import os
from pymongo import MongoClient

# client = MongoClient("localhost", 27017)
# db = client.csvtomongo

MdbURI = "mongodb://heroku_n22qp0w4:ie7fjj59dm14gap8hafjfae9eg@ds131963.mlab.com:31963/heroku_n22qp0w4"
client = MongoClient(MdbURI)
db = client['heroku_n22qp0w4']

coll = db.samplecoll
coll2 = db.samplecoll2


def get_data():
    with open('data1.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        coll.remove()
        next(csvreader)
        for row in csvreader:
            coll.insert({'School': row[2], 'Students': row[13]})
    data_list = []
    x = coll.find().sort('Students', 1)
    for doc in x:
        value_list = [doc['School'], doc['Students']]
        data_list.append(value_list)
    return data_list


def get_data_2():
    with open('data1.csv', 'r') as csvfile:
        csvreader2 = csv.reader(csvfile, delimiter=',')
        coll2.remove()
        next(csvreader2)
        for row in csvreader2:
            coll2.insert({'District': row[0]})
    data_list1 = []
    for doc in coll2.aggregate([{"$unwind": "$District"}, {"$sortByCount": "$District"}]):
        value_list1 = [doc['_id'], doc['count']]
        data_list1.append(value_list1)
    return data_list1
