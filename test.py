#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import time

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("johnstone7523", "zhao736762141")
InstagramAPI.login() # login

f = open("info.txt","w+")
usernameId = ['1275759271','535065013']

InstagramAPI.getUsernameInfo('29360069')
exa = InstagramAPI.LastJson
for key in exa['user'].keys():
    f.write(key+'\n')
    print(key+'\n')
acc = json.dumps(exa)
f.write(acc+'\n')


g = open('testFinal.txt', 'w+')
for i in usernameId:
    index2 = 1
    time1 = 1
    followers = []
    next_max_id = ''
    while 1:
        InstagramAPI.getUserFollowers(i, next_max_id)
        temp = InstagramAPI.LastJson

        for item in temp["users"]:
            followers.append(item)
            person = json.dumps(item)
            userid = item["pk"]
            userids = '%d' % userid
            g.write(userids)
            g.write(person + '\n')
            print(item)
            print(index2)
            index2 = index2 + 1
        if temp["big_list"] == False:
            break
        if next_max_id == temp["next_max_id"] :
            time1 =time1 +1
        else :
            time1 = 1
        next_max_id = temp["next_max_id"]
        print(next_max_id)
        if time1 == 10:
            print("Now the program sleep 60s!Please wait a moment!")
            time.sleep(180)
            time1 = 1
    s = 'This is  the followers of someone!'
    g.write(i+'    ')
    g.write(s + '\n')
#AQAlifT_ar8JO_cgirPhGUaa5O-MgZc7l9Jk_SvNaKS-fAzyvTwN0FrXR8E2AtvJEnQLyIpIpStGtaEQEIQM1oAY_Ln3rWptJg31EGAel4h-TPsOZmK-2G46pb6iobBlwuE

g.close()


















