import json

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d;

s = '{"name": "Bob", "age": "18"}'
data = json.loads(s, object_hook=JSONObject)
print(data.name)