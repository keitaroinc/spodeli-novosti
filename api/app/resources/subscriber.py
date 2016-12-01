# -*-coding:utf-8-*-
from rethinkdb.errors import RqlError
import json
from falcon import HTTPBadRequest, HTTP_400
from falcon.util.uri import parse_query_string
from app.db import RethinkResource
from app.helpers.schema_validator import validate_subscriber
from app.response import ok, bad_request
from app.db import RethinkDBClient


class SubscriberResource(object):
    def __init__(self, *args, **kwargs):
        self._table_name = "subscribers"

    def on_get(self, req, resp, id=None, offset=0, limit=200):
        """Get all subscribers if no query args. If email in query args
        then return subscriber matching email. If id in route return that
        object."""
        args = parse_query_string(req.query_string)
        email = args.get('email', None)
        if args.get('limit'):
            try:
                limit = int(args.get('limit'))
                if limit > 200:
                    raise ValueError('Limit can not exceed 200')
            except ValueError as e:
                raise HTTPBadRequest('Invalid value for limit', e.message)

        if args.get('offset'):
            try:
                offset = int(args.get('offset'))
            except ValueError as e:
                raise HTTPBadRequest('Invalid value for limit', e.message)

        try:
            rdb = RethinkDBClient()
            if id:
                resp.body = rdb.get(self._table_name, 'id', id)
            elif email:
                resp.body = rdb.get(self._table_name, 'email',
                                    email)
            elif limit:
                resp.body = rdb.get_all(self._table_name,
                                        offset * limit, limit)
            else:
                resp.status = HTTP_400
                resp.body = bad_request(info='Invalid request')
        except RqlError as e:
            raise HTTPBadRequest('Invalid request', e.message)

    def on_post(self, req, resp, id=None):
        """Create subscriber"""
        try:
            raw_json = req.stream.read()
            result = json.loads(raw_json, encoding='utf-8')
            validate_subscriber(result)
        except Exception as e:
            raise HTTPBadRequest('Invalid JSON', e.message)
        else:
            rdb = RethinkDBClient()
            if rdb.get(self._table_name, 'email', result["email"]):
                resp.status = HTTP_400
                resp.body = bad_request(info='Subscriber with that email '
                                             'address already exists')
            else:
                try:
                    rdb.insert(self._table_name, result)
                except RqlError as e:
                    raise HTTPBadRequest('Can not create subscriber',
                                         e.message)
                else:
                    resp.body = ok(ret='Subscriber created')

    def on_put(self, req, resp, id):
        """Update subscriber"""
        try:
            raw_json = req.stream.read()
            result = json.loads(raw_json, encoding='utf-8')
            validate_subscriber(result)
            rdb = RethinkDBClient()
            rdb.get(self._table_name, 'id', id)[0]
        except IndexError:
            raise HTTPBadRequest('Subscriber ' + id + ' does not exist')
        except Exception as e:
            raise HTTPBadRequest('Invalid JSON', e.message)
        else:
            try:
                rdb = RethinkDBClient()
                rdb.update(self._table_name, id, result)
            except RqlError as e:
                raise HTTPBadRequest('Can not update subscriber' + id,
                                     e.message)
            else:
                resp.body = ok(ret='Subscriber %s updated') % id

    def on_delete(self, req, resp, id):
        """Delete subscriber"""
        try:
            rdb = RethinkDBClient()
            rdb.get(self._table_name, 'id', id)[0]
        except IndexError:
            raise HTTPBadRequest('Subscriber ' + id + ' does not exist')
        else:
            try:
                rdb = RethinkDBClient()
                rdb.delete(self._table_name, id)
            except RqlError as e:
                raise HTTPBadRequest('Can not delete subscriber' + id,
                                     e.message)
            else:
                resp.body = ok(ret='Subscriber %s deleted') % id
