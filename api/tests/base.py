# -*- coding:utf-8 -*-
from falcon.testing import TestCase
from app import create_app, db


class BaseTestCase(TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.app = create_app()

    def tearDown(self):
        pass
