#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
import xmltodict
import json

def checkWtserver():

      #定义连接的url，这里就直接用东吴测试环境的，各家可能url不同
      url = 'http://192.250.130.32:8080/cgiwt?cmd=cmd_verifyuser&yyb_ip=192.250.130.32&' \
            'yyb_port=8005&yyb_id=0600&lg_account=060000001518&lg_account_type=0&' \
            'lg_tradepwd=654321&lg_commpwd=1'

      try:
            #打开url并将返回写到page里，用浏览器直接打开的话可以发现是一个xml文件(page_xml)
            #先对返回的xml文件进行重编码成utf-8(page_dict),再转换成字典的数据形式,
            #再转成json格式(page_json),嵌套遍历下params_json,发现是个多层的json，
            #先遍历items，再遍历items的vaule，找到ret_code就是请求委托返回的状态符
            #根据状态符进行判定,当然如果一开始就产生exception的话，就基本是网关也连上
            response = urlopen(url)
            page = response.read()
            response.close()
            #print page
            page_xml = page.decode('gbk').encode('utf-8')
            #print page_xml

            page_dict = xmltodict.parse(page_xml, encoding='utf-8')
            #print page_dict

            page_json = json.dumps(page_dict, indent=2)
            #print page_json
            params_json = json.loads(page_json)
            #print params_json

            items = params_json.items()
            #print items

            for key,value in items:
                  #print(str(key) + '=' + str(value))
                  ret_code = value.items()
                  for k,v in ret_code:
                        #print (str(k) + '=' + str(v))
                        if (k == 'ret_code' and v == '-1008'):
                              print (str(k) + '=' + str(v))
                              print u"连接委托主站失败！请检查网络或者尝试重启程序!"
                        elif (k == 'ret_code' and v == '0'):
                              print (str(k) + '=' + str(v))
                              print u"请求成功，委托主站正常!"
      except:
            print u"连接委托网关异常！请检查网络或者尝试重启程序!"

if __name__ == '__main__':
      checkWtserver()






