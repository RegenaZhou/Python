# Pizza Panic
# Player must catch falling pizzas before they hit the ground
# 披萨危机
# 玩家必须在披萨落地前接住它们

# 1.导入模块
from livewires import games, color
import random

# 2.初始化游戏窗口
# 创建640×480像素的窗口 设置帧率为50FPS
games.init(screen_width = 640, screen_height = 480, fps = 50)

# 3.Pan 类（玩家控制的平底锅）
class Pan(games.Sprite):
    """
    A pan controlled by player to catch falling pizzas.
    由玩家控制的平底锅，用来接住掉下来的比萨饼。
    """
    # 类属性，所有实例共享同一个图像
    image = games.load_image("pan.bmp")

    # 构造函数
    def __init__(self):
        """
        Initialize Pan object and create Text object for score.
        初始化面板对象并创建用于分数的文本对象。
        """
        # 调用父类构造函数
        # x = games.mouse.x：初始x坐标在鼠标位置
        # bottom = games.screen.height：底部对齐屏幕底部
        super(Pan, self).__init__(image = Pan.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)

        # 创建分数显示
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    # update() 方法
    def update(self):
        """ Move to mouse x position. 移动到鼠标的 X 坐标"""
        # 水平跟随鼠标移动
        self.x = games.mouse.x

        # 边界检测，防止移出屏幕
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width

        # 调用碰撞检测
        self.check_catch()

    # check_catch() 方法
    def check_catch(self):
        """ Check if catch pizzas. 检查是否抓到披萨。"""
        # 检测与披萨的碰撞
        for pizza in self.overlapping_sprites:
            # 每接住一个披萨加10分
            self.score.value += 10
            # 更新分数显示位置
            self.score.right = games.screen.width - 10
            # 调用披萨的被接住处理方法
            pizza.handle_caught()

# 4.Pizza 类（下落的披萨）
class Pizza(games.Sprite):
    """
    A pizza which falls to the ground.
    一块掉到地上的披萨。
    """
    # 类属性 共享的披萨图像 下落速度（类属性，所有披萨相同）
    image = games.load_image("pizza.bmp")
    speed = 1   

    # 构造函数
    # x 参数指定生成位置（与厨师位置对齐）
    # y = 90 默认在屏幕顶部附近
    # dy = Pizza.speed 设置垂直下落速度
    def __init__(self, x, y = 90):
        """ Initialize a Pizza object. 初始化一个披萨对象。"""
        super(Pizza, self).__init__(image = Pizza.image,
                                    x = x, y = y,
                                    dy = Pizza.speed)

    # update() 方法
    def update(self):
        """ Check if bottom edge has reached screen bottom. 检查底部边缘是否已到达屏幕底部。"""
        # 检测是否落地
        if self.bottom > games.screen.height:
            # 如果落地，触发游戏结束并销毁披萨
            self.end_game()
            self.destroy()

    # handle_caught() 方法
    # 被平底锅接住时调用 简单销毁自己
    def handle_caught(self):
        """ Destroy self if caught. 如果被抓到，立即自毁。"""
        self.destroy()

    # end_game() 方法
    def end_game(self):
        """ End the game. 结束游戏。"""
        # 创建游戏结束消息
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        # 显示5秒后自动退出游戏
        # 游戏初始化时设置了 fps = 50 这意味着游戏每秒运行50帧
        # lifetime = 5 * games.screen.fps 消息会显示250帧 即5秒
        games.screen.add(end_message)

# 5.Chef 类（移动的厨师）
class Chef(games.Sprite):
    """
    A chef which moves left and right, dropping pizzas.
    """
    image = games.load_image("chef.bmp")

    # 构造函数
    # odds_change = 200：随机改变方向的概率
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        """ Initialize the Chef object. """
        super(Chef, self).__init__(image = Chef.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)
        
        self.odds_change = odds_change
        self.time_til_drop = 0

    # update() 方法
    def update(self):
        """ Determine if direction needs to be reversed. """
        # 边界碰撞时反转方向
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        # 随机概率下改变方向（增加不可预测性）
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
        # 调用扔披萨检测
        self.check_drop()

    # check_drop() 方法
    def check_drop(self):
        """ Decrease countdown or drop pizza and reset countdown. """
        # 使用计时器控制扔披萨频率
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        # 计时器归零时扔出新披萨
        else:
            # self.x 指的是当前厨师对象的x坐标
            # 当厨师调用 check_drop() 方法扔披萨时，将厨师当前的x坐标传递给披萨的构造函数
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)

            # set buffer to approx 30% of pizza height, regardless of pizza speed   
            # 重新设置计时器，基于披萨高度和速度计算间隔
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1

# 6.main() 函数
def main():
    """ Play the game. """
    # 设置背景
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    # 创建厨师并添加到屏幕
    the_chef = Chef()
    games.screen.add(the_chef)

    # 创建平底锅并添加到屏幕
    the_pan = Pan()
    games.screen.add(the_pan)

    # 隐藏鼠标指针
    games.mouse.is_visible = False

    # 启用事件捕获
    games.screen.event_grab = True

    # 启动游戏主循环
    games.screen.mainloop()

# start it up!
main()