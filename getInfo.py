#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

from InstagramAPI import InstagramAPI
f = open("profile.txt","w")
InstagramAPI = InstagramAPI("Goupuper", "zhao736762141")
InstagramAPI.login()
#3293680605   'vincentcassel',//141668
#vergegirl   ''29360069

InstagramAPI.getUsernameInfo('3322468295')
exa = InstagramAPI.LastJson
print(exa)
InstagramAPI.getProfileData()
print(type(exa['user']['following_count']))
for key in exa['user'].keys():
    f.write(key+'\n')
    print(key+'\n')
acc = json.dumps(exa)
f.write(acc+'\n')
f.close()
