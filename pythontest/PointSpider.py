#coding=utf-8
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
    dateTime = content.find('p','time_f').string.replace(u'开赛：','').replace(u'年','-').replace(u'月','-').replace(u'日','').replace('  ',' ')
    date = dateTime.split(' ')[0]
    time = dateTime.split(' ')[1]
    peopleNum = content.find('p','peopleNum').string.replace(u'上座：','').replace(u'人','')

    # 比分相关
    point = Domain.Point()

    # 球员数据相关
    playerRecord = Domain.PlayerRecord()

    #获取比分
    trInfos = content.find('table','itinerary_table').find_all('tr')

    #主队数据
    homeTdInfos = trInfos[1].find_all('td')
    #客队数据
    guestTdInfos = trInfos[2].find_all('td')

    #基础数据
    point.home = homeName
    point.guest = guestName
    point.date = date
    point.time = time
    point.peopleNum = peopleNum

    # 比分数据-home
    point.home1P = homeTdInfos[1].string
    point.home2P = homeTdInfos[2].string
    point.home3p = homeTdInfos[3].string
    point.home4P = homeTdInfos[4].string
    # guest
    point.guest1P = guestTdInfos[1].string
    point.guest2P = guestTdInfos[2].string
    point.guest3P = guestTdInfos[3].string
    point.guest4P = guestTdInfos[4].string

    # 存在加时的情况
    if(len(homeTdInfos) == 6):
        point.homePoint = homeTdInfos[5].string
        point.guestPoint = guestTdInfos[5].string
    elif(len(homeTdInfos) == 7):
        point.home5P = homeTdInfos[5].string
        point.guest5P = guestTdInfos[5].string
        point.homePoint = homeTdInfos[6].string
        point.guestPoint = guestTdInfos[6].string
    elif(len(homeTdInfos) == 8):
        point.home5P = homeTdInfos[5].string
        point.guest5P = guestTdInfos[5].string
        point.home6P = homeTdInfos[6].string
        point.guest6P = guestTdInfos[6].string
        point.homePoint = homeTdInfos[7].string
        point.guestPoint = guestTdInfos[7].string
    elif(len(homeTdInfos) == 9):
        point.home5P = homeTdInfos[5].string
        point.guest5P = guestTdInfos[5].string
        point.home6P = homeTdInfos[6].string
        point.guest6P = guestTdInfos[6].string
        point.home7P = homeTdInfos[7].string
        point.guest7P = guestTdInfos[7].string
        point.homePoint = homeTdInfos[8].string
        point.guestPoint = guestTdInfos[8].string


    #下面开始搞球员数据





if __name__ == '__main__':
    getTeamPoints()