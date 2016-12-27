#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("johnstone7523", "zhao736762141")
InstagramAPI.login() # login

f = open("info.txt","w+")
usernameId = '29360069'
#InstagramAPI.tagFeed("cat") # get media list by tag #cat
#media_id = InstagramAPI.LastJson # last response JSON
#InstagramAPI.like(media_id["ranked_items"][0]["pk"]) # like first media
#InstagramAPI.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"]) # get first media owner followers

InstagramAPI.getUsernameInfo('29360069')
exa = InstagramAPI.LastJson
for key in exa['user'].keys():
    f.write(key+'\n')
    print(key+'\n')
acc = json.dumps(exa)
f.write(acc+'\n')
#InstagramAPI.getTotalFollowings('243575783')
InstagramAPI.getTotalFollowings('3322468295')
#print(len(InstagramAPI.getTotalSelfFollowings()))
#print(len(InstagramAPI.getTotalFollowers('4105645240')))
#InstagramAPI.getTotalFollowings('29360069')
#InstagramAPI.getTotalFollowers('3293680605')
#InstagramAPI.getTotalFollowers('195860627')
#print(len(InstagramAPI.getTotalFollowings('27688175')))
#print(len(InstagramAPI.getTotalFollowings('1650021516')))
f.close()
#王昌裕  3322468295