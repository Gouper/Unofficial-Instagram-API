#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='instagram',port=3306)
cur = conn.cursor()
f = open("followers.txt","r")
index = 1
sql = "REPLACE INTO followers(userID,followerID,mark)VALUES(479323979,%s,0) "

for line in f.readlines()[0:]:
    a = int(line)
    print(a)
    print (index)
    cur.execute(sql, a)
    index = index + 1

conn.commit()
conn.close()
