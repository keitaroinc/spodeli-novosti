# -*-coding:utf-8-*-
from worker.components.email.tasks import send_mail
import json
from falcon import HTTPBadRequest
from app.helpers.schema_validator import validate_newsletter
from app.response import ok
from app.db import RethinkDBClient

class SendResource(object):
    def __init__(self, *args, **kwargs):
        pass

    def on_post(self, req, resp):
        """Send newsletter to all subscribers"""
        try:
            raw_json = req.stream.read()
            result = json.loads(raw_json, encoding='utf-8')
            validate_newsletter(result)
        except Exception as e:
            raise HTTPBadRequest('Invalid JSON', e.message)
        else:
            try:
                with RethinkDBClient() as rdb:
                    subscribers = rdb.get("subscribers", )

                map(lambda s: send_mail.delay(s["email"],
                                              result["subject"],
                                              result["body"]), subscribers)
                resp.body = ok(ret='Sent to worker for delivery')
            except Exception as e:
                raise HTTPBadRequest()
