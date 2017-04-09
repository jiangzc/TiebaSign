# -*- coding: utf-8 -*-
import Tool
import time
from mail import Email
from Tieba import Tieba


def main():
    print("Local Time:", time.asctime(time.localtime()))
    # Email
    print("Login Email, waiting......")
    gmail = Email()

    # Redirect Standard Output
    Tool.redirection.enter()
    Tool.redirection.pass_to_console()

    # Read Cookies
    cookies = Tool.load_cookies_path(".")
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
    # print(Tool.redirection.history)


main()
