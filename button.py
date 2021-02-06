# 按钮
# version: BETA

from global_vars import *
from text import Text

class Button:
	'''按钮'''
	def __init__(self, image, context:Text, centerx:int, centery:int,
				width, height, click_func):
		'''
		image      : 颜色/图像，颜色填RGBA元组，图像填文件名
		context    : 按钮上显示的文本
		centerx    : 中心在X轴的坐标，centery同理     
		width      : 按钮的宽
		height     : 按钮的高
		click_func : 点到了会怎么样
		'''
		self.context = context
		self.centerx = centerx
		self.centery = centery
		self.width = width
		self.height = height
		self.image = imgae
		self.type = "color" if type(image)==tuple else "image"
		self.rect = pygame.Rect(0,0,self.width,self.hetght)
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery

	def draw(self):
		'''绘制'''
		if self.type == "color":
			datpck["screen"].fill(self.image,self.rect)
		else:
			datpck["screen"].blit(self.image,self.rect)
		self.text.draw()

	def check_click(self, x, y):
		'''
		检查有没有被点到
		x,y: 点到哪的坐标
		'''
		if (self.rect.centerx-self.width/2 <= x <= self.rect.centerx+self.width/2 and
			self.rect.centery-(self.height/2) <= y <= self.rect.centery-(self.height/2)):
			self.click_func()


