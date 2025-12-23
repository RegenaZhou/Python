# Big Score
# Demonstrates displaying text on a graphics screen
# 高分
# 演示如何在图形屏幕上显示文本

# 1.导入模块
from livewires import games, color

# 2.初始化游戏窗口
games.init(screen_width = 640, screen_height = 480, fps = 50)

# 3.设置背景
wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

# 4.创建文本对象（核心功能）
# value = 1756521：要显示的文本内容 可以是字符串或数字（会自动转换为字符串） 这里显示一个高分数值
# size = 60：字体大小，设置为60磅（较大尺寸）创建醒目的"大分数"效果
# color = color.black：文本颜色，使用 color 模块中的黑色常量
# x = 550, y = 30：文本在屏幕上的位置坐标 x = 550：靠近屏幕右边缘（屏幕宽度640） y = 30：靠近屏幕顶部 这种位置安排模拟了游戏中常见的分数显示位置
score = games.Text(value = 1756521,
                   size = 60,
                   color = color.black,
                   x = 550,
                   y = 30)

# 5.添加文本到屏幕
games.screen.add(score)

# 6.启动主循环
games.screen.mainloop()
