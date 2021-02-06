# 音响（包括音乐、音效）
# version: BETA

from os import getcwd
from global_vars import *

class Music:
	'''音乐'''
	def __init__(self, file_name: str, volume=1, fade_out=0,):
		'''
		file_name: 音乐文件名
		volume:    音量大小
		fade_out:  淡出秒数
		'''
		# 将音量乘以设置的音量就是真正的音量大小了
		self.volume = volume*datpck["setting"].volume
		# 音乐文件路径
		self.path = getcwd()+"\\data\\"+file_name
		self.fade_out = fade_out
		# 如果要停下来就更改这个标志就行了
		self.music_stop_flag = False

	def player(self):
		'''播放音乐的线程函数'''
		# 设置音量、加载并播放
		pygame.mixer.music.set_volume(self.volume)
		pygame.mixer.music.load(self.path)
		pygame.mixer.music.play(-1)
		# 侦测是否要停止播放
		while True:
			# 如果真要停下来
			if self.music_stop_flag:
				# 假如没设置淡出，直接停下来
				if self.fade_out == 0:
					pygame.mixer.music.stop()
				# 不然还要fadeout
				else:
					pygame.mixer.music.fadeout(self.fade_out)
				# 设置回去，便于下一次的播放
				self.music_stop_flag = False
				return

	def play(self):
		'''播放音乐'''
		player=Thread(target=self.player)
		player.start()

	def stop(self):
		'''停止音乐'''
		self.music_stop_flag = True



class Sound:
	'''音效'''
	def __init__(self, file_name: str, volume=1):
		self.path = getcwd()+"\\data\\"+file_name
		self.volume = volume*datpck["setting"].volume
		self.sound = pygame.mixer.Sound(getcwd()+'\\datas\\music\\'+path)

	def play(self):
		'''播放'''
		self.sound.play()

