# 特效
# version: BETA

from global_vars import *

class Effect(pygame.sprite.Sprite):
	'''特效的类'''
	def __init__(self, centerx:float, centery:float):
		'''
		centerx: 中心所在的X坐标
		centery: 中心所在的Y坐标 
		'''
		super().__init__()
		# 精确坐标
		self.centerx = centerx
		self.centery = centery
		# 它的图像
		self.images = ()
		self.rect = [i.get_rect() for i in self.images]
		# 形态
		self.form = 0
		# 保持一个形态多久
		self.keep_form_time = 1
		# 是不是要换形态了
		self.chg_form = False
		# 矩形
		self.rect[self.form].centerx = round(self.centerx)
		self.rect[self.form].centery = round(self.centery)
		# 它的音效
		self.sound = Sound("")
		# update所用生成器
		self.updater = self.updater_iter()
		# 是不是播完了
		self.finish = False

	def draw(self):
		'''绘制'''
		datpck["screen"].blit(self.images[self.form], self.rect[self.form])

	def timer(self):
		'''计时器'''
		sleep(self.keep_form_time)
		self.chg_form = True

	def change_form(self):
		'''改变形态'''
		self.chg_form = False  # 把开关重置回去
		# 假如已经换完了
		if self.form == len(self.images):
			self.finish = True
		else:
			self.form += 1
			# 设置新矩形的位置
			self.rect[self.form].centerx = centerx
			self.rect[self.form].centery = centery
			# 重启计时器
			timer = Thread(target=self.timer)
			timer.start()

	def updater_iter(self):
		'''update函数所用生成器的生成函数'''
		# 初始化，播放声音，抛出计时线程
		yield (self.sound.play(),exec("timer=Thread(target=self.timer)",
			timer.start()))
		while True:
			yield (change_form() if self.chg_form else None)

	def update(self):
		'''更新'''
		next(self.updater)

	def move_x(self,px: float):
		'''
		移动X轴位置
		px: 移多少
		'''
		# 移动精确位置
		self.centerx += px
		# 设置实际位置
		self.rect[self.form].centerx = self.centerx

	def move_y(self,px: float):
		'''
		移动Y轴位置
		px: 移多少
		'''
		# 移动精确位置
		self.centery += px
		# 设置实际位置
		self.rect[self.form].centery = self.centery

