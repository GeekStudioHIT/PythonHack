#Python 面向对象
##Demo
- 重写 dict 中的 `__setattr__`、`__getattr__`、`__delattr__`、`__call__`

	``` Python
	# -*- coding:utf-8 -*-
class storage(dict):
    def __setattr__(self, key, value):
        self[key] = value
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            return None
    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            return None
    def __call__(self, key):
        try:
            return self[key]
        except KeyError, k:
            return None

	s = storage()
	s.name = "hello" # __setattr__
	print(s("name")) # __call__
	print(s["name"]) # dict 默认行为
	print(s.name) # __getattr__
	del s.name # __delattr__
	print(s.name)
	print(s("name"))
	print(s["name"])

	```
	- `__call__` 可以使对象像函数一样调用。

- [`__str__` 和 `__repr__`](http://blog.csdn.net/yyt8yyt8/article/details/7030416)

