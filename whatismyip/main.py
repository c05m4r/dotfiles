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


def main(obj):

    endpoint = 'https://ipinfo.io/json'
    try:
        res = requests.get(endpoint, verify = True)
        data = res.json()
        if res.status_code != 200:
            raise Exception(f'Error: status code {res.status_code}')
    except Exception as e:
        msg = f'Error: {e}'
        print(msg)
    
    telegram = Telegram()

    if obj.public_ip is None:
        obj.public_ip = data["ip"]

    if obj.public_ip != data["ip"]:
        msg = f"Your public ip has been changed to {obj.public_ip}"
        telegram.send_message(msg)


if __name__ == '__main__':
    obj = Singleton()
    # main(obj)
    schedule.every(5).minutes.do(main, obj)

    while True:
        schedule.run_pending()
        time.sleep(1)