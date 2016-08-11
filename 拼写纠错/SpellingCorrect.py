import re, collections

def words(text):
    return re.findall('[a-z]+', text.lower())

relink = '<a href="(.*)">(.*)</a>'
info = '<a href="http://www.baidu.com">baidu</a>'
cinfo = re.findall(relink,info)
print(cinfo)