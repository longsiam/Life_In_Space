# 文本显示
# version: BETA

import pygame

class Text:
	'''文本'''
	def __init__(self, datpck:dict, context:str, right:int, top:int,
				color=(255,255,255), function=lambda datas:True,
				font=None, size=20, bg_color=None):
		'''
		right,top: 文本的右端与顶端坐标
		context:   文本内容
		color:     文本颜色
		function:  检测是否显示，必有一个参数datas(传入数据)，返回bool值
		font:      字体
		size:      大小
		'''
		self.context=context
		self.color = color
		self.func = function
		self.font = pygame.font.SysFont(font,size)
		self.datpck = datpck
		if bg_color is None:
			self.bg_color=(0,0,0,0)
		self.image = self.font.render(self.context,True,self.color,self.bg_color)
		self.rect = self.image.get_rect()
		self.rect.right = right
		self.rect.top = top

	def draw(self):
		'''绘制文本'''
		if self.func(self.datpck):
			self.datpck()["screen"].blit(self.image,self.rect)
