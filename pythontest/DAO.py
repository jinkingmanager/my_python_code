# coding:utf-8
__author__ = 'siyu'
import Domain
import  sqlite3
import CommonUtils

# 插入球员基础数据
def insertPlayer(players):
    insertSql = "insert into player(player_zn_name,player_eng_name,team,location,height,weight,birthday,money) values(" \
                "?,?,?,?,?,?,?,?)"

    insertValues = []
    for player in players:
        value = (player.playerZnName,player.playerEngName,player.teamName,player.location,player.height,player.weight,player.birthday,player.money)
        insertValues.append(value)

    conn = CommonUtils.getConnect()
    cu = conn.cursor()
    # before insert,delete data that is older
    cu.execute("delete from player")
    # insert player data
    cu.executemany(insertSql,insertValues)
    conn.commit()
    conn.close()

# 插入球队基础数据
def insertTeam(teams):
    insertSql = "insert into team(eng_name,chinese_name,city,short_name) values(?,?,?,?)"

    insertValues = []
    for team in teams:
        value = (team.engName, team.chineseName, team.city, team.shortName)
        insertValues.append(value)

    conn = CommonUtils.getConnect()
    cu = conn.cursor()
    cu.execute("delete from team")
    cu.executemany(insertSql, insertValues)
    conn.commit()
    conn.close()

# 插入赛程数据，仅包含日期、时间、主队、客队
def insertSchedules(schedules):
	insertSql = "insert into point(type,date,time,weekday,guest,home) values (?,?,?,?,?,?)"

	insertValus = []
	for point in schedules:
		schedule = (point.type,point.date,point.time,point.weekday,point.guest,point.home)
		insertValus.append(schedule)

	conn = CommonUtils.getConnect()
	cu = conn.cursor()
	cu.execute("delete from point")
	cu.executemany(insertSql,insertValus)
	conn.commit()
	conn.close()

# 插入比赛数据，包括球队数据及球员数据
