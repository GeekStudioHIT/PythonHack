# Python 基础
- 判断变量数据类型
	- type()
	
##作用域
- > 声明适用的程序的范围被称为了声明的作用域。在一个过程中，如果名字在过程的声明之内，它的出现即为过程的局部变量；否则的话，出现即为非局部。——《龙书》

- global，明确地引用一个已命名的全局变量。

- 静态嵌套域

	``` Python
	def foo():
		m = 3
		def bar():
		    n = 4
		    print(m + n)
		print m
		bar()
		
	foo()
	```
	m 既不是全局，又不是局部。为静态作用域。
	
##闭包
如果在一个内部函数里，对在外部作用域（但不是全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）。定义在外部函数内的但由内部函数引用或者使用的变量被称为自由变量。

``` Python
def counter(start_at=0): 
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]
    return incr
```

##装饰器
- 举例

	``` Python
	from time import ctime, sleep

	def tsfunc(func):
		def wrappedFunc():
			print ('[%s] %s() called' % (ctime(), func.__name__))
			return func()
		return wrappedFunc

	@tsfunc
	def foo():
		pass

	foo()
	sleep(4)

	for i in range(2):
		sleep(1)
		foo()
	```
装饰器就是一个函数，调这个函数之前会先调这个装饰器。

##生成器
- 带有 `yield` 的函数被称为生成器（generator）。
- 简单举例

 	``` Python
 	def simpleGen():
	yield 1
	yield 2

	# myG = simpleGen()
	# myG.__next__()
	# myG.__next__()

	for eachItem in simpleGen():
		print(eachItem)
 	```
- [Python yield 使用浅析](http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)

##迭代器
从根本上说，迭代器就是有一个 next() 方法的对象。

 ``` Python
>>> a = [1, 2, 3]
>>> a = iter(a)
>>> a.__next__()
1
>>> a.__next__()
2
>>> a.__next__()
3
>>> a.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
 ```