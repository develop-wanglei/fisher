# -*- coding: utf-8 -*-

"""
@author: 王磊

@File    : __init__.py.py 

@Created on: 2019/11/4 16:50
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
