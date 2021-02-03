# 可能被其他文件修改的全局变量
# version: BETA

datpck = {}
def change_datpck(key,value):
	'''
	为避免其他文件无法更改datpck的尴尬，所以有了这个函数
	key:   要改什么
	value: 要改成什么
	'''
	global datpck
	datpck[key] = value