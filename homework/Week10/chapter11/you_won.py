# You Won
# Demonstrates displaying a message
# 你赢了
# 演示显示一条消息

# 1.导入模块
from livewires import games, color

# 2.初始化游戏窗口
games.init(screen_width = 640, screen_height = 480, fps = 50)

# 3.设置背景
wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

# 4.创建消息对象（核心部分）
# games.Message 是 games.Text 的子类，专门用于显示临时消息，具有自动销毁功能。
won_message = games.Message(value = "You won!",
                            size = 100,
                            color = color.red,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            lifetime = 2500, #消息的存活时间，以帧为单位 2500帧在50FPS下相当于50秒（2500 ÷ 50 = 50） 时间到达后消息会自动销毁
                            after_death = games.screen.quit) #回调函数机制：指定消息销毁后要执行的函数 games.screen.quit 是退出游戏窗口的函数 这意味着消息显示50秒后程序会自动关闭

# 5.添加消息到屏幕
games.screen.add(won_message)

# 6.启动主循环
games.screen.mainloop()
