# -*- coding: utf-8 -*-

"""
@author: 王磊

@File    : book.py 

@Created on: 2019/11/4 16:51
"""
from flask import Blueprint, jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook

web=Blueprint('web',__name__)

@web.route("/book/search/<q>/<page>")
def search(q,page):
    isbn_or_key=is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result= YuShuBook.search_by_isbn(q)
    else:
        result= YuShuBook.search_by_keyword(q)
    return jsonify(result)