#coding=utf-8
#!/usr/bin/python
__author__ = 'siyu'

import sqlite3


point_ddl_sql = """create table point(id integer primary key autoincrement,
                        date varchar(30),time varchar(10), guest varchar(40),
                        home varchar(40),guest_point integer(3),home_point integer(3),guest_1_point integer(2),
                        guest_2_point integer(2),guest_3_point integer(2),guest_4_point integer(2),
                        guest_5_point integer(2),guest_6_point integer(2),guest_7_point integer(2),
                        home_1_point integer(2),home_2_point integer(2),home_3_point integer(2),home_4_point integer(2),
                        home_5_point integer(2),home_6_point integer(2),home_7_point integer(2)) """

team_ddl_sql = """create table team(id integer primary key autoincrement,eng_name varchar(40),
                    chinese_name varchar(40),city varchar(40),short_name varchar(20),extend varchar(512))"""

side_ddl_sql = """create table sides(id integer primary key autoincrement,date varchar(30),
                      guest_short_name varchar(20),home_short_name varchar(20),sides1 varchar(100),sides2 varchar(100),
                      sides3 varchar(100),sides4 varchar(100),sides5 varchar(100))"""

total_ddl_sql = """create table totals(id integer primary key autoincrement,date varchar(30),
                       guest_short_name varchar(20), home_short_name varchar(20),totals1 varchar(100),
                       totals2 varchar(100),totals3 varchar(100),totals4 varchar(100),totals5 varchar(100)) """

team_alter_sql1 = """alter table team add column subregion varchar(30) """

player_ddl_sql = """ create table player(id integer primary key autoincrement,player_zn_name varchar(40),
                    player_eng_name varchar(50),team(11),location varchar(10),height varchar(5),
                    weight varchar(10),birthday varchar(10),money varchar(100))"""

player_record_ddl_sql = """ create table player_record(id integer primary key autoincrement,minutes integer(2),
                            total_shoot varchar(10),three_shoot varchar(10),free_throw varchar(10),front_board integer(2),
                            back_board integer(2),total_board integer(2),assist integer(2),fault integer(1),steal integer(2),
                            turnover integer(2),block integer(2),point integer(2),value varchar(3))"""

player_record_alter_sql = """alter table player_record add column team varchar(40),is_home varchar(5),date varchar(30),is_bench varchar(1)"""

cx = sqlite3.connect("nba.db")
cu = cx.cursor()
#cu.execute(team_alter_sql1)

#cu.execute(point_ddl_sql)
#cu.execute(team_ddl_sql)
#cu.execute(side_ddl_sql)
#cu.execute(total_ddl_sql)
#cu.execute(player_ddl_sql)
cu.execute(player_record_ddl_sql)
cu.execute(player_record_alter_sql)
cu.close()
