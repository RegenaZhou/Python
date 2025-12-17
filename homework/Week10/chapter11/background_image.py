# Background Image
# Demonstrates setting the background image of a graphics screen
# 背景图片
# 演示如何设置图形界面的背景图片

# 1.导入模块
# 从 livewires 库导入 games 模块
# livewires 是一个用于教学的游戏编程库，提供了简单的图形和游戏开发功能
from livewires import games

# 2.初始化游戏窗口
# screen_width = 640：设置窗口宽度为640像素
# screen_height = 480：设置窗口高度为480像素
# fps = 50：设置帧率为50帧/秒（Frame Per Second）
games.init(screen_width = 640, screen_height = 480, fps = 50)

# 3.加载背景图像
# 第一个参数 "wall.jpg"：图像文件名
# 第二个参数 transparent = False：设置图像不透明
wall_image = games.load_image("wall.jpg", transparent = False)

# 4. 设置背景
# 将加载的图像设置为屏幕背景
games.screen.background = wall_image

# 5.启动主循环
games.screen.mainloop()
