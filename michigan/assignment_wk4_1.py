'''
pip install beautifulsoup4

http://py4e-data.dr-chuck.net/comments_42.html
http://py4e-data.dr-chuck.net/comments_1438672.html

Data Format:
The file is a table of names and comment counts.
You can ignore most of the data in the file except for lines like the following:
<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

Assignment:
You are to find all the <span> tags in the file and pull out the numbers from the tag
and sum the numbers. Look for span tags and pull out the text content of the span tag,
convert them to integers and add them up
'''

import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1438672.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
nbrs = []
for tag in tags:
    # Look at the parts of a tag
    # Validate if the span has a 'comments' class
    if 'class' in tag.attrs.keys() and 'comments' in tag.attrs['class']:
        nbrs.append(int(tag.contents[0]))

print(sum(nbrs))
