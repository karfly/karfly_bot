import urllib
import urllib2

import json

KARFLY_CHAT_ID = 124796645

class KarflyBot:
    def __init__(self, bot_id):
        self.bot_id = bot_id

    def connect(self, user_name):
        answer_str = urllib2.urlopen("https://api.telegram.org/bot" + self.bot_id + "/getUpdates").read()
        answer = json.loads(answer_str)

        for result in answer['result']:
            if result['message']['chat']['username'] == user_name:
                self.chat_id = result['message']['chat']['id']
                break

    def send_message(self, message, user_name):
        self.connect(user_name)
        urllib2.urlopen('https://api.telegram.org/bot' + self.bot_id + '/sendMessage',
                        urllib.urlencode({'chat_id': self.chat_id, 'text': message}))