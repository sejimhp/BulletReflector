from Common import *

class Player:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
        self.hp = 10
        self.x = 100
        self.y = 100

    def update(self):
        # 押されているキーをチェック
        self.pressed_keys = pygame.key.get_pressed()
        # 矢印キーなら画像を移動
        if self.pressed_keys[K_LEFT]:
            self.x -= 2
        if self.pressed_keys[K_RIGHT]:
            self.x += 2
        if self.pressed_keys[K_DOWN]:
            self.y += 2
        if self.pressed_keys[K_UP]:
            self.y -= 2


    def draw(self, stage):
        x = self.x
        y = self.y
        if self.x > SCREEN_SIZE[0]/2:
            x = SCREEN_SIZE[0]/2
        if self.y > SCREEN_SIZE[1]/2:
            y = SCREEN_SIZE[1]/2
        if self.x + SCREEN_SIZE[0]/2 > stage.img_rect[2]:
            x = self.x - (stage.img_rect[2] - SCREEN_SIZE[0])
        if self.y + SCREEN_SIZE[1]/2 > stage.img_rect[3]:
            y = self.y - (stage.img_rect[3] - SCREEN_SIZE[1])

        pygame.draw.circle(self.screen, (100,0,0), (int(1100+self.x/10), int(50+self.y/10)), 3)
        pygame.draw.circle(self.screen, (255,0,0), (int(x), int(y)), 20)
