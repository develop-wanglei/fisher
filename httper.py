# -*- coding: utf-8 -*-

"""
@author: 王磊

@File    : httper.py

@Created on: 2019/11/2 22:10
"""
import requests

class HTTP:
    @staticmethod
    def get(url,return_json=True):
        r = requests.get(url)
        if r.status_code !=200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 2000:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     return "404"