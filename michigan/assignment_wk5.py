'''
Extracting Data from XML

http://py4e-data.dr-chuck.net/comments_42.xml
http://py4e-data.dr-chuck.net/comments_1438674.xml

Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

You are to look through all the <comment> tags and find the <count> values sum the numbers.
'''

import ssl
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET


def ssl_no_verification():
    ''' (None) -> SSLContext
    '''
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def get_input():
    ''' (None) -> str

    Ask user for an url, the position (nth href), and the number of links to follow.
    '''
    url = input("Enter a url: ")
    if url == '':
        url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    return url


def get_xml_content(url):
    '''(str) -> str
    '''
    ctx = ssl_no_verification()

    url = urllib.request.urlopen(url, context=ctx).read()
    return url.decode()


def get_total_count(data):
    '''(str) -> int
    '''
    tree = ET.fromstring(data)

    lst = tree.findall('.//count')
    total = 0
    for item in lst:
        total += int(item.text)
    return total


xml_url = get_input()
xml_data = get_xml_content(xml_url)
count = get_total_count(xml_data)
print(count)
