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
	# 窗口标题
	pygame.display.set_caption("域外人生")  
	# 窗口图标
	icon=pygame.image.load(os.getcwd()+r"\data\gameicon.ico")
	pygame.display.set_icon(icon)         

	# 进度信息
	if not isFirstRun():
		prg=read_file()["progress"]
	else:
		prg="starting"
	# 游戏数据包
	datpck={
			"progress":prg,
			"screen":screen,
			"setting":set_
			}    
	datpck["stats"]=Stats(datpck)  # 统计信息

	# 存档，标记已经运行过
	save_file(datpck)
	if isFirstRun():
		show_start_cg(datpck)  # 起始剧情CG
		with open(os.getcwd()+r"\data\firstrun","w") as f:
			pass

	# 游戏主循环
	while True:
		handle_event(datpck)
		pygame.display.update()

# 检查是否是被当成模块导入，如果是就别运行
if __name__ == "__main__":
	run()
