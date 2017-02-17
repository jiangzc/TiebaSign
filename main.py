# -*- coding: utf-8 -*-
import Tool
import os
import sys
import time
from Tieba import Tieba


PATH = os.path.abspath(os.path.dirname(sys.argv[0]))


def main():
    print("Local Time:", time.asctime(time.localtime()))
    #print("\r\n")
    with Tool.redirection:
        Tool.redirection.to_console()
        print("hello")

    print(Tool.redirection.history)
    ###
    # cookies = Tool.load_cookies_path(PATH)
    # for cookie in cookies:
    #     user = Tieba(cookie)
    #     print(user.get_likes())

        # print(user.username, "Signing")
        # for name in user.get_likes():
        #     if user.sign_Wap(name):
        #         time.sleep(10)
        # print("\r\n")

main()
