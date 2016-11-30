# -*- coding:utf-8 -*-
from tests.base import BaseTestCase
import json


class TestSubscriber(BaseTestCase):
    def setUp(self):
        super(TestSubscriber, self).setUp()

    def test_post_subscriber(self):
        title = u'OK'

        payload = {"name": "John Doe", "email": "john.doe@acme.com"}
        result = self.simulate_post('/subscriber', body=json.dumps(payload))

        self.assertEqual(result.json["title"], title)

        test_sub = self.simulate_get('/subscriber',
                                     params={"email": "john.doe@acme.com"})
        sub_id = json.loads(test_sub.json)["id"]
        self.simulate_delete('/subscriber/' + sub_id)

    def test_invalid_post_subscriber(self):
        title = u'Invalid JSON'

        payload = {"name": "John Doe", "email": "invalidemail"}
        result = self.simulate_post('/subscriber', body=json.dumps(payload))

        self.assertEqual(result.json["title"], title)

    def test_existing_email_post_subscriber(self):
        title = u'Bad Request'

        payload = {"name": "Mark Twain", "email": "mark@acme.com"}
        self.simulate_post('/subscriber', body=json.dumps(payload))

        result = self.simulate_post('/subscriber', body=json.dumps(payload))

        self.assertEqual(result.json["title"], title)

        test_sub = self.simulate_get('/subscriber',
                                     params={"email": "mark@acme.com"})
        sub_id = json.loads(test_sub.json)["id"]
        self.simulate_delete('/subscriber/' + sub_id)

    def test_get_subscriber(self):
        name = u'John Smith'

        payload = {"name": "John Smith", "email": "john.smith@acme.com"}
        self.simulate_post('/subscriber', body=json.dumps(payload))

        result = self.simulate_get('/subscriber',
                                   params={"email": "john.smith@acme.com"})

        self.assertEqual(json.loads(result.json)["name"], name)

        test_sub = self.simulate_get('/subscriber',
                                     params={"email": "john.smith@acme.com"})
        sub_id = json.loads(test_sub.json)["id"]
        self.simulate_delete('/subscriber/' + sub_id)

    def test_get_all_subscribers(self):
        result = self.simulate_get('/subscriber')

        self.assertFalse(result.json)

    def test_invalid_get_all_subscribers(self):
        title = u'Invalid value for limit'

        result = self.simulate_get('/subscriber', params={"limit": "badvalue"})
        self.assertEqual(result.json["title"], title)

    def test_put_subscriber(self):
        title = u'OK'

        payload = {"name": "Pappa John", "email": "pappa.john@acme.com"}
        self.simulate_post('/subscriber', body=json.dumps(payload))

        update = {"name": "John", "email": "john@acme.com"}
        test_sub = self.simulate_get('/subscriber',
                                     params={"email": "pappa.john@acme.com"})
        sub_id = json.loads(test_sub.json)["id"]
        result = self.simulate_put('/subscriber/' + sub_id,
                                   body=json.dumps(update))

        self.assertEqual(result.json["title"], title)

        self.simulate_delete('/subscriber/' + sub_id)

    def test_delete_subscriber(self):
        title = u'OK'

        payload = {"name": "Yosemite Sam", "email": "yo.sam@acme.com"}
        self.simulate_post('/subscriber', body=json.dumps(payload))

        test_sub = self.simulate_get('/subscriber',
                                     params={"email": "yo.sam@acme.com"})
        sub_id = json.loads(test_sub.json)["id"]
        result = self.simulate_delete('/subscriber/' + sub_id)

        self.assertEqual(result.json["title"], title)

    def tearDown(self):
        pass
