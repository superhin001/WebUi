import unittest
import requests
import json
import pymysql

url = 'http://115.28.108.130:8080/gasStation/process'
headers = {'Content-Type': 'application/json'}
payload = {
    "dataSourceId": "bG9uZ3Rlbmd0ZXN0",
    "methodId": "04A",
    "CardUser": {
        "userId": 616
},
    "CardInfo": {
        "cardNumber": "1230012300",
        "cardBalance": "1"
 }
}

db = pymysql.connect(host='115.28.108.130', user="test", passwd="123456", db="longtengserver", port=3306)
cursor = db.cursor()
sql = 'select * from cardinfo where cardNumber=1230012300'
cursor.execute(sql)
db.commit()
balance_db = int(cursor.fetchone()[4])
balance_consume = int(payload['CardInfo']['cardBalance'])

class Consume(unittest.TestCase):
    def test_consume(self):
        r = requests.post(url, json=payload, headers=headers)
        if balance_db > balance_consume:
            self.assertEqual(200, json.loads(r.text)['code'])
            self.assertIn('消费成功', r.text)
        else:
            self.assertEqual(200, json.loads(r.text)['code'])
            self.assertIn('余额不足', r.text)

if __name__ == '__main__':
    unittest.main()
