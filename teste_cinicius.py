from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017")
db = conn["testando"]
coll = db["vinicius"]

doc = {
    "nome": "Vinicius",
    "idade": 23
}

coll.insert_one(doc)