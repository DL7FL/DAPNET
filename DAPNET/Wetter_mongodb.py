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
print(type(unwetterwarnunglist[0]))

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

# Mongo zu Panda df
data = pd.DataFrame(list(posts.find()))

print(posts.find_one('id'))

data[(data['sent'] > '2018-12-30T19:55:26+01:00') & (data['sent'] < '2019-03-25T16:40:38+01:00')]
data['sent'] = pd.to_datetime(data['sent'])

len(data['info'][0][0]['area'])
x = data['info']
data['anzahl'] = x.apply(lambda x: len(x[0]['area']))

data['anzahl']

len(data['anzahl'])
data.set_index('sent',inplace=True)
data.anzahl.plot(legend=True)
data.hist()

# Pie Chart
var= data.groupby(['anzahl']).sum().stack()
temp = var.unstack()
type(temp)
x_list = temp['anzahl']
label_list = temp.index
pyplot.axis("equal") # Kreisdiagramm rund gestaltet (sonst Standard: oval!)
pyplot.pie(x_list, labels=label_list, autopct="%1.1f%%")
pyplot.title('Aufteilung alle Mitarbeiter auf die Standorte nach Funktion')
pyplot.show()

