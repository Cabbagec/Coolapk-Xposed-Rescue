#!/usr/bin/env python3
from re import search

class Luna():
    def __init__(self, feed):
        self.EpsteinDrive = search(r".*var apkDownloadUrl = \"(\S*?)\"",\
            feed).group(1)
        print("\n解析 apk 文件地址...")
        print(self.EpsteinDrive)

        self.EpsteinDrive2 = search(r".*img\s*class=\"media-object\s*img-rounded\"\s*src=\"(.*?)\"\s*alt=\"(.*?)\"", feed).group(1)
        print("解析应用图片地址...")
        print(self.EpsteinDrive2)

        self.EpsteinDrive3 = search(r".*img\s*class=\"media-object\s*img-rounded\"\s*src=\"(.*?)\"\s*alt=\"(.*?)\"", feed).group(2)
        print("解析应用名称")

        self.EpsteinDrive4 = search(r"\?pn=(\S*?)&", self.EpsteinDrive).group(1)
        print("解析应用包名...")
        print(self.EpsteinDrive4)

        self.EpsteinDrive5 = search(r'.*/(\S*)', self.EpsteinDrive2).group(1)
        print("图片文件名...")
        print(self.EpsteinDrive5)
