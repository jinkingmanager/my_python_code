#coding=utf-8
#!/usr/bin/python

import os, re
import CommonUtils

url = 'http://nba.sports.sina.com.cn/look_scores.php?id=2006110120'
bs = CommonUtils.getSoupFromUrl(url)

# client and home
teams = bs.find_all("a", 'tlogo')
# client
client = teams[0].string.strip()
# home
home = teams[1].string.strip()
# final points
total_points = bs.find_all("td", "num")

# sec points
sec_points = bs.find_all("td", {"bgcolor": "#000000"})

# date
date = url.split("=")[1][0:8]

print client,home,total_points,sec_points