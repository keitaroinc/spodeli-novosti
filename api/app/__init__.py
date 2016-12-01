# -*-coding:utf-8-*-
import falcon
import settings

# from .resources import *
from .resources import IndexResource
from .resources import SubscriberResource
from .resources import SendResource
from .db import RethinkDBFactory
from .middleware import CORSMiddleware

indexResource = IndexResource()
subscriberResource = SubscriberResource()
sendResource = SendResource()
corsMiddleware = CORSMiddleware()

def create_app():
    db = RethinkDBFactory()
    db.create_table("subscribers")

    app = falcon.API(middleware=[corsMiddleware])
    app.add_route('/', indexResource)
    app.add_route('/subscriber', subscriberResource)
    app.add_route('/subscriber/{id}', subscriberResource)
    app.add_route('/send', sendResource)

    return app

spodelinovosti = create_app()
