import pymongo
client = pymongo.MongoClient("mongodb+srv://sharad:jimmy0311@cluster0.em1lh8p.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sharad",
    "email" : "sharad1989@hotmail.com",
    "surname" : "chauhan"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )