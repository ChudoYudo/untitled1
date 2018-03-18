#!/usr/bin/env python

import requests
import json
import datetime
import time
import argparse
import os


class BotHandler(object):
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        params = {"timeout": timeout, "offset": offset}
        resp = requests.get(self.api_url + "getUpdates", params).json()
        if "result" not in resp:
            return []
        return resp["result"]

    def send_message(self, chat_id, text):
        params = {"chat_id": chat_id, "text": text}
        return requests.post(self.api_url + "sendMessage", params)


def main():


    token = "537225479:AAGWqBwv3QmkcSKLuPqv8MrAFQdrvv66in4"

    bot = BotHandler(token)
    offset = 0

    while True:
        print("ll")
        updates = bot.get_updates(offset=offset)
        for update in updates:
            print(update)
            chat_id = update["message"]["chat"]["id"]
            if "text" in update["message"]:
                bot.send_message(chat_id, "ECHooO: " + update["message"]["text"])


            offset = max(offset, update['update_id'] + 1)

        time.sleep(1)



if __name__ == "__main__":
    main()
