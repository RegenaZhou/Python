# Moving Pizza
# Demonstrates sprite velocities
# 移动披萨
# 演示精灵速度

# 1.导入模块
from livewires import games

# 2.初始化游戏窗口
games.init(screen_width = 640, screen_height = 480, fps = 50) 

# 3.设置背景
wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

# 4.创建移动的披萨精灵（核心部分）
pizza_image = games.load_image("pizza.bmp")
the_pizza = games.Sprite(image = pizza_image,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         dx = 1,
                         dy = 1)
games.screen.add(the_pizza)

games.screen.mainloop()

