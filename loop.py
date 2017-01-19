#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import pymysql
from InstagramAPI import InstagramAPI

def followings_remove_duplicates(ID):
    next_max_id = ''
    time1 = 1
    index = 1
    sql = "REPLACE INTO remove_dup(userID,pk)VALUES (%s,%s)"
    while 1:
        InstagramAPI.getUserFollowings(ID, next_max_id)
        temp = InstagramAPI.LastJson
        for item in temp["users"]:
            userID = item["pk"]
            fID = str(ID)
            userIDS = str(userID)
            param = (fID, userIDS)
            cur.execute(sql,param)
            conn.commit()
        print(index)
        index = index +1
        if temp["big_list"] == False:
            break
        if next_max_id == temp["next_max_id"]:
            time1 = time1 + 1
        else:
            time1 = 1
        next_max_id = temp["next_max_id"]
        print(next_max_id)
        if time1 == 20:
            print("Now the program sleep 180s!Please wait a moment!")
            time.sleep(180)
            time1 = 1
    print("Completed remove the duplicate!")

def followers_remove_duplicates(ID):
    next_max_id = ''
    time1 = 1
    index = 1
    sql = "replace into remove_dup(userID,pk)VALUES (%s,%s)"
    while 1:
        InstagramAPI.getUserFollowers(ID, next_max_id)
        temp = InstagramAPI.LastJson
        for item in temp["users"]:
            userID = item["pk"]
            param = (ID, userID)
            cur.execute(sql,param)
            conn.commit()
        print(index)
        index = index + 1
        if temp["big_list"] == False:
            break
        if next_max_id == temp["next_max_id"]:
            time1 = time1 + 1
        else:
            time1 = 1
        next_max_id = temp["next_max_id"]
        print(next_max_id)
        if time1 == 20:
            print("Now the program sleep 180s!Please wait a moment!")
            time.sleep(180)
            time1 = 1
    print("Completed remove the duplicate!")

def getTotalFollowing(category,num):
    print("Push the data to the followings from remove_dup!")
    sql1 = "select * from remove_dup"
    sql2 = "insert into followings(num, userID, followingID, category, mark)VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql1)
    results = cur.fetchall()
    for row in results:
        userID = row[0]
        followingID = row[1]
        mark = 'A'
        param = (num, userID, followingID, category, mark)
        cur.execute(sql2, param)
        conn.commit()
        num = num + 1
    print("It has been put the message to followings database!")
    return num

def getTotalFollower(category,num):
    print("Push the data to the followers from remove_dup!")
    sql1 = "select * from remove_dup"
    sql2 = "insert into followers(num, userID, followerID, category, mark)VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql1)
    results = cur.fetchall()
    for row in results:
        userID = row[0]
        followingID = row[1]
        mark = 'A'
        param = (num, userID, followingID, category, mark)
        cur.execute(sql2, param)
        conn.commit()
        num = num + 1
    print("It has been put the message to followers database!")
    return num

def getUserCount(ID):
    count = []
    InstagramAPI.getUsernameInfo(ID)
    exa = InstagramAPI.LastJson
    follower_count = exa['user']['follower_count']
    count.append(follower_count)
    following_count = exa['user']['following_count']
    count.append(following_count)
    return count
def getUserProfile(ID):
    InstagramAPI.getUsernameInfo(ID)
    exa = InstagramAPI.LastJson
    username = exa['user']['username']
    full_name = exa['user']['full_name']
    is_verified = exa['user']['is_verified']
    follower_count = exa['user']['follower_count']
    following_count = exa['user']['following_count']
    sql = "insert into userProfile(userID, username, full_name, is_verified, follower_count, following_count)VALUES (%s,%s,%s,%s,%s,%s)"
    param = (ID, username, full_name, is_verified, follower_count, following_count)
    cur.execute(sql, param)
    conn.commit()
def delete_sql():
    sql = "delete from remove_dup"
    cur.execute(sql)
    conn.commit()
    print("It has been delete the sql!")
def followingsNum():
    sql = "select * from followings"
    cur.execute(sql)
    num = int(cur.rowcount) + 1
    return num
def followersNum():
    sql = "select * from followers"
    cur.execute(sql)
    num = int(cur.rowcount) + 1
    return num
def get_follower_ID(cate):
    followerID = []
    sql = "select * from followers WHERE category='%s' AND mark='A' " % (cate)
    cur.execute(sql)
    results = cur.fetchall()
    for item in results:
        a = int(item[2])
        followerID.append(a)
    return followerID
def get_following_ID(cate):
    followingID = []
    sql = "select * from followings WHERE category='%s' AND mark='A' " % (cate)
    cur.execute(sql)
    results = cur.fetchall()
    for item in results:
        a = int(item[2])
        followingID.append(a)
    return followingID
def findID(ID):
    sql = "select * from userProfile WHERE userID='%s'"%(str(ID))
    cur.execute(sql)
    if int(cur.rowcount) == 1:
        return True
    else:
        return False



if __name__ == "__main__":
    InstagramAPI = InstagramAPI("johnstone7523", "zhao736762141")
    InstagramAPI.login()  # login
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='instagram', port=3306)
    cur = conn.cursor()
    cate_get = 0
    cate_push = 1
    follower_num = followersNum()
    following_num = followingsNum()
    while 1:
        followers = get_follower_ID(cate_get)
        followings = get_following_ID(cate_get)
        for item in followers:
            count = getUserCount(item)
            #如果userProfile表中没有这个ID，则读；如果有则更新状态
            if findID(item): #如果已经读取过了更新成B
                sql = "update followers set mark='B' WHERE followerID='%s'"%(str(item))
                print("It has been read the person's relationship!  Follower")
                cur.execute(sql)
                conn.commit()
            elif (count[0]>1000000 or count[1]>1000000):#如果大于100万则更新成C
                sql1 = "update followers set mark='C' WHERE followerID='%s'" % (str(item))
                print("The person's relationship is too large,so it will read at last! Follower")
                cur.execute(sql1)
                conn.commit()
            else:
                delete_sql()
                followers_remove_duplicates(item)
                a = getTotalFollower(cate_push, follower_num)
                follower_num = a
                delete_sql()
                followings_remove_duplicates(item)
                b = getTotalFollowing(cate_push, following_num)
                following_num = b
                getUserProfile(item)
                sql = "update followers set mark='B' WHERE followerID='%s'" % (str(item))
                print("It has been read one person!")
                cur.execute(sql)
                conn.commit()
                cate_push = cate_push + 1
        for item in followings:
            count = getUserCount(item)
            # 如果userProfile表中没有这个ID，则读；如果有则更新状态
            if findID(item):  # 如果已经读取过了更新成B
                sql = "update followings set mark='B' WHERE followingID='%s'" % (str(item))
                print("It has been read the person's relationship! Following")
                cur.execute(sql)
                conn.commit()
            elif (count[0] > 1000000 or count[1]>1000000):
                sql1 = "update followings set mark='C' WHERE followingID='%s'" % (str(item))
                print("The person's relationship is too large,so it will read at last! Following")
                cur.execute(sql1)
                conn.commit()
            else:
                delete_sql()
                followers_remove_duplicates(item)
                a = getTotalFollower(cate_push, follower_num)
                follower_num = a
                delete_sql()
                followings_remove_duplicates(item)
                b = getTotalFollowing(cate_push, following_num)
                following_num = b
                getUserProfile(item)
                sql = "update followings set mark='B' WHERE followerID='%s'" % (str(item))
                print("It has been read one person!")
                cur.execute(sql)
                conn.commit()
                cate_push = cate_push +1
    cate_get = cate_get + 1

