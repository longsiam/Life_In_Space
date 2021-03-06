# 统计信息
# version: BETA

from funclib import read_file, isFirstRun
from global_vars import *

class Stats:
	'''游戏的统计信息'''
	def __init__(self):
		self.active_states = 0                           # 游戏活动状态，0为活动，1为暂停
		if isFirstRun():
			self.exp = 0                                 # EXecution Point
			self.money = datpck["setting"].start_money   # 财产
			self.hp = datpck["setting"].player_maxhp     # 血量
		else:
			data = read_file()["stats"]
			self.exp = data["exp"]
			self.money = data["money"]
			self.hp = data["hp"]

	def get_longterm(self) -> dict:
		'''
		获取长期保存的统计信息
		返回值：长期统计信息的字典
		'''
		return {"exp":self.exp, "money":self.money, "hp":self.hp}

	def __repr__(self):
		'''如果被当字符串使就返回长期信息（报错用）'''
		return repr(self.get_longterm())
