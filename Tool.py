import os
import sys

os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))


def get_cookies_files(dirpath):
    return [os.path.join(dirpath, x) for x in os.listdir(dirpath) if x.endswith(".json") or x.endswith(".txt")]
