import json

with open('questions.json') as file:
    data = json.load(file)

for d in range(0,len(data["results"])):
    print d,".Question:",data["results"][d]["question"]

#print data
