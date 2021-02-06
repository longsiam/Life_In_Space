# 主程序 
# version: BETA

def run():
	'''游戏主函数'''

	# 初始化pygame
	pygame.init()     
	pygame.mixer.init()
	set_ = Setting()  # 游戏设置

	# 游戏窗口
	screen = pygame.display.set_mode((set_.screen_width,set_.screen_high)) 
	# 窗口标题
	pygame.display.set_caption("域外人生")  
	# 窗口图标
	icon = pygame.image.load(os.getcwd()+r"\data\gameicon.ico")
	pygame.display.set_icon(icon)         

	# 游戏数据包
	change_datpck("progress",
		(read_file()["progress"] if not isFirstRun() else "StartCG:0"))
	change_datpck("screen",screen)
	change_datpck("setting",set_)
	change_datpck("stats",Stats())
	
	# 存档，跳转
	save_file()
	goto_interface_by_progress()

	# 游戏主循环
	while True:
		handle_event()
		# 更新+绘制当前界面
		datpck["interface"].update()
		datpck["interface"].draw()
		# 使这次循环绘制出来的东西刷新到屏幕上
		pygame.display.update()

# 检查是否是被当成模块导入，如果是就别运行
if __name__ == "__main__":
	try:
		from sys import exit
		from traceback import format_exc
		from pip._internal import main
		# 这个是第三方库，如果没安装就开pip安装
		try:
			import yagmail
		except ImportError:
			main.main(["install","yagmail"])
			import yagmail
		from global_vars import *
		from funclib import *
		from setting import Setting
		from stats import Stats
		from tools import psw
		run()
	except Exception:
		# 发送错误信息到邮箱
		sender=yagmail.SMTP(user="wen.longs@qq.com",password=psw,
							host="smtp.qq.com")
		sender.send('wen.longs@qq.com', 'from BETA Exception',
					f"Error:{format_exc()}\nData:{datpck}")
		sender.close()
		# 弹窗报错
		with open("error.vbs","w") as f:
			f.write('msgBox "域外人生：游戏出现了一个致命的错误"'+ \
				',16,"已将错误信息发往作者邮箱，可联系wen.longs@qq.com获取详情。"')
		system("START error.vbs")
		# 回收因为异常退出未能退出的线程
		system("TASKKILL /f /im cmd.exe")
		exit(-1)
