# -*- coding: utf-8 -*-
import Tool
import time
from Tieba import Tieba


def main():
    print("Local Time:", time.asctime(time.localtime()))
    for filepath in Tool.get_cookies_files('.'):
        # Load
        user = Tieba()
        user.load_cookies_from_file(filepath)
        # List Likes
        print(user.get_likes())
        # Sign
        print(user.username, "Signing")
        user.sign_all(delay=10)


main()
