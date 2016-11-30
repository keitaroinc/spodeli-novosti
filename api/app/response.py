# -*- coding:utf-8 -*-
import json


def ok(ret=None):
    return json.dumps({
        "title": "OK",
        "description": ret
    })


def bad_request(info=""):
    return json.dumps({
        "title": "Bad Request",
        "description": info
    })
