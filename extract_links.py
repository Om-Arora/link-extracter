#!/usr/bin/env python3
import requests
import sys
import traceback
from bs4 import BeautifulSoup
if len(sys.argv) < 2:
    print ("[!] URL not provided !")
    print ("[+] Usage : ./extract_links.py <URL>")
    quit()
elif len(sys.argv) > 2:
    print ("[!] Too many arguments provided !")
    print ("[+] Usage : ./extract_links.py <URL>")
    quit()

URL = sys.argv [1]

if not (URL.startswith('http://') or URL.startswith('https://')) :
    URL = 'http://' + URL

try:
    get = requests.get(URL)
except Exception as exc:
    print ('[!] Error occured !')
    print (f'[!] {traceback.format_exc()}')
    quit()

html = get.text
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.findAll('a'):
    if not tag['href'] == '#':
            print (tag['href'])
