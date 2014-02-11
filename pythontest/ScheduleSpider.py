#coding:utf-8
__author__ = 'siyu'

import CommonUtils
import Domain
import DAO


def init():
	scheduleUrl = "http://nba.sports.sina.com.cn/match_result.php?day=all"
	return CommonUtils.getSoupFromUrl(scheduleUrl)


def getAllSchedule():
	tempInfo = init().find_all('table', width="950", border="0", align="center")[0]
	allTrInfo = tempInfo.find_all('tr')

	# 当前时间
	curDate = None
	# 当前星期
	curWeek = None
	# 需要插入的比赛数据
	schedules = []
	year = ['2013', '2014']
	for trInfo in allTrInfo:
		# 为标题，需要取当天时间
		if trInfo['bgcolor'] == '#FFD200':
			# date = 10月05日星期六，替换掉月、日
			tempDate = trInfo.find_all('td')[0].getText()
			curWeek = tempDate[-3:]
			curDate = tempDate.replace(curWeek,'').replace(u'月', '-').replace(u'日', '')

			# 截取前两位，获得月份
			curMonth = curDate[0:2]
			# 判断是第一年，还是第二年
			if curMonth == '10' or curMonth == '11' or curMonth == '12':
				curDate = year[0] + '-' + curDate
			else:
				curDate = year[1] + '-' + curDate

		# 为具体比赛，需要取当前数据，不包括比分，只有日期、时间、主队、客队
		else:
			tdInfo = trInfo.find_all('td')
			# 具体时间
			# 比赛对象
			pointInfo = Domain.Point()
			pointInfo.time = tdInfo[0].getText().replace(u'完场', '').replace(u'未赛','')
			pointInfo.date = curDate
			pointInfo.type = tdInfo[1].string
			pointInfo.weekday = curWeek
			pointInfo.guest = tdInfo[2].a.string
			pointInfo.home = tdInfo[4].a.string

			schedules.append(pointInfo)
	# 插入schedule数据
	DAO.insertSchedules(schedules)
