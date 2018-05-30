# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

sauce=urllib.request.urlopen('https://zh.wikipedia.org/wiki/GNU計劃').read()

soup=bs.BeautifulSoup(sauce,'lxml')

print(soup.title)