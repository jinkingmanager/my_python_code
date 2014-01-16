__author__ = 'siyu'
import Domain
import  sqlite3
import CommonUtils

def insertPlayer(player):
    insertSql = "insert into player(player_zn_name,player_eng_name,team,location,height,weight,birthday,money) values("\
    +player.playerZnName+","+player.playerEngName+","+player.teamName+","\
    +player.location+","+player.height+","+player.weight+","\
    +player.birthday+","+player.money+")"

    print insertSql
    cu = CommonUtils.getCursor()
    cu.execute(insertSql)
    cu.close()

if __name__ == '__main__':
    insertPlayer(Domain.Player)