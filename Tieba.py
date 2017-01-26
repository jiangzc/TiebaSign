# -*- coding: utf-8 -*-
import Baidu
import requests
import re
import json


class Tieba(Baidu.Baidu):
    def _get_tbs(self, url):
        tbs_pattern = re.compile("'tbs': \"(.+?)\"")
        match = tbs_pattern.search(self.session.get(url).text)
        if match:
            return match.group(1)
        else:
            return ""

    def _set_stoken(self):
        likes_url = "https://passport.baidu.com/v3/login/api/auth/?tpl=tb&jump=&return_type=3&u=http%3A%2F%2Ftie" \
                    "ba.baidu.com%2Ff%2Flike%2Fmylike%3Fpn%3D1"
        res = self.session.get(likes_url, allow_redirects=False)
        likes_url = res.headers['Location']
        res = self.session.get(likes_url, allow_redirects=False)
        stoken = re.search("STOKEN=(.+?);", res.headers['Set-Cookie']).group(1)
        self.session.cookies["STOKEN"] = stoken

    def _check_sign(self, url):
        res = self.session.get(url)
        return "'isSignIn':1" in res.text


    def get_likes(self):
        #self._set_stoken()
        res = self.session.get('http://tieba.baidu.com/f/like/mylike?pn=1', allow_redirects=False)
        last = re.search("pn=(\d+)\">尾页</a>", res.text).group(1)
        likes_url = 'http://tieba.baidu.com/f/like/mylike?pn='
        likes_tieba = []
        for i in range(1, int(last) + 1):
            res = self.session.get(likes_url + str(i))
            likes_tieba += re.compile('<a href.+?title="(.+?)"').findall(res.text)
        return likes_tieba

    def sign(self, tieba_name):
        tieba_url = "http://tieba.baidu.com/f?kw={0}&fr=index".format(tieba_name)
        if self._check_sign(tieba_url):
            print("Already signed in", tieba_name)
            return
        tbs = self._get_tbs(tieba_url)
        if not tbs:
            print("Failed to grasp ", tieba_name, " !")
            return
        sign_url = "http://tieba.baidu.com/sign/add"
        response = self.session.post(
            sign_url,
            data={
                'ie': 'utf-8',
                'kw': tieba_name,
                'tbs': tbs,
            },
        )
        data = json.loads(response.text)
        if data['no'] == 0:
            print("Signed successfully in", tieba_name)
        else:
            print("Failed to sign, reason:", data['error'], tieba_name)

    def reply(self, tid, content):
        if 'p' in str(tid):
            # tid is an URL
            url = tid
            tid = re.search("\d+",url).group(0)
        else:
            # tid is a string of numbers
            url = "http://tieba.baidu.com/p/" + str(tid)
        res = self.session.get(url)
        fid = re.search("fid:'(\d+?)'", res.text).group(1)
        kw = re.search("kw:'(.+?)'", res.text).group(1)
        res = self.session.post(
            "http://tieba.baidu.com/f/commit/post/add",
            data={
                "ie": "utf-8",
                "kw": kw,
                "fid": fid,
                "tid": tid,
                "vcode_md5": "",
                "rich_text": 1,
                "tbs": re.search('"tbs"  : "(.+?)"', res.text).group(1),
                "content": content,
                "__type__": "reply"
            })
        print(res.text)

    def commit(self, tieba_name, title, content):
        url = "http://tieba.baidu.com/f?kw=" + tieba_name
        fid = re.search("fid: (\d+)", self.session.get(url).text).group(1)
        res = self.session.post(
            "http://tieba.baidu.com/f/commit/thread/add",
            data = {
                "ie": "utf-8",
                "kw": tieba_name,
                "fid": fid,
                "tid": 0,
                "vcode_md5": "",
                "rich_text": 1,
                "floor_num": 0,
                "tbs": self._get_tbs(url),
                "content": content,
                "title": title,
                "__type__": "thread"
            })
        print(res.text)

