#Python 深拷贝和浅拷贝 总结
- 浅拷贝
	- 切片
	- list() 工厂函数
	- copy.copy()
- 深拷贝
	- copy.deepcopy()
- 对一个对象进行浅拷贝，只是拷贝了这个对象的引用。
- 字符串、数字和其他『原子』类型的对象，当对其进行『拷贝』之时，会重新新建一个对象。
- 示例
	- 浅拷贝

		```
		>>> a = ['a', 123, []]
		>>> b = a[:]
		>>> b[2].append(123)
		>>> b
		['a', 123, [123]]
		>>> a
		['a', 123, [123]]
		```
	- 深拷贝
	
		```
		>>> a = ['a', 123, []]
		>>> import copy
		>>> b = copy.deepcopy(a)
		>>> b[2].append(123)
		>>> b
		['a', 123, [123]]
		>>> a
		['a', 123, []]
		```

