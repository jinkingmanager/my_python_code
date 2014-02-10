# coding=utf-8
__author__ = 'siyu'
import CommonUtils
import Domain
import DAO

#get All teams info using for loop
def getTeamsInfo():
    #base url
    url = "http://g.hupu.com/nba/players/"
    #teams
    teams = ['Spurs','Rockets','Mavericks','Grizzlies','Pelicans','Clippers',
             'Warriors','Suns','Lakers','Kings','Blazers','Thunder','Nuggets',
             'Timberwolves','Jazz','Raptors','Nets','Knicks','Celtics','76ers',
             'Heat','Hawks','Wizards','Bobcats','Magic','Pacers','Bulls',
             'Pistons','Cavaliers','Bucks']
    #team dictionary
    teamDic = {}

    #get all html info divide by teamName
    for team in teams:
        teamUrl = url + team
        teamPlayerInfos = CommonUtils.getSoupFromUrl(teamUrl)
        teamDic[team] = teamPlayerInfos
    return teamDic

#Get All Players Info
def getPlayersInfo():

    teamDic = getTeamsInfo()

    playerList = []

    # for loop to get one team player using tbody
    for teamName in teamDic:
        playerInTeam = teamDic[teamName].find("tbody")
        for players in playerInTeam.find_all("tr"):
            #print len(players)
            myplayer = Domain.Player()
            playerInfo = players.find_all("td")
            if cmp("姓名".decode("utf8"),playerInfo[1].string) == 0:
                continue
            if(len(playerInfo) == 8):
                aLinkInfo = playerInfo[1].find_all("a")
                bInfo = playerInfo[1].find_all("b")
                if len(aLinkInfo) > 0:
                    if(aLinkInfo[0].string != None):
                        myplayer.playerZnName = aLinkInfo[0].string
                        myplayer.playerEngName = bInfo[1].string.replace(')','')


                myplayer.location = playerInfo[3].string
                myplayer.height = playerInfo[4].string
                myplayer.weight = playerInfo[5].string
                myplayer.birthday = playerInfo[6].string
                myplayer.money = playerInfo[7].getText('left').replace('left',',')
                myplayer.teamName = teamName

                playerList.append(myplayer)

    print len(playerList)
    return playerList

#save player
def savePlayers():
    playerList = getPlayersInfo()
    DAO.insertPlayer(playerList)

