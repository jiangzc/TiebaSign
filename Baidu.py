# -*- coding: utf-8 -*-
import requests
import re
import json


def load_cookies(path):
    '''
    加载浏览器的Cookie
    '''
    with open(path, 'r') as f:
        data = json.load(f)
    cookies = dict()
    for item in data:
        cookies[item["name"]] = item["value"]
    return cookies


class Baidu():
    def __init__(self, cookies):
        self.base_url = "https://www.baidu.com"
        self.session = requests.session()
        self.session.cookies.update(cookies)
        self.session.headers["User-Agent"] = "Mozilla/5.0 Chrome/53.0.2785.143 Safari/537.36"
        print("Login:", self.get_username())

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
