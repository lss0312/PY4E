# Unicode Characters and Strings
print(ord('H')) # tell us what the numeric value of a simple ASCII character.
#>> 72
encode# transform something into byte
decode# transform byte into unicode (utf-8 of ASCII)

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	print(line.decode().strip()) # get the content of the html in a shorter expression.

	# when read html file, we should first decode it.
from bs4 import BeautifulSoup# used to spider the web.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html.'html.parser')

tags = soup('a')
print(tags)

