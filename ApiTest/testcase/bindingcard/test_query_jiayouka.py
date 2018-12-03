import unittest
import requests
import json


class Query(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)
    def test_queryexist(self):
        self.url = 'http://115.28.108.130:8080/gasStation/process'
        self.payload = {'dataSourceId': 'bG9uZ3Rlbmd0ZXN0',
                   'userId': '616',
                   'cardNumber': '1230012300',
                   'methodId': '02A'
                   }
        r = requests.get(self.url, params=self.payload)
        self.assertEqual(200, json.loads(r.text)['code'])
        self.assertIn('成功返回', r.text)

    def test_querynoexist(self):
        self.url = 'http://115.28.108.130:8080/gasStation/process'
        self.payload = {'dataSourceId': 'bG9uZ3Rlbmd0ZXN0',
                   'userId': '568',
                   'cardNumber': '22222222',
                   'methodId': '02A'
                   }
        r = requests.get(self.url, params=self.payload)
        self.assertEqual(400, json.loads(r.text)['code'])
        self.assertIn('false', r.text)



if __name__ == '__main__':
    unittest.main()
