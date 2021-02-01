# function library of LifeInSpace
# version: BETA_00
import os
import sys
import pygame

def quit_game(datpck: dict):
	'''
	安全退出游戏
	datpck: 游戏数据包
	'''
	save_file(datpck)  # 先存档
	sys.exit(0)        # 退出码为0：安全退出

def encry(target: str) -> str:
	'''
	加密一段字符串
	target: 要加密的字符串
	返回值: 加密后的字符串
	'''
	return "".join(reversed([chr((ord(x)^3)+5) for x in target]))

def decry(target: str) -> str:
	'''
	解密一段字符串
	target: 被加密的字符串
	返回值: 解密后的字符串
	'''
	return "".join(reversed([chr((ord(x)-5)^3) for x in target]))

def save_file(datpck: dict):
	'''
	将数据存档
	datpck: 游戏数据包
	'''
	# os.getcwd()能获取当前路径
	# .dat文件其实就是普通的文本文件换了个后缀, player.dat是游戏存档文件
	with open(os.getcwd()+r"\player.dat", "w") as f:
		# 将统计信息与进度描述放入一个元组，加密写入存档中
		f.write(encry(str((datpck["stats"].get(), datpck["progress"]))))

def read_file() -> tuple:
	'''
	读取存档
	返回值：统计信息与进度的元组
	'''
	with open(os.getcwd()+r"\player.dat", "r") as f:
		# 解密后读得的仍是字符串，我们要eval一下才是真正的元组
		return eval(decry(f.read()))
