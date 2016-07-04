import json

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 将对象转化为可序列化的字典
def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__}
    # d = {}
    d.update(vars(obj))
    return d

classes = {
    'Point' : Point
}

# 将 JSON 字符串反序列化为对象
def unserialize_object(d):
    clsname = d.pop('__classname__')
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d
# test
p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
print(s, type(s))

a = json.loads(s, object_hook=unserialize_object)
print(a.__dict__)
