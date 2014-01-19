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

    print len(insertValues)
    print insertValues[0]
    conn = CommonUtils.getConnect()
    cu = conn.cursor()
    cu.executemany(insertSql,insertValues)
    conn.commit()
    conn.close()