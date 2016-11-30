# -*- coding:utf-8 -*-
import rethinkdb as r
import json
from settings import RDB_HOST, RDB_PORT, RDB_DB


class RethinkDBFactory(object):
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._conn.close()

    def __init__(self, host=RDB_HOST, port=RDB_PORT, db=RDB_DB, tables=None,
                 **kwargs):
        if tables is None:
            tables = {}
        self.host = host
        self.port = port
        self._db = db
        self._tables = tables
        self._conn = None
        self._init()

    def _init(self):
        conn = self.conn

        try:
            r.db_create(self._db).run(conn)
        except r.errors.ReqlOpFailedError as e:
            pass

        for table_name, index_names in self._tables.items():
            self.create_table(table_name, index_names)

    def create_table(self, table_name, index_names=None):
        if index_names is None:
            index_names = []
        conn = self.conn
        try:
            r.table_create(table_name).run(conn)
        except r.errors.ReqlOpFailedError as e:
            pass

        for idx_name in index_names:
            try:
                r.table(table_name).index_create(idx_name).run(conn)
            except r.errors.ReqlOpFailedError as e:
                pass

    def insert(self, table_name, data):
        conn = self.conn
        try:
            r.table(table_name).insert(data).run(conn)
        except r.errors.ReqlOpFailedError as e:
            raise e.message

    def update(self, table_name, id, data):
        conn = self.conn
        try:
            r.table(table_name).filter(r.row['id'] == id).update(data).\
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

    @property
    def conn(self):
        if self._conn is None:
            return r.connect(self.host, self.port, self.db)
        else:
            return self._conn

    @property
    def db(self):
        return self._db


class RethinkResource(object):
    def __init__(self, factory=None, host=RDB_HOST, port=int(RDB_PORT),
                 db=RDB_DB, tables=None, **kwargs):
        if factory is None:
            self.factory = RethinkDBFactory(host, port, db, tables, **kwargs)
        else:
            self.factory = factory

    @property
    def conn(self):
        return self.factory.conn
