import warnings
from elasticsearch import Elasticsearch
warnings.filterwarnings('ignore')

import requests
res = requests.get('http://localhost:9200?pretty')
#print(res.content)

es = Elasticsearch('http://localhost:9200')

doc1 = {"city":"New Delhi", "country":"India"}
doc2 = {"city":"London", "country":"England"}
doc3 = {"city":"Los Angeles", "country":"USA"}

#Pour inserer doc1 dans l'Id 1 
es.index(index="cities", id=1, document=doc1)


es.index(index="cities", id=2, document=doc2)


es.index(index="cities", id=3, document=doc3)

response = es.index(index="cities", id=1, document=doc1)

res = es.search(index="cities", body={"query":{"match_all":{}}})
print(res)

print(es.search(index="cities", body={"query": {"regexp" : { "city" : "l.*n" }}}))