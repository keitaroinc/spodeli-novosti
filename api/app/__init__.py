# -*-coding:utf-8-*-
import falcon
import settings

# from .resources import *
from .resources import IndexResource
from .resources import SubscriberResource
from .resources import SendResource
from .db import RethinkDBFactory

indexResource = IndexResource()
subscriberResource = SubscriberResource()
sendResource = SendResource()

def create_app():
    db = RethinkDBFactory()
    db.create_table("subscribers")

    app = falcon.API()
    app.add_route('/', indexResource)
    app.add_route('/subscriber', subscriberResource)
    app.add_route('/subscriber/{id}', subscriberResource)
    app.add_route('/send', sendResource)

    return app

spodelinovosti = create_app()
