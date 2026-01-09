# Pizza Sprite
# Demonstrates creating a sprite
# 比萨精灵
# 演示创建一个精灵

# 1.导入模块
from livewires import games

# 2.初始化游戏窗口
games.init(screen_width = 640, screen_height = 480, fps = 50)

# 3.设置背景
wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

# 4.创建披萨精灵（核心部分）
pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image = pizza_image, x = 320, y = 240)

# 5.添加精灵到屏幕
games.screen.add(pizza)

# 6.启动主循环
games.screen.mainloop()
