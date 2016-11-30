# -*- coding:utf-8 -*-
from tests.base import BaseTestCase


class TestIndex(BaseTestCase):
    def setUp(self):
        super(TestIndex, self).setUp()

    def test_get_index(self):
        content = 'Сподели Новости'

        result = self.simulate_get('/')

        self.assertEqual(result.content, content)

    def tearDown(self):
        pass
