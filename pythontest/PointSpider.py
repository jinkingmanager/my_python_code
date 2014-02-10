__author__ = 'siyu'

import  CommonUtils

def getUrlContent():
    return CommonUtils.getSoupFromUrl("http://g.hupu.com/nba/daily/boxscore_23325.html")

def getTeamPoints():
    content = getUrlContent()
    home_TeamInfo = content.find('div','team_a')
    print home_TeamInfo.string
    return content

if __name__ == '__main__':
    getTeamPoints()