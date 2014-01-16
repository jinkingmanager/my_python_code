# coding=utf-8
__author__ = 'siyu'
import urllib2
from bs4 import BeautifulSoup


def get_file_size(url, proxy=None):
    """通过content-length头获取文件大小
    url - 目标文件URL
    proxy - 代理
    """
    opener = urllib2.build_opener()
    if proxy:
        if url.lower().startswith('https://'):
            opener.add_handler(urllib2.ProxyHandler({'https': proxy}))
        else:
            opener.add_handler(urllib2.ProxyHandler({'http': proxy}))
    request = urllib2.Request(url)
    request.get_method = lambda: 'HEAD'
    try:
        response = opener.open(request)
        response.read()
    except Exception, e:
        print '%s %s' % (url, e)
    else:
        return dict(response.headers).get('content-length', 0)


def getTdValue():
    str = '<html><tr><td>到期</td></tr></html>'
    money = BeautifulSoup(str)
    print(money.getText('left').replace('left',','))
    print cmp("到期".decode("utf8"),money.getText('left').replace('left',','))


if __name__ == '__main__':
    #print get_file_size(url='http://g.hupu.com/nba/players/')
    getTdValue()