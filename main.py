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

def load_cookies(filename):
    if filename.endswith(".json"):
        with open1(filename, 'r&') as f:
            data = json.load(f)
        cookies = dict()
        for item in data:
            cookies[item["name"]] = item["value"]
        return cookies
    elif filename.endswith(".cookie"):
        with open1(filename, 'r&') as f:
            data = json.load(f)
        return data
    else:
        pass


def load_files(dirpath):
    files_name = [x for x in os.listdir(dirpath) if x.endswith(".json") or x.endswith(".cookie")]
    users = list()
    for file in files_name:
        users.append(Tieba(load_cookies(file)))
    return users

def main():
    print("Local Time:", time.asctime(time.localtime()))
    print("\r\n")
    users = load_files(PATH)
    for user in users:
        print(user.username, "Signing")
        for name in user.get_likes():
            if user.sign_Wap(name):
                time.sleep(10)
        print("\r\n")

main()
