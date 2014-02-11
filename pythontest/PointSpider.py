__author__ = 'siyu'

import CommonUtils
import Domain

def getUrlContent():
    return CommonUtils.getSoupFromUrl("http://g.hupu.com/nba/daily/boxscore_23325.html")

def getTeamPoints():
    content = getUrlContent()
    teamInfo = content.find_all('div','message')
    #主队名称
    homeName = teamInfo[0].p.a.string
    #客队名称
    guestName = teamInfo[1].p.a.string

    #附加信息
    dateTime = content.find('p','time_f').replace(u'开赛：','').replace(u'年','-').replace(u'月','-').replace(u'日','')
    peopleNum = content.find('p','peopleNum').replace(u'上座：','').replace(u'人','')

    # 比分相关
    point = Domain.Point()

    # 球员数据相关
    playerRecord = Domain.PlayerRecord()

    #获取比分
    trInfo = content.find('table','itinerary_table').tr





if __name__ == '__main__':
    getTeamPoints()