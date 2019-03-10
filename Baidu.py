# -*- coding: utf-8 -*-
import requests
import re
import json


class Baidu:
    def __init__(self):
        self.base_url = "https://www.baidu.com"
        self.username = ""
        self.session = requests.session()
        self.session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"

    def load_cookies_from_file(self, filepath):
        # Format 1: exported from EditThisCookie plugin in Chrome
        if filepath.endswith(".json"):
            with open(filepath, 'r') as f:
                data = json.load(f)
            cookies = dict()
            for item in data:
                cookies[item["name"]] = item["value"]
            self.session.cookies.update(cookies)
        # Format 2: exported from Network monitor in Chrome
        elif filepath.endswith(".txt"):
            with open(filepath, 'r') as f:
                text = f.read()
            text = text.replace(' ', '').replace('\n', '').replace('\r', '')
            for item in text.split(';'):
                self.session.cookies.set(item[:item.index('=')], item[item.index('=') + 1:])
        else:
            raise ValueError('filepath: %s is invalid format' % filepath)
        if self.check_login():
            self.username = self.get_username() or self.get_username() or self.get_username()
            print("Login:", self.username)
            return True
        else:
            print("Login failed, cookies are from ", filepath)
            return False

    def check_login(self):
        res = self.session.get(self.base_url)
        if re.search("'login':'1'", res.text):
            return True
        return False

    def get_username(self):
        res = self.session.get(self.base_url)
        match = re.search("=user-name>(.+?)<", res.text)
        if match:
            return match.group(1)
        else:
            print("Fail to get username!")
            return None
