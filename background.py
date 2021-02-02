# 背景(包括CG, 星空等，背景星星的类也包含在里面)
# version: BETA

import pygame
from pygame.sprite import Sprite, Group
from os import getcwd
from text import Text
from random import randint, choice


class BackGround:
	'''游戏背景'''
	def __init__(self, datpck: dict, image=(0,0,0), **text):
		'''
		image: 元组或字符串，如果是元组就是背景颜色RGB，否则是背景图片文件名
		text: 共context,type,color,function四个关键字，用于构造文本对象，可选
		'''
		self.screen = datpck["screen"]
		if text:
			self.text=Text(text["context"],text["type"],text["color"],text["function"])
		# 如果是元组，那么就是背景颜色模式
		if type(image) == tuple:
			self.bg=image
			# 表明是什么模式
			self.image_type = "color"
		# 不然就是图片模式
		else:
			self.bg = pygame.image.load(getcwd()+"\\data\\"+image)
			# 图片的矩形对象与它的(x,y)坐标
			self.bg_rect = self.bg.get_rect()
			self.bg_rect.x = 0
			self.bg_rect.y = 0
			# x,y坐标的精确值
			self.x = 0.0
			self.y = 0.0
			self.image_type = "image"

	def draw(self):
		'''绘制背景图像'''
		if self.image_type == "color":
			# color模式填颜色
			self.screen.fill(self.bg)
		else:
			# 否则绘制图片
			self.screen.blit(self.bg, self.bg_rect)
		# 绘制文本
		self.text.draw()

	def up(self, px):
		'''
		将背景图像向上移
		px: 向上移几个像素
		'''
		self.y -= px
		self.bg_rect.y = self.y

	def down(self, px):
		'''向下移'''
		self.up(-px)  # 向下n像素相当于向上-n像素

	def left(self, px):
		'''向左移'''
		self.x -= px
		self.bg_rect.x = self.x

	def right(self, px):
		'''向右移'''
		self.left(-px) # 同理



class SmallStar(Sprite):
	'''星空背景上的随机小星星'''
	def __init__(self, datpck: dict, x=None, y=None):
		'''
		x：星星的X轴位置，若未指定将随机指定位置
		y: 星星的Y轴位置，x与y必须同时指定或同时不指定
		'''
		super().__init__()
		self.screen = datpck["screen"]
		# 绘制一个n*n的矩形代表星星
		self.rect = pygame.Rect(0, 0,
			datpck["setting"].star_size, datpck["setting"].star_size)
		# 确定其亮度
		light = randint(datpck["setting"].star_drakest,
			datpck["setting"].star_lightest)
		# 选择其颜色
		self.color = choice((
			( light, light, light ),  # 白色
			( light, light, light ),  # 为让白色星星更多，突出彩色星星
			( light, light, light ),  # 所以多设两个白色，增加权重
			( light,   0,     0   ),  # 红色
			(   0,     0,   light ),  # 蓝色
			( light, light,   0   )   # 黄色
		))
		# 如果没有指定x和y，将直接随机决定位置
		# 注意此处x如果是None，y必然也是None
		if x is None:
			ramdom_location()
		else:
			# 如果指定x,y，就直接写入
			self.rect.centerx=x
			self.rect.centery=y

	def draw(self):
		'''绘制星星'''
		pygame.draw.rect(self.screen, self.color, self.rect)

	def ramdom_location(self):
		'''随机决定星星位置'''
		# 确定其在X轴上的位置，距离窗口边框要有一定距离
		self.rect.centerx = random.randint(self.datpck["setting"].star_edge,
			self.datpck["setting"].screen_width-self.datpck["setting"].star_edge)
		# 确定其在Y轴上的位置
		self.rect.centery = random.randint(self.datpck["setting"].star_edge,
			self.datpck["setting"].screen_high-self.datpck["setting"].star_edge)



class StarrySky(BackGround):
	'''星空背景'''
	def __init__(self, datpck: dict, image=(0,0,0), **text):
		super().__init__()
		# 星星的编组（可以将其看做集合，遍历要用.sprites()）
		self.stars=Group()
		self.datpck=datpck
		# 生成星星
		for _ in range(0, self.datpck["setting"].star_quantity):
			self.stars.add(SmallStar(self.datpck))
		# X,Y轴的“容量”
		# 容量：因为星星是固定的，所以星空背景移动时会有一片区域空缺出来没星星
		# 为生成星星，记录在X轴与Y轴上的移动距离总和
		# 当达到一定水平时(即“满”了)，在移动出来的空缺区生成一颗星星
		self.volume_x=0
		self.volume_y=0

	def draw(self):
		'''绘制星空'''
		super().draw()
		# 绘制星星
		for star in self.stars.sprites():
			star.draw()

	def up(self, px):
		'''向上移'''
		super().up()
		# 将星星移动，假如越界了就删除
		for star in self.stars.sprites():
			star.centery -= px
			if star.centery < 0:
				self.stars.remove(star)
		# 检查容量是否满了，为防止容量超过star_density两倍，所以用while
		while volume_y > self.datpck["setting"].star_density:
			# 指定新星星的坐标
			y = self.datpck["setting"].star_edge
			x = randint(self.datpck["setting"].star_edge, 
				self.datpck["setting"].screen_high-self.datpck["setting"].star_edge)
			self.stars.add(SmallStar(self.datpck,x,y))
			# 使容量恢复
			volume_y -= star_density

	def down(self, px):
		'''向下移'''
		super().down()
		for star in self.stars.sprites():
			star.centery += px
			if star.centery > self.datpck["setting"].screen_high:
				self.stars.remove(star)
		while volume_y < -self.datpck["setting"].star_density:
			y = self.datpck["setting"].screen_high-self.datpck["setting"].star_edge
			x = randint(self.datpck["setting"].star_edge, 
				self.datpck["setting"].screen_high-self.datpck["setting"].star_edge)
			self.stars.add(SmallStar(self.datpck,x,y))
			volume_y += self.datpck["setting"].star_density

	def left(self, px):
		'''向左移'''
		super().left()
		for star in self.stars.sprites():
			star.centerx -= px
			if star.centerx < 0:
				self.stars.remove(star)
		while volume_x < self.datpck["setting"].star_density:
			x = self.datpck["setting"].star_edge
			y = randint(self.datpck["setting"].star_edge, 
				self.datpck["setting"].screen_width-self.datpck["setting"].star_edge)
			self.stars.add(SmallStar(self.datpck,x,y))
			volume_x -= self.datpck["setting"].star_density


	def right(self, px):
		'''向右移'''
		super().right()
		for star in self.stars.sprites():
			star.centerx += px
			if star.centerx > self.datpck["setting"].screen_width:
				self.stars.remove(star)
		while volume_x < -self.datpck["setting"].star_density:
			x = self.datpck["setting"].screen.width-self.datpck["setting"].star_edge
			y = randint(self.datpck["setting"].star_edge, 
				self.datpck["setting"].screen_width-self.datpck["setting"].star_edge)
			self.stars.add(SmallStar(self.datpck,x,y))
			volume_x += self.datpck["setting"].star_density
