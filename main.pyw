# 主程序
# version: BETA

import pygame
import os
from setting import Setting
from funclib import *

def run():
	'''游戏主函数'''
	pygame.init()   # 初始化pygame
	set_=Setting()  # 游戏设置
	# 游戏窗口
	screen=pygame.display.set_mode((set_.screen_width,set_.screen_high)) 
	pygame.display.set_caption("域外人生") # 标题
	icon=pygame.image.load(os.getcwd()+r"\data\gameicon.ico")
	pygame.display.set_icon(icon) # 图标
	datpck={"screen":screen, "set":set_}
	# 游戏主循环
	while True:
		handle_event(datpck)

if __name__ == "__main__":
	run()
