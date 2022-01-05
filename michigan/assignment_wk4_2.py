'''
http://py4e-data.dr-chuck.net/known_by_Fikret.html
http://py4e-data.dr-chuck.net/known_by_Malecia.html
'''

import re
import ssl
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

def ssl_no_verification():
    ''' (None) -> SSLContext
    '''
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def get_input():
    ''' (None) -> lst [str, int, int]

    Ask user for an url, the position (nth href), and the number of links to follow.
    '''
    url = input("Enter a url: ")
    if url == '':
        url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

    position = input("Enter a position: ")
    if position == '':
        position = 1
    else:
        position = int(position)

    count = input("Enter a count: ")
    if count == '':
        count = 1
    else:
        count = int(count)

    return [url, position, count]


def follow_link(lst):
    '''(lst [str, int, int]) -> str
    '''
    url = lst[0]
    position = lst[1]
    count = lst[2]

    ctx = ssl_no_verification()

    while count > 0:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
        tags = soup('a')
        if len(tags) >= position:
            url = tags[position-1].get('href')
        count -= 1

    return url

def url_to_name(url):
    '''(str) -> str
    '''
    regex = 'by_(.+).html'
    return re.findall(regex, url)[0]


crawl_input = get_input()
full_url = follow_link(crawl_input)
print(url_to_name(full_url))
