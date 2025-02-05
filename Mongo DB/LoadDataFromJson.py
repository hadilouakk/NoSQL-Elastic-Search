import json
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Mets l'URL de ton MongoDB
db = client.mydb  # Remplace par le nom de ta base de données
collection = db.mycollection  # Remplace par le nom de ta collection


with open("accounts.json", "r") as file:
    data = json.load(file)



    result = collection.insert_many(data)
    print(" Inserted data with the following IDs :", result.inserted_ids)

##Create an Index 
index_name ="city_index"
collection.create_index("adress.city", name=index_name)
print("Inserted Index",index_name )
##Find accounts with name of city

city = "Bradshawborough"
results = collection.find({"address.city": city})

for result in results:
    print(result)

##Find accounts with a balance
min_balance = 30000
results = collection.find({"balance": {"$gt": min_balance}})

for result in results:
    print(result)

    


pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(f"{result['_id']}: {result['total_balance']}")
