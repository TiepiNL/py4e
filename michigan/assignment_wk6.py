'''
http://py4e-data.dr-chuck.net/comments_42.json        (Sum=2553)
http://py4e-data.dr-chuck.net/comments_1438675.json   (Sum ends with 15)

Data Format
The data consists of a number of names and comment counts in JSON as follows:
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

Assignment
Parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file.
'''

import json
import ssl
import urllib.request
import urllib.parse
import urllib.error


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
        url = 'http://py4e-data.dr-chuck.net/comments_42.json '
    return url


def get_url_content(url):
    '''(str) -> str
    '''
    ctx = ssl_no_verification()

    url = urllib.request.urlopen(url, context=ctx).read().decode()
    return url


def get_total_count(data):
    '''(str) -> int
    '''
    jsn = json.loads(data)
    total = 0
    for item in jsn['comments']:
        total += int(item['count'])
    return total


json_url = get_input()
json_data = get_url_content(json_url)
count = get_total_count(json_data)
print(count)
