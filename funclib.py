# 函数库
# version: BETA
import os.path
import sys
from tools import *
from global_vars import *
from interface import *

def quit_game():
	'''安全退出游戏'''
	# 保存进度
	change_datpck("progress",datpck["interface"].id+":"+str(datpck["interface"].subid))
	save_file()                     # 存档
	datpck["interface"].quit()      # 停止音乐
	# 回收残余线程, 安全退出
	sys.exit(system("TASKKILL /f /im cmd.exe"))

def save_file():
	'''将数据存档'''
	# getcwd()能获取当前路径
	# .dat文件其实就是普通的文本文件换了个后缀, player.dat是游戏存档文件
	with open(getcwd()+r"\data\player.dat", "w", encoding="utf-8") as f:
		# 将统计信息与进度描述放入一个字典，加密写入存档中
		f.write(encry(str(
			{
				"stats":datpck["stats"].get_longterm(), 
				"progress":datpck["progress"], 
				"setting":datpck["setting"].get_dynamic()
			}
		)))

def read_file() -> tuple:
	'''
	读取存档
	返回值：存档存的字典
	'''
	with open(getcwd()+r"\data\player.dat", "r", encoding="utf-8") as f:
		# 解密后读得的仍是字符串，要eval一下才是真正的字典
		return eval(decry(f.read()))

def handle_event():
	'''监听+处理事件'''
	for event in pygame.event.get():
		# 监听是否按下×，按下就退出
		if event.type == pygame.QUIT:
			quit_game()
		# 按键事件，移交界面处理
		elif event.type == pygame.KEYDOWN:
			datpck["interface"].handle_key_down(event.key)
		elif event.type == pygame.KEYUP:
			datpck["interface"].handle_key_down(event.key)
		# 鼠标事件，移交界面处理
		elif event.type == pygame.MOUSEBUTTONDOWN:
			datpck["interface"].handle_mouse_button_down()
		elif event.type == pygame.MOUSEBUTTONUP:
			datpck["interface"].handle_mouse_button_up()
		elif event.type == pygame.MOUSEMOTION:
			datpck["interface"].handle_mouse_motion()

def isFirstRun() -> bool:
	'''
	检查是否为第一次运行
	返回值：是否第一次运行，是为True
	'''
	return not os.path.exists(getcwd()+r'\data\player.dat')

def goto_interface_by_progress():
	'''根据进度信息跳转界面, 父ID=界面类名'''
	# 进度信息按冒号分隔，最后一部分是子ID，其余是父ID
	# 父ID不知道有没有被分成几部分，所以要拼成字符串
	super_id = "".join(datpck["progress"].split(":")[:-1])
	sub_id = int(datpck["progress"].split(":")[-1])
	change_datpck("interface",eval(f"{super_id}({sub_id})"))
	change_datpck("progress",eval(f"{super_id}({sub_id})"))

