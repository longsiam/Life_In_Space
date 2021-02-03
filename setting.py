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
		self.star_quantity = 75   # 一次性生成的星星数量
		self.star_darkest = 45    # 最暗的星星亮度
		self.star_lightest = 230  # 最亮的星星亮度 
		self.star_size = 2        # 星星尺寸(单位px) 
		self.fade_time = 1        # 淡入/淡出所需时间
		# 星星颜色RGB值表
		self.star_color = lambda light: (
			(  light,    light,   light  ),  # 白色
			(  light,    light,   light  ),  # 为让白色星星更多，
			(  light,    light,   light  ),  # 突出彩色星星，增加权重
			(  light,    light,   light  ),  # 突出彩色星星
			(  light,    light,   light  ),  # 所以多设几个白色
			(  light,    light,   light  ),  # 增加权重到2/3
			(  light,   light/2, light/2 ),  # 红色
			( light/2,  light/2,  light  ),  # 蓝色
			(  light,    light,  light/2 )   # 黄色
		)
		self.init_dynamic()       # 初始化动态设置

	def init_dynamic(self):
		'''初始化动态设置'''
		if isFirstRun():
			self.player_maxhp = 100  # 玩家血量最大值 
			self.volume = 0.8        # 音响音量
		else:
			data=read_file()["setting"]
			self.player_maxhp = data["pmaxhp"]
			self.volume = data["volume"]
			
	def get_dynamic(self) -> dict:
		'''
		获取动态设置
		返回值：动态设置字典
		'''
		return {"pmaxhp":self.player_maxhp, "volume":self.volume}

	def __str__(self):
		'''如果被当成字符串，那就返回动态设置的字符串（报错时要用）'''
		return str(get_dynamic())
