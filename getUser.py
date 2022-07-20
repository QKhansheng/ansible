#!/usr/bin/python

import os
import json
import sys

#获取当前的用户，判断是不是root
def getUser():

    userID = os.geteuid()
    return userID

if __name__ == '__main__':
    userid = getUser()
    if userid == 0:
        print json.dumps({
            "successful": True,
            "msg": "The current user is ROOT!"
        }
        )
        sys.exit(1)
    else:
        print json.dumps({
            "successful": True,
            "msg": "The current user is not ROOT!"
        }
        )