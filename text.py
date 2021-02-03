# 文本显示
# version: BETA

import pygame
from global_vars import *

class Text:
	'''文本'''
	def __init__(self, context:str, right:int, top:int,
				color=(255,255,255,255), function=lambda datas:True,
				font=None, size=20, bg_color=(0,0,0,0)):
		'''
		right,top: 文本的右端与顶端坐标
		context:   文本内容
		color:     文本颜色RGBA值
		function:  检测是否显示，必有一个参数datas(传入数据)，返回bool值
				   若不理解lambda表达式，那就按这种形式写就可以了：
				   lambda datas:表达式
				   你能用到的变量只有datas一个
		font:      字体
		size:      大小
		'''
		self.context = context
		self.color = color
		self.func = function
		self.font = pygame.font.SysFont(font,size) # 字体
		self.datpck = datpck
		self.bg_color = bg_color
		# 图像及矩形
		self.image = self.font.render(self.context,True,self.color,self.bg_color)
		self.rect = self.image.get_rect()
		# 设置好位置
		self.rect.right = right
		self.rect.top = top

	def draw(self):
		'''绘制文本'''
		# 假如满足func的要求就绘制
		if self.func(self.datpck):
			self.datpck["screen"].blit(self.image,self.rect)
