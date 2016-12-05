#coding: utf-8

import requests
import json

test_date = [
    {
    'test1': {
        'user': 'lisetn',
        'job': 'te',
        'mac': 'aa:bb:cc:dd:ee:ff',
        'ip': '192.168.1.1',
        'description': '',
    }
    },
    {
        'test2': {
        'user': 'test',
        'job': 'cn',
        'mac': 'aa:11:cc:33:ee:55',
        'ip': '192.168.100.100',
        'description': '',
        }
     },
{
        'test3': {
        'user': 'test1',
        'job': 'cn1',
        'mac': 'aa:11:cc:33:ee:55',
        'ip': '192.168.100.100',
        'description': '1',
        },
        'test4': {
        'user': 'test4',
        'job': 'cn',
        'mac': 'aa:11:cc:33:ee:55',
        'ip': '192.168.100.100',
        'description': '4',
        }
     }
]

#json encode
json_str = json.dumps(test_date)
data = json_str.encode('utf-8')

r = requests.post("http://127.0.0.1:5000/", data={'data': data})
print r.text







