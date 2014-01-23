# coding = utf-8
__author__ = 'siyu'

import CommonUtils
import Domain

def init():
    scheduleUrl = "http://nba.sports.sina.com.cn/match_result.php?day=all"
    return CommonUtils.getSoupFromUrl(scheduleUrl)

def getAllSchedule():
    tempInfo = init().find_all('table980middle')
    tableInfo = tempInfo.find('table')





if __name__ == '__main__':
    print getAllSchedule()