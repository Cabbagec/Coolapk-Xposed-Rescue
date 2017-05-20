#!/usr/bin/env python3
from html.parser import HTMLParser

class Ganymede(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.Earther = False
        self.Belter = []
        self.Martian = []

    def __enter__(self):
        print("读取搜索列表...")
        return self

    def handle_starttag(self, tag, attr):
        if tag == "ul" and \
            attr == [("class", "media-list ex-card-app-list")]:
            self.Earther = True
        if self.Earther and tag == "li":
            self.Belter.append(attr)

    def handle_endtag(self, tag):
        if tag == "ul":
            self.Earther = False

    def __exit__(self, exec_type, exec_value, traceback):
        print("获取应用网址...")
        for Belta in self.Belter:
            Belta = dict(Belta)['data-touch-url']
            self.Martian.append(Belta)

        del self.Belter, self.Earther