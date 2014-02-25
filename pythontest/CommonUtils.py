#coding=utf-8
__author__ = 'siyu'

from bs4 import BeautifulSoup
import urllib2
import sqlite3

# get all content using urllib2
def getAllContent(url):
    wp = urllib2.urlopen(url,None)
    return wp.read()

# get bs obj from url
def getSoupFromUrl(url):
    wp = getAllContent(url)
    #print len(wp)
    return BeautifulSoup(wp)

def getConnect():
    conn = sqlite3.connect("nba.db")
    return conn