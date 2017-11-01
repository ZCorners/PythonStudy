from __future__ import print_function
from __future__ import print_function
import re
import urllib2
from time import sleep

import itertools


def download(url, user_agent='wswp', num_retries=2):
    print("Downloading:" + url)
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print("Download error:", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5xx HTTP errors
                sleep(1)
                return download(url, user_agent, num_retries - 1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall("<a href=\"(.*?)\">", sitemap)
    for link in links:
        html = download(link)

# crawl_sitemap('http://example.webscraping.com/sitemap.xml')

html = '<td class="w2"><img></img></td>'
print(re.findall('<td class="w2">(.*?)</td>', html))
