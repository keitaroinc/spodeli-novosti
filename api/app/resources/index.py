# -*- coding:utf-8 -*-
import falcon


class IndexResource(object):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Сподели Новости'
