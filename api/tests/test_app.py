# -*- coding:utf-8 -*-
from tests.base import BaseTestCase


class TestApp(BaseTestCase):
    def setUp(self):
        super(TestApp, self).setUp()

    def test_create_app(self):
        testspodelinovosti = self.app

        self.assertEqual(testspodelinovosti, self.app)

    def tearDown(self):
        pass
