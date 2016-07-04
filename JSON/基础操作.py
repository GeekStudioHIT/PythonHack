import json

data = {
    "name" : "Bob",
    "age" : "19"
}

json_str = json.dumps(data)
data = json.loads(json_str)
print(type(json_str), type(data))