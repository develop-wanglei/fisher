# -*- coding: utf-8 -*-

"""
@author: 王磊

@File    : helper.py 

@Created on: 2019/11/2 22:04
"""
def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) ==13 and word.isdigit():
        isbn_or_key='isbn'
    short_word=word.replace('-','')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key