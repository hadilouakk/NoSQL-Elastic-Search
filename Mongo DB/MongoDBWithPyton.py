from pymongo import MongoClient
client =MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

##To Insert

#  document ={"name": "John Doe", "email":"john.doe@exemple.com", "age":30}
#  result =collection.insert_one(document)
#  print("Inserted document ID:", result.inserted_id)

# #To Read 
#  query ={"name": "John Doe"}
#  document = collection.find_one(query)
#  print(document)

# #To update

#  query = {"name":"John"}
#  update= {"$set":{"age":31}}
#  result = collection.update_one(query, update)
#  print ("Modified document count:" ,result.modified_count)

#To Delete
# query ={"name":"John Doe"}
# result= collection.delete_one(query)
# print ("Deleted document count:", result.deleted_count)


query = {
    "$and": [
        {"age": {"$gt": 25}},
        {"email": {"$regex": "@example\.com$"}}
    ]
}
documents = collection.find(query)

for doc in documents:
    print(doc)
