# 界面 Interface
# version: BETA

import pygame
from text import Text
from background import *
from audio import *
from time import sleep
from threading import Thread
from global_vars import *

class Interface:
	'''
	为便于描述和定位，像播放CG，漫游星际这种界面
	就放在一个Interface子类中，像显示什么的方便很多
	自己重写超类的方法，就可以定义出很多不同的界面了
	'''
	def __init__(self, subid:int=0):
		'''
		里面的变量直接子类内部重定义
		其实这里只是做个样子，当是声明一下做个约定
		subid: 进度标识符子索引
		'''
		# 实体编组列表，考虑到不止一种实体，所以一种实体一个编组
		# entities则是这些编组的列表
		self.entities = []
		# 界面背景
		self.bg = BackGround()
		# 界面文本元组（考虑到可能有多种文本）
		self.text = ()
		# 画面是否被冻结（暂停）
		self.isFrozen = False
		# 界面进度标识符（进度定位时要用）
		self.id = ""
		self.subid = subid
		# 音响资源元组
		self.bgm = ()
		self.sound = ()
		# 播放中的bgm在资源元组中的位置
		self.playing_bgm_ind = 0
		# 如果子索引不为0，那么上次退出前肯定在某个子界面
		# 所以我们要跳转过去
		if subid:
			self.goto_subinterface(subid)

	def __str__(self):
		'''当对象被用作字符串时返回什么（报错时要用）'''
		return self.id

	def draw(self):
		'''绘制,图层千万别搞混'''
		# 绘制背景(背景图层在最下方)
		self.bg.draw()
		# 之后是逐个绘制实体
		for entity_group in self.entities:
			for entity in entity_group.sprites():
				entity.draw()
		# 最后是绘制文本
		for t in self.text:
			t.draw()

	def update(self):
		'''更新实体'''
		for entity_group in self.entities:
			entity_group.update()

	def goto_subinterface(self, subid: int):
		'''跳转至某个子索引(subid)'''
		pass

	def handle_key_down(self, key):
		'''处理按键(key)被按下'''
		pass

	def handle_key_up(self, key):
		'''处理按键被松开'''
		pass

	def handle_mouse_button_down(self):
		'''处理鼠标按键按下'''
		pass

	def handle_mouse_button_up(self):
		'''处理鼠标按键松开'''
		pass

	def handle_mouse_motion(self):
		'''处理鼠标移动'''
		pass

	def frozen(self, time=0):
		'''暂停冻住画面,time=0时必须主动解冻'''
		isFrozen = True
		if time:
			def thaw_time():
				'''为不干扰主线程其他组件的运行，单独开一个线程计时'''
				sleep(time)
				isFrozen = False
			timer = Thread(target=thaw_time)
			timer.start()


	def thaw(self):
		'''解冻画面'''
		isFrozen = False

	def play_bgm(self, ind:int=0):
		'''
		播放BGM(只能同时播放一个)
		ind: 在资源元组的索引
		'''
		self.bgm[ind].play()
		self.playing_bgm_ind=ind

	def stop_bgm(self):
		'''暂停BGM'''
		# 为防止没有bgm又恰好quit_game的时候崩溃
		if self.bgm:
			self.bgm[self.playing_bgm_ind].stop()

	def play_sound(self, ind: int):
		'''播放音效'''
		self.sound[ind].play()



class StartCG(Interface):
	'''起始剧情的CG'''
	pass