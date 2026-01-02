# Pizza Panic - Pygame 版本
# 玩家必须在披萨落地前接住它们

import pygame
import random
import sys
import os

# 初始化 Pygame
pygame.init()

# 设置游戏窗口
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pizza Panic")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# 加载图像函数
def load_image(name, scale=1):
    """加载图像并可选缩放"""
    try:
        image = pygame.image.load(name)
        if scale != 1:
            new_size = (int(image.get_width() * scale), int(image.get_height() * scale))
            image = pygame.transform.scale(image, new_size)
        return image.convert_alpha()
    except pygame.error as e:
        print(f"无法加载图像: {name}")
        print(e)
        # 如果图像加载失败，创建一个替代的彩色矩形
        surf = pygame.Surface((50, 50))
        surf.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        return surf


# 加载游戏图像
# 请确保这些图像文件存在于当前目录或指定路径中
pan_img = load_image("pan.bmp", 0.5)  # 平底锅图像
pizza_img = load_image("pizza.bmp", 0.5)  # 披萨图像
chef_img = load_image("chef.bmp", 0.5)  # 厨师图像
wall_img = load_image("wall.jpg")  # 背景图像

# 如果背景图像尺寸不匹配，调整大小
if wall_img.get_size() != (screen_width, screen_height):
    wall_img = pygame.transform.scale(wall_img, (screen_width, screen_height))


# Pan 类（玩家控制的平底锅）
class Pan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pan_img
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed = 8
        self.score = 0

        # 创建分数文本
        self.font = pygame.font.Font(None, 36)
        self.update_score_text()

    def update(self):
        # 获取鼠标位置
        mouse_x, _ = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x

        # 边界检测
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

    def update_score_text(self):
        self.score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.score_rect = self.score_text.get_rect(top=10, right=screen_width - 10)

    def draw_score(self, surface):
        surface.blit(self.score_text, self.score_rect)


# Pizza 类（下落的披萨）
class Pizza(pygame.sprite.Sprite):
    def __init__(self, x, y=90):
        super().__init__()
        self.image = pizza_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

        # 检查是否落地
        if self.rect.top > screen_height:
            self.kill()
            return True  # 返回True表示披萨落地
        return False


# Chef 类（移动的厨师）
class Chef(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = chef_img
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.centery = 55
        self.speed = 3
        self.direction = 1  # 1表示向右，-1表示向左
        self.drop_timer = 0
        self.drop_interval = 60  # 帧数

    def update(self):
        # 移动厨师
        self.rect.x += self.speed * self.direction

        # 边界检测和方向改变
        if self.rect.right > screen_width or self.rect.left < 0:
            self.direction *= -1
        elif random.randint(0, 200) == 0:  # 随机改变方向
            self.direction *= -1

        # 扔披萨计时器
        self.drop_timer += 1
        if self.drop_timer >= self.drop_interval:
            self.drop_timer = 0
            return True  # 返回True表示应该扔披萨
        return False


# 游戏主函数
def main():
    clock = pygame.time.Clock()

    # 创建精灵组
    all_sprites = pygame.sprite.Group()
    pizzas = pygame.sprite.Group()

    # 创建游戏对象
    pan = Pan()
    chef = Chef()

    # 添加到精灵组
    all_sprites.add(pan)
    all_sprites.add(chef)

    # 游戏状态
    game_over = False
    game_over_time = 0

    # 隐藏鼠标
    pygame.mouse.set_visible(False)

    # 游戏主循环
    running = True
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if game_over and event.key == pygame.K_r:
                    # 重新开始游戏
                    return main()

        if not game_over:
            # 更新游戏对象
            pan.update()

            # 更新厨师并检查是否应该扔披萨
            if chef.update():
                new_pizza = Pizza(chef.rect.centerx)
                all_sprites.add(new_pizza)
                pizzas.add(new_pizza)

            # 更新披萨并检查是否落地
            for pizza in pizzas:
                if pizza.update():  # 如果披萨落地
                    game_over = True
                    game_over_time = pygame.time.get_ticks()

            # 检测碰撞
            hits = pygame.sprite.spritecollide(pan, pizzas, True)
            for hit in hits:
                pan.score += 10
                pan.update_score_text()

        # 绘制
        screen.blit(wall_img, (0, 0))  # 绘制背景

        # 绘制所有精灵
        all_sprites.draw(screen)

        # 绘制分数
        pan.draw_score(screen)

        # 游戏结束显示
        if game_over:
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("GAME OVER", True, RED)
            game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(game_over_text, game_over_rect)

            # 显示重新开始提示
            restart_font = pygame.font.Font(None, 36)
            restart_text = restart_font.render("Press R to Restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
            screen.blit(restart_text, restart_rect)

            # 5秒后自动退出
            if pygame.time.get_ticks() - game_over_time > 5000:  # 5000毫秒 = 5秒
                running = False

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()
    sys.exit()


# 启动游戏
if __name__ == "__main__":
    main()