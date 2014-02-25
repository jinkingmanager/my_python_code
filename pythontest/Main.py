#coding=utf-8
__author__ = 'siyu'

import playerSpider
import PointSpider
import ScheduleSpider
import teamSpider

if __name__ == '__main__':
    #球员数据抓取
    playerSpider.savePlayers()

    #球队数据抓取
    #teamSpider.saveTeams()

    #赛程数据抓取
    #ScheduleSpider.getAllSchedule()

    # 比赛数据抓取
    #PointSpider.getTeamPoints()