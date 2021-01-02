#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:18:40 2021

@author: MrinalTyagi
"""

import fbchat 
from fbchat import Client
"""from getpass import getpass"""
import maskpass
password=maskpass.advpass()
username = "mrinaltyagi1912"
client =  fbchat.Client(username, password)
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name of friend: "))
    friends = client.getUsers(name)
    friend = friends[0]
    msg = str(input("Message: Happy New Year! May this year brings lot of joy in your life"))
    sent = client.send(friend.uid, msg)
    if sent:
        print("Message sent successfully")
        
       
        
        
        
        
        
        