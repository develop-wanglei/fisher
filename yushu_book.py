# -*- coding: utf-8 -*-

"""
@author: 王磊

@File    : yushu_book.py 

@Created on: 2019/11/4 17:12
"""
from httper import HTTP


class YuShuBook:

    isbn_url='http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/serach?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls,isbn):
        url=cls.isbn_url.format(isbn)
        result= HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls,keyword,count=15,start=0):
        url =cls.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result




