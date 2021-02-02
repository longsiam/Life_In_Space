# 更新日志

### 2021/1/31 21:05 BETA_00 (Longs)
1. 创建main.pyw
	- 创建main 函数（现在还是一个空壳）
	- 创建sets对象
2. 创建wiki
	- home
	- operation
3. 创建funclib.py
	- 创建quit_game函数
4. 创建setting.py
	- 创建setting类

### 2021/2/1 18:00 BETA_00 (Longs)
1. 更新funclib.py
	- 更新quit_game函数（存档机制）
	- 加入加/解密功能(encry与decry函数)
	- 加入读/存档机制(save_file与read_file函数)
2. 更新setting.py
	- 加入窗口长宽设置
	- 声明了init_dynamic方法（目前没有内容）

### 2021/2/1 20:00 BETA_01 (Longs)
1. 更新main.py
	- 构建窗口及datpck
	- 建立游戏主循环（目前只会监听+处理事件）
2. 更新funclib.py
	- 加入handle_event函数（目前只会监听关闭事件）
3. 加入图标data\gameicon.ico

### 2021/2/2 14:00 BETA_02 (Longs)
1. 更新funclib.py
	- 加入isFirstRun函数
2. 更新setting.py
	- 加入get_dynamic方法, init_dynamic方法现在也有内容了
	- 加入起始财产与血量最大值的设置
3. 加入stats.py
	- 加入活动状态、处决点数、血量
	- 加入get_longterm方法
