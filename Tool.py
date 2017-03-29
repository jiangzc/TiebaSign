import builtins
import os
import sys
import json


PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
_open = builtins.open


def open1(file, mode, *args, **kwargs):
    if mode.endswith("&"):
        file = os.path.join(PATH, os.path.basename(file))
        return _open(file, mode[:-1], *args, **kwargs)


def load_cookies_file(filename):
    if filename.endswith(".json"):
        with open1(filename, 'r&') as f:
            data = json.load(f)
        cookies = dict()
        for item in data:
            cookies[item["name"]] = item["value"]
        return cookies
    elif filename.endswith(".cookie"):
        with open1(filename, 'r&') as f:
            data = json.load(f)
        return data
    else:
        pass


def load_cookies_path(dirpath):
    files_name = [x for x in os.listdir(dirpath) if x.endswith(".json") or x.endswith(".cookie")]
    cookies = list()
    for file in files_name:
        cookies.append(load_cookies_file(file))
    return cookies


class dashboard():
    def __init__(self):
        if type(sys.stdout) == dashboard:
            raise Exception("Cannot initialize")
        self.buff = ""
        self.history = ""
        self.my_board = self
        self.__console = sys.stdout

    def write(self, stream):
        self.history += stream
        if self.my_board == self:
            self.buff += stream
        else:
            self.my_board.write(stream)

    def flush(self):
        self.buff = ""

    def clear(self):
        self.buff = self.history = ""

    def to_console(self):
        self.my_board = self.__console
        self.my_board.write(self.buff)
        self.flush()

    def reset(self):
        sys.stdout = self.__console
        self.clear()

    def enter(self):
        self.__enter__()

    def exit(self):
        sys.stdout = self.__console

    def __enter__(self):
        self.__init__()
        sys.stdout = self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.__console

redirection = dashboard()
