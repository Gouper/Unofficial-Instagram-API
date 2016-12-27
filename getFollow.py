#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("Goupuper", "zhao736762141")
InstagramAPI.login()
#3293680605   'vincentcassel',//141668
#vergegirl   ''29360069
InstagramAPI.getUsernameInfo('1275759271')
exa = InstagramAPI.LastJson
print(exa)
#InstagramAPI.getUserFollowers()