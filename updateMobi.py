#!/usr/bin/python
#coding=utf-8

import os
import json
import sys

def updateMobi():

    jenkins_host = '192.250.110.111'
    mobi_git_path = '/hexin/mobile/mobile.git'
    pull_cmd = 'cd /hexin/mobile/mobile.git && ' \
               'git pull ' + 'root@' + jenkins_host + ':/hexin/mobile/mobile.git'
    #print pull_cmd
    ln_cmd = 'cd /hexin/mobile/mobile.git/mobile && sh ln.sh'
    #ln_cmd = 'echo hello'
    stop_cmd = 'sh /root/mobile/stop.sh'
    start_cmd = 'nohup sh /root/mobile/mobi.sh'
    pull_status = os.system(pull_cmd)
    #print pull_status
    ln_status = os.system(ln_cmd)
    #print ln_status
    stop_status = os.system(stop_cmd)
    start_status = os.system(start_cmd)
    #print start_status

    return pull_status , ln_status , start_status

if __name__ == '__main__':

    (pull_status , ln_status , start_status) = updateMobi()

    if pull_status is not 0:
        print json.dumps({
            "faild" : True ,
            "msg" : "Git pull faild! Please check!"
        })
        sys.exit(1)
    elif start_status is not 0:
        print json.dumps({
            "faild" : True ,
            "msg" : "Restart mobi faild!Please check!"
        })
        sys.exit(1)
    else:
        print json.dumps({
            "successful" : True ,
            "msg" : "Update successful!"
        })



