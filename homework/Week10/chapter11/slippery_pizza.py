# Slippery Pizza Program
# Demonstrates testing for sprite collisions
# 滑溜溜的披萨程序
# 演示精灵碰撞测试

# 1. 导入模块
from livewires import games
import random

# 2.初始化游戏窗口
games.init(screen_width = 640, screen_height = 480, fps = 50)

# 3.Pan 类定义 继承自 games.Sprite 类
class Pan(games.Sprite):
    """" A pan controlled by the mouse. """
    # 每帧更新平底锅位置到鼠标当前位置 调用碰撞检测方法
    def update(self):
        """ Move to mouse position. """
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
 
    def check_collide(self):
        """ Check for collision with pizza. """
        # self.overlapping_sprites：这是一个自动维护的列表，包含所有与当前精灵重叠的精灵
        # 遍历所有重叠的披萨精灵，调用它们的 handle_collide() 方法
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()

# 4.Pizza 类定义
class Pizza(games.Sprite):
    """" A slippery pizza. """
    # 当被平底锅碰撞时调用
    # 将披萨传送到屏幕上的随机位置
    # random.randrange(games.screen.width)：生成0到639之间的随机x坐标
    # random.randrange(games.screen.height)：生成0到479之间的随机y坐标
    def handle_collide(self):
        """ Move to a random screen location. """
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)

# 5.main() 函数
def main():
    # 设置背景
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    # 创建披萨精灵
    pizza_image = games.load_image("pizza.bmp")
    pizza_x = random.randrange(games.screen.width)
    pizza_y = random.randrange(games.screen.height)
    the_pizza = Pizza(image = pizza_image, x = pizza_x, y = pizza_y)
    games.screen.add(the_pizza)

    # 创建平底锅精灵
    pan_image = games.load_image("pan.bmp")
    the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_pan)

    # 鼠标设置
    # 隐藏系统鼠标指针
    games.mouse.is_visible = False
    # 启用事件捕获，防止鼠标移出窗口
    games.screen.event_grab = True

    games.screen.mainloop()

# kick it off!
# 6.程序启动
main()
