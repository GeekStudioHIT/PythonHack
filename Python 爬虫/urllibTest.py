# -*- coding: utf-8 -*-

import urllib.request

def easyTest() :
    response = urllib.request.urlopen("http://www.baidu.com")
    print(response.read())

def RequestTest():
    request = urllib.request.Request("http://www.baidu.com")
    response = urllib.request.urlopen(request)
    print(response.read())

def sendData():
    url = ""

if __name__ == '__main__':
    easyTest()
    RequestTest()