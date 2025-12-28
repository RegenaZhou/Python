# Moving Pan
# Demonstrates mouse input
# 移动画面平移
# 演示鼠标输入

# 1.导入模块
from livewires import games

# 2.初始化游戏窗口
games.init(screen_width = 640, screen_height = 480, fps = 50)

# 3.定义 Pan 类（核心部分）
# Pan 类继承自 games.Sprite 继承了精灵的所有基本属性和方法
class Pan(games.Sprite):
    """" A pan controlled by the mouse. """
    # update() 方法重写 这是程序的核心逻辑，处理鼠标跟随：
    # update() 方法在每一帧都会被自动调用
    # 每次调用时，将平底锅的位置设置为当前鼠标位置
    # 实现实时的鼠标跟随效果
    def update(self):
        """ Move to mouse coordinates. """
        self.x = games.mouse.x  # 当前鼠标指针的x坐标
        self.y = games.mouse.y  # 当前鼠标指针的y坐标

# 4.main() 函数
def main():
    # 设置背景
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    # 创建 Pan 实例
    # image = pan_image：设置平底锅图像
    # x = games.mouse.x：初始x坐标设置为当前鼠标x坐标
    # y = games.mouse.y：初始y坐标设置为当前鼠标y坐标
    # 这样确保平底锅一开始就出现在鼠标位置
    pan_image = games.load_image("pan.bmp")
    the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_pan)

    # 隐藏系统鼠标指针 这样玩家只会看到平底锅图像，不会看到双重光标
    games.mouse.is_visible = False
    # 启用事件捕获模式 鼠标会被限制在游戏窗口内 防止鼠标意外移出窗口影响游戏体验
    games.screen.event_grab = True
    # 启动主循环
    games.screen.mainloop()

# kick it off!
main()
