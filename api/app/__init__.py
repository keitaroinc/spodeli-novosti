# -*-coding:utf-8-*-
import falcon
import settings

# from .resources import *
from .resources import IndexResource
from .resources import SubscriberResource
from .resources import SendResource

indexResource = IndexResource()
subscriberResource = SubscriberResource()
sendResource = SendResource()

def create_app():
    app = falcon.API()

    app.add_route('/', indexResource)
    app.add_route('/subscriber', subscriberResource)
    app.add_route('/subscriber/{id}', subscriberResource)
    app.add_route('/send', sendResource)

    return app

spodelinovosti = create_app()
