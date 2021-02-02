# 函数库
# version: BETA
import os
import sys
import pygame

def quit_game(datpck: dict):
	'''安全退出游戏'''
	save_file(datpck)  # 先存档
	sys.exit(0)        # 退出码为0：安全退出

def encry(target: str) -> str:
	'''
	加密一段字符串
	target: 要加密的字符串
	返回值: 加密后的字符串
	'''
	return "".join(reversed([chr((ord(x)^3)+15) for x in target]))

def decry(target: str) -> str:
	'''
	解密一段字符串
	target: 被加密的字符串
	返回值: 解密后的字符串
	'''
	return "".join(reversed([chr((ord(x)-15)^3) for x in target]))

def save_file(datpck: dict):
	'''将数据存档'''
	# os.getcwd()能获取当前路径
	# .dat文件其实就是普通的文本文件换了个后缀, player.dat是游戏存档文件
	with open(os.getcwd()+r"\data\player.dat", "w", encoding="utf-8") as f:
		# 将统计信息与进度描述放入一个字典，加密写入存档中
		f.write(encry(str(
			{
				"stats":datpck["stats"].get_longterm(), 
				"progress":datpck["progress"], 
				"setting":datpck["setting"].get_dynamic()
			}
		)))

def read_file() -> tuple:
	'''
	读取存档
	返回值：统计信息与进度的元组
	'''
	with open(os.getcwd()+r"\data\player.dat", "r", encoding="utf-8") as f:
		# 解密后读得的仍是字符串，要eval一下才是真正的元组
		return eval(decry(f.read()))

def handle_event(datpck: dict):
	'''监听+处理事件'''
	for event in pygame.event.get():
		# 监听是否按下×，按下就退出
		if event.type == pygame.QUIT:
			quit_game(datpck)

def isFirstRun() -> bool:
	'''
	检查是否为第一次运行
	返回值：是否第一次运行，是为True
	'''
	return not os.path.exists(os.getcwd()+r'\data\firstrun')

def show_start_cg(datpck: dict):
	'''展示起始的剧情CG'''
	'''
	# 假如关闭游戏前存档不是在播放sCG，就更改进度
	if datpck["progress"][:3]!="sCG":
		datpck["progress"]="sCG:0"
	# CG图配文，没有配文就直接用空字符串
	cgtext=("3020年 地球...\n太阳系文明高度发达，人类都说普通话，但并不知道外星人的存在...",)
	# CG图对象列表
	cg_list=[]
	# 将"sCG:n"用':'分开，倒数第一个就是要开始播放的那个图的序号
	for i in range(int(datpck["progress"].split(":")[-1]), len(cgtext)):
	'''
	# 暂时先放着，下个版本再写完
	pass
