# -*- coding: utf-8 -*-
import cookielib
import urllib2

url = "http://www.baidu.com"

print '第一种方法'
response = urllib2.urlopen(url)
print response.getcode()
print len(response.read())


print '第二种方法'
request = urllib2.Request(url)
# request.add_header('user-agent', 'Mozilla/5.0')
request.add_header('User-Agent', 'fake-client')
response1 = urllib2.urlopen(request)
print response1.getcode()
print response1.read()

print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response2 = urllib2.urlopen(url)
print response2.getcode()
print cj
print response2.read()