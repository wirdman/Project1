"""
dumpimages.py
    Downloads all the images on the supplied URL, and saves them to the
    specified output file ("/test/" by default)

Usage:
    python dumpimages.py http://example.com/ [output]
"""
import sys
sys.path.append('..')
sys.path.append('../lib')
sys.path.append('./lib')
sys.path.append('./bs4')
sys.path.append('../bs4')
from bs4 import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import urllib
import os

def main(url):
    """Downloads all the images at 'url' to /test/"""
    soup = bs(urlopen(url))
    for image in soup.findAll("img"):
        if image["src"].lower().endswith("500.jpg"):
            APP_DIR = os.path.dirname(os.path.abspath(__file__))
            pic = urllib.urlopen(image["src"])
            f = open( os.path.join(APP_DIR, "dailyPic.jpg"), 'wb')
            f.write(pic.read()) # save the pic
            f.close()

def _usage():
    print "usage: python dumpimages.py http://example.com [outpath]"

if __name__ == "__main__":
    url = sys.argv[-1]
    main(url)
