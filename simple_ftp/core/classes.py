# -*- encoding:utf-8 -*-
# Author: Koctr


class User(object):
    """
    用户类
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def list_files(self, direction):
        pass

    def upload_file(self, file):
        pass

    def download_file(self, file):
        pass


class Server(object):
    """
    ftp服务器类
    """
    def __init__(self):
        pass

