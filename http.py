# -*- coding: utf-8 -*-

"""
@author: 王磊

@File    : http.py 

@Created on: 2019/11/2 22:10
"""
import requests
class HTTP:
    def get(self,url,return_json=True):
        r = requests.get(url)
        if return_json:
            return r.json()
        else:
            return r.text