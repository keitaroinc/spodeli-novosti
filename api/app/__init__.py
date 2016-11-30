# -*-coding:utf-8-*-
import falcon
import settings

# from .resources import *
from .resources import IndexResource
from .resources import SubscriberResource
from .resources import NewsResource

indexResource = IndexResource()
subscriberResource = SubscriberResource()
newsResource = NewsResource()


def create_app():
    app = falcon.API()

    app.add_route('/', indexResource)
    app.add_route('/subscriber', subscriberResource)
    app.add_route('/subscriber/{id}', subscriberResource)

    return app

spodelinovosti = create_app()
