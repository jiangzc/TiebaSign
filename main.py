# -*- coding: utf-8 -*-
import builtins
import os
import sys
import json
import time
from Tieba import Tieba


PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
_open = builtins.open


def open1(file, mode, *args, **kwargs):
    if mode.endswith("&"):
        file = os.path.join(PATH, os.path.basename(file))
        return _open(file, mode[:-1], *args, **kwargs)


def load_cookies(path):
    with open1(path, 'r&') as f:
        data = json.load(f)
    cookies = dict()
    for item in data:
        cookies[item["name"]] = item["value"]
    return cookies


def main():
    print("Local Time:", time.asctime(time.localtime()))
    print("\r\n")
    users_path = [x for x in os.listdir(PATH) if x.endswith(".json")]
    for path in users_path:
        user = Tieba(load_cookies(path))
        for name in user.get_likes():
            user.sign_Wap(name)

main()
