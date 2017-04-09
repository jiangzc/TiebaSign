# -*- coding: utf-8 -*-
import Tool
import time
from Tieba import Tieba


def main():
    print("Local Time:", time.asctime(time.localtime()))
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
        Tool.redirection.clear()
    # Exit
    Tool.redirection.exit()

main()
