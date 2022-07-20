#!/usr/bin/python
#coding=utf-8

import json
import sys
import os
import datetime
import commands
import time


#测试中发现一种现象：
#pauth.ini中的编码和下载证书时候并不一致，会导致下载证书失败，脚本失效
def updateCert():

    #设置语言环境,主要是为了下面截取一个到期时间
    os.system("echo LANG=zh_CN.GB2312 > /etc/locales.conf")
    os.system("source /etc/locales.conf")

    #截取证书的编码，省略M11等字眼
    authCode = commands.getoutput("cat /root/mobile/mobiwt/pcert/pauth.ini "
                                  "| grep M41= | awk -F 'M41' '{print $3}'")
    # print authCode
    #判断如果编码没截取出来直接报错
    if authCode is None:
        print json.dumps({
            "failed": True,
            "msg": "Can not catch the cert code ! Please check pauth.ini!"
        }
        )
        sys.exit(1)

    #停止手机主站
    os.system('sh /root/mobile/stop.sh')
    #获取主机名称
    hostName = commands.getoutput("hostname")
    #print hostName
    #获取下今天的日期，到日为止
    today = str(datetime.datetime.now().strftime('%y%m%d'))
    # print today

    #定义一堆后续拼凑命令要用的变量，以及mobiList数组
    mobiPath = '/root/mobile/'
    mobiWget = 'nohup wget -t 10 -O /root/mobile/'
    certUrl = 'http://services.myhexin.com/produser/downloadcert?libver=20030506&authcode='
    submitCode = '&Submit=%CF%C2%D4%D8%D6%A4%CA%E9'
    pauthPath = '/pcert/pauth.ini'
    mobiList = [['mobigw', 'M11'], ['mobiauth', 'M21'], ['mobihq', 'M31'],
                ['mobiwt', 'M41']]
    #遍历mobiList，拼凑备份pauth.ini和下载证书的命令，并执行
    for m in mobiList:

        mobiBakCmd = 'mv ' + mobiPath + m[0] + pauthPath + ' ' + mobiPath + m[0] \
                     + pauthPath + today
        #print mobiBakCmd
        resBak = os.system(mobiBakCmd)

        downloadCmd = mobiWget + m[0] + '/pcert/' + m[1] + '.dat ' + '"' + certUrl \
                    + m[1] + authCode + submitCode + '"'
        #print downloaCmd
        resDw = os.system(downloadCmd)
    #启动手机主站
    resRst = os.system('nohup sh /root/mobile/mobi.sh')
    time.sleep(3)
    #截图更新后的证书到期时间
    deadDate = commands.getoutput("cat /root/mobile/mobiwt/pcert/pauth.ini "
                                  "| grep 证书截止日期 | awk -F '=' '{print $2}'")
    #print deadDate
    #返回参数，有执行命令的状态，主机名，认证码，到期时间
    return resBak , resDw , resRst , hostName , authCode , deadDate

if __name__ == '__main__':
    #运行updateCert方法，获取返回的参数
    (resBak , resDw , resRst , hostName , authCode , deadDate) = updateCert()
    #根据参数做判断，不同的情况返回不同的json.dumps，提供给ansible运行的结果
    if resBak != 0:
        print json.dumps({
            "failed": True,
            "msg": "Backup pauth.ini faild! Please check!"
        }
        )
        sys.exit(1)
    elif resDw != 0:
        print json.dumps({
            "failed": True,
            "msg": "Download cert faild! Please check network!"
        }
        )
        sys.exit(1)
    elif resRst != 0:
        print json.dumps({
            "failed": True,
            "msg": "Restart failed ! Please check!"
        }
        )
        sys.exit(1)
    elif deadDate is None:
        print json.dumps({
            "failed": True,
            "msg": "DeadDate Null ! Please check!"
        }
        )
        sys.exit(1)
    else:
        print json.dumps({
            "successful": True,
            "hostName": hostName,
            "authCode": authCode,
            "deadDate": deadDate
        }
        )













