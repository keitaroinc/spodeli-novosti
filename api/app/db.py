# -*- coding:utf-8 -*-
import rethinkdb as r
import json
from settings import RDB_HOST, RDB_PORT, RDB_DB


class RethinkDBClient(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            raise

        self._close()

    def __init__(self, host=None, port=None, db=None):
        if host is None:
            host = RDB_HOST
        if port is None:
            port = RDB_PORT
        if db is None:
            db = RDB_DB

        self.host = host
        self.port = port
        self._db = db
        self._conn = r.connect(self.host, self.port, self.db)

    def _close(self):
        self._conn.close()

    @property
    def conn(self):
        return self._conn

    @property
    def db(self):
        return self._db

    def insert(self, table_name, data):
        conn = self.conn
        try:
            r.table(table_name).insert(data).run(conn)
        except r.errors.ReqlOpFailedError as e:
            raise e.message

    def update(self, table_name, id, data):
        conn = self.conn
        try:
            r.table(table_name).filter(r.row['id'] == id).update(data). \
                run(conn)
        except r.errors.ReqlOpFailedError as e:
            raise e.message

    def delete(self, table_name, id):
        conn = self.conn
        try:
            r.table(table_name).filter(r.row['id'] == id).delete().run(conn)
        except r.errors.ReqlOpFailedError as e:
            raise e.message

    def get(self, table_name, key, value):
        conn = self.conn
        try:
            result = r.table(table_name).filter({key: value}).run(conn)
        except r.errors.ReqlOpFailedError as e:
            raise e.message
        else:
            rset = [json.dumps(item) for item in result]
            if rset:
                return json.dumps(rset[0])
            else:
                return None

    def get_all(self, table_name, skip, limit):
        conn = self.conn
        try:
            result = r.table(table_name).skip(skip).limit(limit).run(conn)
        except r.errors.ReqlOpFailedError as e:
            raise e.message
        else:
            return json.dumps([json.dumps(item) for item in result])

    def get_everyone(self, table_name):
        conn = self.conn
        try:
            result = r.table(table_name).run(conn)
        except r.errors.ReqlOpFailedError as e:
            raise e.message
        else:
            return [json.dumps(item) for item in result]


class RethinkDBFactory(object):
    def __init__(self, host=RDB_HOST, port=RDB_PORT, db=RDB_DB, tables=None,
                 **kwargs):
        if tables is None:
            tables = {}
        self.client = RethinkDBClient(host, port, db)
        self._tables = tables
        self._init()

    def _init(self):
        conn = self.client.conn
        try:
            r.db_create(self.client._db).run(conn)
        except r.errors.ReqlOpFailedError as e:
            pass

        for table_name, index_names in self._tables.items():
            self.create_table(table_name, index_names)

    def create_table(self, table_name, index_names=None):
        if index_names is None:
            index_names = []
        conn = self.client.conn
        try:
            r.table_create(table_name).run(conn)
        except r.errors.ReqlOpFailedError as e:
            pass

        for idx_name in index_names:
            try:
                r.table(table_name).index_create(idx_name).run(conn)
            except r.errors.ReqlOpFailedError as e:
                pass
