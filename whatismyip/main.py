#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import schedule
import time
from src.telegram import Telegram


class Singleton:
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        self.__public_ip = None
        
    @property
    def public_ip(self) -> str:
        return self.__public_ip

    @public_ip.setter
    def public_ip(self, ip) -> str:
        self.__public_ip = ip


def main():
    singleton = Singleton()

    endpoint = 'https://ipinfo.io/json'
    try:
        res = requests.get(endpoint, verify = True)
        data = res.json()
        singleton.public_ip = data["ip"]
        if res.status_code != 200:
            raise Exception(f'Error: status code {res.status_code}')
    except Exception as e:
        msg = f'Error: {e}'
        print(msg)
    
    telegram = Telegram()

    if singleton.public_ip != data["ip"]:
        msg = f"Your public ip has been changed to {singleton.public_ip}"
        telegram.send_message(msg)


if __name__ == '__main__':
    # main()
    schedule.every(5).minutes.do(main)

    while True:
            schedule.run_pending()
            time.sleep(1)