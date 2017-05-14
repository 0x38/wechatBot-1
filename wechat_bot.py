import itchat
from itchat.content import TEXT
import requests
import threading
import json

bot_api="http://127.0.0.1:8000/get_response"

@itchat.msg_register(TEXT, isFriendChat=True)
def text_reply(msg):
    user_input = msg['Text']
    payload = {"user_input":user_input}
    response = requests.get(bot_api, params=payload).json()["response"]
    itchat.send(response, msg['FromUserName'])

def bot_server():
    from bottle import Bottle, run
    from bottle import response, request
    from json import dumps
    import json
    import requests

    KEY = '2e72cb905f084783b350f492786e2538'
    url = 'http://www.tuling123.com/openapi/api'

    app = Bottle()
    @app.route('/get_response')
    def get_response():
        user_input = request.query.user_input or ""
        query = {'key': KEY, 'info': user_input}
        headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

        r = requests.get(url, params=query, headers=headers)
        # response = r.text
        response = json.loads(r.text).get('text').replace('<br>', 'n')
        res = {'response':response}
        return dumps(res)

    run(app, host='localhost', port=8000)

botThread = threading.Thread(target=bot_server)
botThread.setDaemon(True)
botThread.start()

itchat.auto_login(hotReload=True)
itchat.run()
