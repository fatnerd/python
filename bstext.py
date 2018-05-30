import urllib
from bs4 import BeautifulSoup
try:
	html=urllib.urlopen("http://stackoverflow.com/questions/18419500/how-to-make-mac-os-use-the-python-installed-by-homebrew")
except HTTPError as e:
	print(e)
else:
	print(html)

bsObj = BeautifulSoup(html.read())
print(bsObj.h1)