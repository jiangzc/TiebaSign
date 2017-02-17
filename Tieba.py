# -*- coding: utf-8 -*-
import Baidu
import re


def Retry(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) or func(*args, **kwargs) or func(*args, **kwargs)
    return wrapper


class Tieba(Baidu.Baidu):
    def _get_tbs(self, url):
        tbs_pattern = re.compile("'tbs': \"(.+?)\"")
        match = tbs_pattern.search(self.session.get(url).text)
        if match:
            return match.group(1)
        else:
            return ""

    @Retry
    def _check_sign(self, tieba_name):
        res = self.session.get("http://tieba.baidu.com/mo/m?kw=" + tieba_name)
        return "已签到" in res.text

    @Retry
    def get_likes(self):
        try:
            res = self.session.get("http://tieba.baidu.com/mo/")
            likes_url = "http://tieba.baidu.com" + \
                        re.search('"([^"]+tab=favorite)"', res.text).group(1).replace("&amp;", "&")
            res = self.session.get(likes_url)
            likes = re.findall('kw.+?">(.+?)<', res.text)
            return likes
        except:
            return False

    def sign_Wap(self, tieba_name):
        if self._check_sign(tieba_name):
            print("Already signed in", tieba_name)
            return False
        tieba_url = "http://tieba.baidu.com/mo/m?kw=" + tieba_name
        res = self.session.get(tieba_url)
        match = re.search('(/mo/q[^<]+?)">签到', res.text)
        if match:
            sign_url = "http://tieba.baidu.com" + match.group(1)
            sign_url = sign_url.replace("&amp;", "&")
            res = self.session.get(sign_url)

        if "已签到" in res.text:
            print("Signed successfully in", tieba_name)
            return True
        else:
            print("Fail to sign in", tieba_name)
            return False

    def reply(self, tid, content):
        if 'p' in str(tid):
            # tid is an URL
            url = tid
            tid = re.search("\d+", url).group(0)
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
            data={
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
