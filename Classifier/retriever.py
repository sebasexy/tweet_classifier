import re
import urllib.request, urllib.error
import http.client
import html

def load(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Twitterbot/1.0'})
    return urllib.request.urlopen(req).read()

def find_tweet(url):
    regex = '<title>.*?&quot;(.*?)&quot;</title>'
    tweet = re.findall(regex, load(url).decode('utf-8'))
    tweet = html.unescape(tweet[0])
    return tweet