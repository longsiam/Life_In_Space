# 可能被其他文件修改的全局变量与常用库
# version: BETA

# 导入常用的库
try:
	import pygame
except ImportError:
	# 这个是第三方库，如果没安装就开pip安装
	from pip._internal import main
	main.main(["install","pygame"])
from os import system, getcwd
from threading import Thread
from time import sleep
from random import randint,choice


datpck = {}
def change_datpck(key,value):
	'''
	为避免其他文件无法更改datpck的尴尬，所以有了这个函数
	key:   要改什么
	value: 要改成什么
	'''
	global datpck
	datpck[key] = value
