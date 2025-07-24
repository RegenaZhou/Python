import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen # 赋值为游戏窗口
        self.screen_rect = ai_game.screen.get_rect() # 赋值为游戏窗口的剧情
        self.settings = ai_game.settings

        # 加载飞船图像并获取其外接矩形

        # 加载原始飞船图像
        original_image = pygame.image.load('images/ship.bmp')

        # 设置缩放比例（例如缩小到50%）
        scale_factor = 0.5  # 可调整此值改变大小

        # 计算新尺寸（保持宽高比）
        original_width, original_height = original_image.get_size()
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        # 等比缩放图像
        self.image = pygame.transform.smoothscale(
            original_image,
            (new_width, new_height)
        )

        # 获取缩放后的矩形
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞创的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)