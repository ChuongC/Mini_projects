import json

file = open("read.json","r")
data = json.load(file)
print(data["age"])
family_member = data["family_member"]
print(family_member[0])