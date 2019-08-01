# Jupiter Datei
import json
import requests
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client.warnungsdb
collection = db.warnungcollection
posts = db.posts

url = "https://warnung.bund.de/bbk.dwd/unwetter.json"
unwetterjson = requests.get(url)
unwetterwarnunglist = json.loads(unwetterjson.text)

print(type(unwetterwarnunglist))

for unwetterwarnung in unwetterwarnunglist:
    post_id = posts.insert_one(unwetterwarnung).inserted_id
    print(post_id)
	
	
# Abfragen und Auswertung / Visualisierung

# Documente zählen

posts.count_documents({})

posts.count_documents({"msgType":"Alert"})
for doc in posts.find():
    print(set(doc['sender']))
	
{i['info'][0]['senderName'] for i in posts.find()}

len({i['sent'] for i in posts.find()})


