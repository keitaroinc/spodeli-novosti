# -*- coding:utf-8 -*-
from wsgiref import simple_server

from app import spodelinovosti


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5001, spodelinovosti)
    httpd.serve_forever()
