__author__ = 'siyu'
import Domain
import  sqlite3
import CommonUtils

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