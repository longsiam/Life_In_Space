# 游戏设置
# version: BETA

from funclib import isFirstRun, read_file

class Setting:
	'''储存游戏设置'''
	def __init__(self):
		self.screen_width = 1050  # 游戏窗口宽度
		self.screen_high = 660    # 游戏窗口高度
		self.start_money = 2000.0 # 玩家起始财产
		self.star_density = 30    # 后生成星星密度
		self.star_edge = 15       # 星星距窗口边框的距离(单位px)
		self.star_quantity = 60   # 一次性生成的星星数量
		self.star_darkest = 45    # 最暗的星星亮度
		self.star_lightest = 230  # 最亮的星星亮度 
		self.star_size = 2        # 星星尺寸(单位px) 
		self.init_dynamic()       # 初始化动态设置
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
