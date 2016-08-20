# -*- coding: utf-8 -*-

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm";
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)