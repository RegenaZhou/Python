# Bouncing Pizza
# Demonstrates dealing with screen boundaries
# 弹跳披萨
# 演示如何处理屏幕边界

# 1.导入模块
from livewires import games

# 2.初始化游戏窗口
games.init(screen_width = 640, screen_height = 480, fps = 50) 

# 3.定义 Pizza 类（核心部分）
# Pizza 类继承自 games.Sprite 继承了精灵的所有基本功能（位置、速度、图像显示等）
class Pizza(games.Sprite):
    """ A bouncing pizza. """
    # update()方法重写，这是程序的核心逻辑，处理边界碰撞检测：
    def update(self):
        """ Reverse a velocity component if edge of screen reached. """
        # 如果到达屏幕边缘，则反转速度分量。
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx # 水平速度 dx 取反
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy # 垂直速度 dy 取反

# 4.main() 函数
def main():
    # 设置背景
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    # 创建 Pizza 实例
    # image = pizza_image：设置披萨图像
    # x = games.screen.width / 2：初始x坐标在屏幕中央（320）
    # y = games.screen.height / 2：初始y坐标在屏幕中央（240）
    # dx = 1：水平速度，每帧向右移动1像素
    # dy = 1：垂直速度，每帧向下移动1像素
    pizza_image = games.load_image("pizza.bmp")
    the_pizza = Pizza(image = pizza_image,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)
    # 添加到屏幕并启动
    games.screen.add(the_pizza)

    games.screen.mainloop()

# kick it off!
# 5.程序启动
main()
