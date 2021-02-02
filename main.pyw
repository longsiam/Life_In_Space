# 主程序
# version: BETA

from setting import Setting
from funclib import *
from stats import Stats

def run():
	'''游戏主函数'''
	pygame.init()   # 初始化pygame
	set_=Setting()  # 游戏设置

	# 游戏窗口
	screen=pygame.display.set_mode((set_.screen_width,set_.screen_high)) 
	pygame.display.set_caption("域外人生")  # 标题
	icon=pygame.image.load(os.getcwd()+r"\data\gameicon.ico")
	pygame.display.set_icon(icon)          # 图标

	# 游戏数据包
	datpck={
			"progress":"starting",
			"screen":screen,
			"setting":set_
			}    
	datpck['stats']=Stats(datpck)  # 统计信息

	# 存档，标记已经运行过
	save_file(datpck)
	if isFirstRun():
		with open(os.getcwd()+"\\data\\firstrun","w") as f:
			pass

	# 游戏主循环
	while True:
		handle_event(datpck)

if __name__ == "__main__":
	run()
