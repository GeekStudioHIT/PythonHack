#Python 面向对象
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

- @property
	- 装饰器，改变函数调用方式为属性访问方式。
	- [参考](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820062641f3bcc60a4b164f8d91df476445697b9e000)
	
	``` Python
		class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

	s = Student();
	s.score = 60;
	print(s.score);
	s.score = 80;
	print(s.score);
	s.score = 1000;

	```
	