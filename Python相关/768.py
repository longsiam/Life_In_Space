#!/usr/bin/env python
# -*- coding: utf-8 -*-
filename = 'test.txt'
with open(filename) as pai:
	yzls = pai.readlines()
	
yuanzl = ''
for roror in yzls:
	yuanzl += roror.strip()
	
birth = input('请输入你的生日(格式mmdd):  ')
if len(birth) > 4:print("格式不正确!")

if birth in yuanzl:
	print('它在圆周率4412位内出现了')
else:
	print('很遗憾,它不在圆周率4412位内')


