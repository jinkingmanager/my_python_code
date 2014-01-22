# coding=utf-8
#!/usr/bin/python
__author__ = 'siyu'

import CommonUtils
import Domain
import DAO

# get team url page content
def getTeamUrlContent():

    teamUrl = "http://g.hupu.com/nba/teams/"
    #teams
    teams = ['Spurs','Rockets','Mavericks','Grizzlies','Pelicans','Clippers',
             'Warriors','Suns','Lakers','Kings','Blazers','Thunder','Nuggets',
             'Timberwolves','Jazz','Raptors','Nets','Knicks','Celtics','76ers',
             'Heat','Hawks','Wizards','Bobcats','Magic','Pacers','Bulls',
             'Pistons','Cavaliers','Bucks']

    teamDic = {}

    for teamName in teams:
        url = teamUrl + teamName
        teamInfo = CommonUtils.getSoupFromUrl(url)
        teamDic[teamName] = teamInfo

    return teamDic

def getTeamInfo():
    teamDic = getTeamUrlContent()

    teamInfo = []
    # get Teaminfo
    for teamName in teamDic:
        team = Domain.Team()
        teamAllName = teamDic[teamName].find_all("h2")[0].string
        names = teamAllName.split(u"（")
        cnName = names[0]
        enName = names[1].replace(u"）", "")
        team.chineseName = cnName
        team.engName = enName
        team.shortName = teamName
        team.city = enName.replace(teamName, "")

        teamInfo.append(team)
        print team.engName
    print len(teamInfo)
    return teamInfo

def saveTeams():
    DAO.insertTeam(getTeamInfo())

if __name__ == '__main__':
    saveTeams()