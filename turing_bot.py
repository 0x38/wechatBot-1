import json
import requests

KEY = '2e72cb905f084783b350f492786e2538'
url = 'http://www.tuling123.com/openapi/api'

def get_response(req):
    query = {'key': KEY, 'info': req}
    headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

    r = requests.get(url, params=query, headers=headers)
    response = r.text
    print(json.loads(response).get('text').replace('<br>', 'n'))

while True:
    raw = input(": ")
    req = raw.encode('utf-8')
    get_response(req)
