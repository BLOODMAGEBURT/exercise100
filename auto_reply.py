#!/usr/bin/python
# -*- coding: utf-8 -*
import itchat
from itchat.content import *


itchat.auto_login(hotReload=True)

user = itchat.search_friends(name=u'初长成')
userName = user[0]['UserName']
# itchat.send('hello my darling', toUserName='filehelper')


@itchat.msg_register(TEXT)
def print_content(msg):
    # print msg.text
    itchat.send_msg(msg.text, toUserName=userName)
    # itchat.send_msg(u'已收到的信息：%s，发送者为：%s'%(msg.text,msg['FromUserName']), toUserName=msg['FromUserName'])


itchat.run()
