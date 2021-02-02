# 游戏设置
# version: BETA

from funclib import isFirstRun, read_file

class Setting:
	'''储存游戏设置'''
	def __init__(self):
		self.screen_width=1050  # 游戏窗口宽度
		self.screen_high=660    # 游戏窗口高度
		self.start_money=2000.0 # 玩家起始财产
		self.init_dynamic()     # 初始化动态设置
	def init_dynamic(self):
		'''初始化动态设置'''
		if isFirstRun():
			self.player_maxhp=100  # 玩家血量最大值 
		else:
			data=read_file()["setting"]
			self.player_maxhp=data["pmaxhp"]
	def get_dynamic(self) -> dict:
		'''
		获取动态设置
		返回值：动态设置字典
		'''
		return {"pmaxhp":self.player_maxhp}
