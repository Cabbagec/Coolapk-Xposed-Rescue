#!/usr/bin/env python3
from html.parser import HTMLParser
from urllib.parse import urlparse, parse_qs

class Eros(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.Belta = False
        self.Pampa = []

    def __enter__(self):
        print("获取搜索页...")
        return self

    def handle_starttag(self, tag, attr):
        if (tag == 'div' and attr == [('class','panel-footer '
        'ex-card-footer text-center')]):
            self.Belta = True
        if self.Belta and tag == 'a':
            self.Pampa.append(attr)

    def handle_endtag(self, tag):
        if tag == 'div':
            self.Belta = False

    def handle_data(self, data):
        if data == '最末页':
            self.Inner = self.Pampa[-1][0][1]
            self.Inner = urlparse(self.Inner)
            self.Inner = parse_qs(self.Inner.query)['p'][0]
            self.Inner = int(self.Inner)

    def __exit__(self, exec_type, exec_value, traceback):
        print("获取所有搜索页面...")
        del self.Belta, self.Pampa