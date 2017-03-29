# -*- coding: utf-8 -*-
import Tool
import os
import sys
import time
from mail import Email
from Tieba import Tieba


PATH = os.path.abspath(os.path.dirname(sys.argv[0]))


def main():
    print("Local Time:", time.asctime(time.localtime()))
    # Email
    print("Login Email, waiting......")
    gmail = Email("***", "***")

    # Redirect Standard Output
    Tool.redirection.enter()
    Tool.redirection.to_console()
    # Read Cookies
    cookies = Tool.load_cookies_path(PATH)
    for cookie in cookies:
       # Login
        user = Tieba(cookie)
        # List Likes
        print(user.get_likes())
        # Sign
        print(user.username, "Signing")
        for name in user.get_likes():
            if user.sign_Wap(name):
                time.sleep(10)

        gmail.sendmail("Tieba Cloud Sign System", "985811440@qq.com", "Result of Signing", Tool.redirection.history)
        Tool.redirection.clear()
    # Exit
    Tool.redirection.exit()
    gmail.close()
    #print(Tool.redirection.history)


main()
