# coding=utf-8
__author__ = 'siyu'
# 球员模型
class Player:
    playerZnName = ''
    playerEngName = ''
    teamName = ''
    location = ''
    height = ''
    weight = ''
    birthday = ''
    money = ''

# 球队模型
class Team:
    engName = ''
    chineseName = ''
    city = ''
    shortName = ''
    subregion = ''


# 球队数据模型
class Point:
    type = ''
    date = ''
    time = ''
    guest = ''
    home = ''
    weekday = ''
    peopleNum = ''
    guestPoint = ''
    homePoint = ''
    guest1P = ''
    guest2P = ''
    guest3P = ''
    guest4P = ''
    guest5P = ''
    guest6P = ''
    guest7P = ''
    home1P = ''
    home2P = ''
    home3P = ''
    home4P = ''
    home5P = ''
    home6P = ''
    home7P = ''
    homeShoot = 0
    homeSucShoot = 0
    homeThree = 0
    homeSucThree = 0
    homeFree = 0
    homeSucFree = 0
    homeFrontBoard = 0
    homeBackBoard = 0
    homeTotalBoard = 0
    homeAssist = 0
    homeFault = 0
    homeSteal = 0
    homeTurnover = 0
    homeBlock = 0
    homeTotalRate = 0.0
    homeThreeRate = 0.0
    homeFreeRate = 0.0
    guestShoot = 0
    guestSucShoot = 0
    guestThree = 0
    guestSucThree = 0
    guestFree = 0
    guestSucFree = 0
    guestFrontBoard = 0
    guestBackBoard = 0
    guestTotalBoard = 0
    guestAssist = 0
    guestFault = 0
    guestSteal = 0
    guestTurnover = 0
    guestBlock = 0
    guestTotalRate = 0.0
    guestThreeRate = 0.0
    guestFreeRate = 0.0




# 球员记录数据模型
class PlayerRecord:
    minutes = ''
    totalShoot = ''
    totalSuc = ''
    threeShoot = ''
    threeSuc = ''
    freeThrow = ''
    freeSuc = ''
    frontBoard = ''
    backBoard = ''
    totalBoard = ''
    assist = ''
    fault = ''
    steal = ''
    turnover = ''
    block = ''
    point = ''
    value = ''
    team = ''
    isHome = ''
    date = ''
    isBench = ''
    name=''

