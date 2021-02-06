# 界面 Interface
# version: BETA

from text import Text
from background import *
from audio import *
from global_vars import *
from funclib import *
from text import Text
from button import Button


class Interface:
	'''
	为便于描述和定位，像播放CG，漫游星际这种界面
	就放在一个Interface子类中，像显示什么的方便很多
	自己重写超类的方法，就可以定义出很多不同的界面了
	'''
	def __init__(self, subid: int=0):
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
		# 界面文本列表（考虑到可能有多种文本）
		self.text = []
		# 画面是否被冻结（暂停）
		self.isFrozen = False
		# 界面进度索引（进度定位时要用）
		self.id = ""
		self.subid = subid
		# 音响资源	
		self.bgm = None
		self.sound = []
		# 如果子索引不为0，那么上次退出前肯定在某个子界面
		# 所以我们要跳转过去
		if subid:
			self.goto_subinterface(subid)

	def __repr__(self):
		'''当对象被用作字符串时返回什么（报错时要用）'''
		return repr(self.id)

	def draw(self):
		'''绘制,图层千万别搞混'''
		# 绘制背景(背景图层在最下方)
		self.bg.draw()
		# 之后是逐个绘制实体
		for entity_group in self.entities:
			for entity in entity_group.sprites():
				entity.draw()
		# 最后是绘制文本
		for txt in self.text:
			txt.draw()

	def update(self):
		'''更新实体'''
		for entity_group in self.entities:
			entity_group.update()

	def goto_subinterface(self, subid: int):
		'''跳转至某个子索引(subid)'''
		pass

	def handle_key_down(self, key):
		'''处理按键(key)被按下'''
		if key == pygame.K_ESCAPE:
			quit_game()

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
		self.bgm.play()

	def stop_bgm(self):
		'''暂停BGM'''
		# 为防止没有bgm又恰好quit_game的时候崩溃
		if self.bgm:
			self.bgm.stop()

	def play_sound(self, ind: int):
		'''播放音效'''
		self.sound[ind].play()

	def quit(self):
		'''安全退出'''
		self.stop_bgm()



class StartCG(Interface):
	'''起始剧情的CG'''
	def __init__(self, subid:int=0):
		super().__init__(subid)
		self.id = "StartCG"
		self.bgm = Music("scg.mp3",0.7)
		# 把第0张CG预加载了，便于操作
		self.bg = CG(f"scg_{subid}.png")
		# 起始剧情文本元组元组，一个画面配一个元组，元组每一个元素一行
		self.plot = (
						(
							Text("3020年  地球",700,500,
								font=getcwd()+r'\data\font.ttf',size=65,fade=True),
						),
						(
							Text("你买彩票中了300亿零一毛",800,500,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
							Text("一夜暴富……",700,570,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True)
						),
						(
							Text("那时候的一毛钱就可以买一套别墅",930,500,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
						),
						(
							Text("当你疯狂地报复性消费",730,460,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
							Text("沉浸在有钱人的喜悦中时...",830,530,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
						),
						(
							Text("一个神秘黑恶组织Acirema派人将你敲晕...",1000,480,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
						),
						(
							Text("醒来时，你发现自己在一架战斗飞碟里",950,480,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
						),
						(
							Text("满怀震惊和疑惑的你来到驾驶台，",870,480,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
							Text("发现去往地球的按钮需要密码才能启动",950,550,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
						),
						(
							Text("你只在驾驶室找到一封信：“看到这张纸条你应该已经" + \
								"在3000光年外的ξ星了吧，你速速把那些ξ星人杀光，",1050,480,
								font=getcwd()+r'\data\font.ttf',size=19,fade=True),
							Text("抢走他们的资源，驾驶台旁的虫洞会自动检测你的资源，" + \
								"你把资源投进去，只要你完成了这项任务，你就能",1050,505,
								font=getcwd()+r'\data\font.ttf',size=19,fade=True),
							Text("坐上Acirema第二把交椅。放心，我们也会把钱还给你，虫" + \
								"洞检测到足够的资源就才显示密码，如果拿不到",1030,530,
								font=getcwd()+r'\data\font.ttf',size=19,fade=True),
							Text("就别想回来了。",180,555,
								font=getcwd()+r'\data\font.ttf',size=19,fade=True),
							Text("-- Acirema首领 Pmurt",1050,555,
								font=getcwd()+r'\data\font.ttf',size=19,fade=True),
						),
						(
							Text("信旁正是那个虫洞，你十分好奇这么小怎么传资源...",1050,480,
								font=getcwd()+r'\data\font.ttf',size=40,fade=True),
						),
						(
							Text("你透过窗户望去，这应该就是他们口中的ξ星",1030,480,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
							Text("你暗暗惊奇：原来真的有外星人啊...",850,550,
								font=getcwd()+r'\data\font.ttf',size=45,fade=True),
						)
					)
		self.text = self.plot[self.subid]
		# 只是一个临时标识变量……
		self.flag = 0
		# 检查是否要换图片了
		self.change_image = False

	def goto_subinterface(self, subid: int):
		# 因为播放的时候起始图片索引按self.subid算，所以直接改就行了
		self.subid = subid

	def timer_t(self):
		'''换图的计时器线程函数'''
		# 停顿指定时间
		sleep(datpck["setting"].scg_chgimg_time[self.subid])
		self.change_image = True

	def update(self):
		'''
		为了不耽误主循环的运作与绘制
		所以一次调用只能有一次不占太多时间的操作
		按flag来保存进度（如果有兴趣可以用yield，但是有点难实现）
		'''
		# flag=0时，开始淡入, 播放音乐
		if not self.flag:
			self.play_bgm()
			self.bg.fade_in()
			for txt in self.text:
				txt.fade_in()
			# 下一次操作就到flag=1那里了
			self.flag = 1   
		# 当加载完了，拉出计时器换图
		elif (self.flag == 1 and self.bg.fade_in_finish and 
				all([i.fade_in_finish for i in self.text])):
			# 要记得重置
			for txt in self.text:
				txt.fade_in_finish = False
			self.bg.fade_in_finish = False
			self.flag = 2
			timer = Thread(target=self.timer_t)
			timer.start()
		# 全部播完了，淡出最后一张
		elif self.flag == 4:
			self.bg.fade_out()
			for txt in self.text:
				txt.fade_out()
			self.flag = 5
		# 淡出完了，停止音乐，移交控制权
		elif (self.flag == 5 and self.bg.fade_out_finish and 
				all([i.fade_out_finish for i in self.text])):
			self.stop_bgm()
			change_datpck("interface", MainMenu()) 
			change_datpck("progress", "MainMenu:0")
		# 其他的时候就坐等换图
		else:
			# 如果叫换图了
			if self.change_image:
				# flag=2的时候就淡出
				if self.flag == 2:
					# 如果已经加载完了，跳到flag=4
					if self.subid == 9:
						self.flag = 4
					# 不然就把指针后移一位，开始淡出
					else:
						self.subid += 1
						self.bg.fade_out()
						for txt in self.text:
							txt.fade_out()
						self.flag = 3
				# 淡出完了，换图，淡入
				if (self.flag == 3 and self.bg.fade_out_finish and 
						all([i.fade_out_finish for i in self.text])):
					self.bg.fade_out_finish = False
					for txt in self.text:
						txt.fade_out_finish = False
					self.bg = CG(f"scg_{self.subid}.png")
					self.text = self.plot[self.subid]
					self.bg.fade_in()
					for txt in self.text:
						txt.fade_in()
				# 淡入完了，开始计下一个的时，重置回flag2
				if (self.flag == 3 and self.bg.fade_in_finish and 
						all([i.fade_in_finish for i in self.text])):
					self.bg.fade_in_finish = False
					for txt in self.text:
						txt.fade_in_finish = False
					self.change_image = False
					new_timer = Thread(target=self.timer_t)
					new_timer.start()
					self.flag = 2
				



class MainMenu(Interface):
	'''主菜单'''
	def __init__(self,subid:int=0):
		super().__init__(subid)
		self.id = "MainMenu"
		self.bg = StarrySky()
		


class TestRoom(Interface):
	def __init__(self,subid:int=0):
		super().__init__(subid)
		self.id = "TestRoom"
