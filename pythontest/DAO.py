#coding=utf-8
__author__ = 'siyu'
import Domain
import  sqlite3
import CommonUtils

# 插入球员基础数据
def insertPlayer(players):
    insertSql = "insert into player(player_zn_name,player_eng_name,team,location,height,weight,birthday,money) " \
                "values(""?,?,?,?,?,?,?,?)"
    selectSql = "select * from player where player_eng_name = ? and birthday=?"
    updateSql = "update player set team=?,location=?,height =?,weight=?,birthday=?,money=?,player_zn_name=? where player_eng_name=? and birthday=?"

    conn = CommonUtils.getConnect()
    cu = conn.cursor()

    #cu.execute("delete from player")

    insertValues = []
    updateValues = []
    for player in players:
        # 先判断是否存在此球员
        cu.execute(selectSql, (player.playerEngName, player.birthday))
        result = cu.fetchall()
        if(len(result) == 0):
            #若不存在，则直接插入
            insertValues.append((player.playerZnName, player.playerEngName, player.teamName, player.location, player.height, player.weight, player.birthday, player.money))
        else:
            # 若存在，则直接更新即可
            updateValues.append((player.teamName,player.location,player.height,player.weight,player.birthday,player.money,player.playerZnName,player.playerEngName,player.birthday))

    # before insert,delete data that is older
    #cu.execute("delete from player")
    # insert player data
    print "新增数据" + str(len(insertValues))
    print "更新数据" + str(len(updateValues))
    cu.executemany(insertSql,insertValues)
    cu.executemany(updateSql,updateValues)
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
