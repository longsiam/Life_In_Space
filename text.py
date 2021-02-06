# 文本显示
# version: BETA

from global_vars import *

class Text:
	'''文本'''
	def __init__(self, context:str, right:int, top:int,
				color=(255,255,255,255), function=lambda datas:True,
				font=None, size:int=20, bg_color=(0,0,0,0),
				fade:bool=False, isSysFont=False):
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
		bg_color:  背景颜色
		fade:      是否具有淡入淡出效果
		isSysFont: 是不是系统字体
		'''
		self.context = context
		self.color = color
		self.func = function
		# 字体加载
		if isSysFont:
			self.font = pygame.font.SysFont(font,size)
		else:
			self.font = pygame.font.Font(font,size) 
		self.bg_color = bg_color
		self.fade = fade
		# 图像及矩形
		self.image = self.font.render(self.context,True,self.color,self.bg_color)
		self.img_rect = self.image.get_rect()
		# 为了调透明度，间接从这个surface渲染出去
		self.surface = pygame.Surface((self.image.get_size()))
		self.rect = self.surface.get_rect()
		self.surface.fill(bg_color)
		# 淡入/淡出完成标识与停顿时间
		self.fade_in_finish = False
		self.fade_out_finish = False
		self.sleep_time = datpck["setting"].fade_time/51
		# 设置好位置
		self.rect.right = right
		self.rect.top = top

	def draw(self):
		'''绘制文本'''
		# 假如满足func的要求就绘制
		if self.func(datpck):
			# 渲染透明度遮罩
			if self.fade:
				self.surface.blit(self.image,self.img_rect)
			datpck["screen"].blit(self.surface,self.rect)

	def fade_in_t(self):
		self.fade_in_finish = False
		for i in range(0,255,5):
			self.surface.set_alpha(i)
			sleep(self.sleep_time*2)
		self.fade_in_finish = True

	def fade_in(self):
		fadein = Thread(target=self.fade_in_t)
		fadein.start()

	def fade_out_t(self):
		self.fade_out_finish = False
		for i in range(255,0,-5):
			self.surface.set_alpha(i)
			sleep(self.sleep_time/3)
		self.fade_out_finish = True

	def fade_out(self):
		fadeout = Thread(target=self.fade_out_t)
		fadeout.start()

