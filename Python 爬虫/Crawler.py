# coding:utf8
import urllib # 引入urllib库
url = "http://www.baidu.com"
content = urllib.urlopen(url) # 打开URL
html = content.read() # 读取页面内容
print html # 打印内容
