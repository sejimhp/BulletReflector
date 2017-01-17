from Common import *

class Enemy:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
        # 座標(double, double)
        self.x = random.uniform(1, 2000)
        self.y = random.uniform(1, 1000)
        # 移動速度
        self.r = random.uniform(0.1, 1)
        # 角度
        self.rad = 1

    def update(self, player):
        if player.x > self.x:
            self.x += self.r
        if player.y > self.y:
            self.y += self.r
        if player.x < self.x:
            self.x -= self.r
        if player.y < self.y:
            self.y -= self.r


    def draw(self, player, stage):
        x = self.x
        y = self.y
        if player.x > SCREEN_SIZE[0]/2:
            x -= (player.x - SCREEN_SIZE[0]/2)
        if player.y > SCREEN_SIZE[1]/2:
            y -= (player.y - SCREEN_SIZE[1]/2)
        if player.x + SCREEN_SIZE[0]/2 > stage.img_rect[2]:
            x = self.x - (stage.img_rect[2] - SCREEN_SIZE[0])
        if player.y + SCREEN_SIZE[1]/2 > stage.img_rect[3]:
            y = self.y - (stage.img_rect[3] - SCREEN_SIZE[1])

        '''
        if self.x > SCREEN_SIZE[0]/2:
            x = SCREEN_SIZE[0]/2
        if self.y > SCREEN_SIZE[1]/2:
            y = SCREEN_SIZE[1]/2
        if self.x + SCREEN_SIZE[0]/2 > stage.img_rect[2]:
            x = self.x - (stage.img_rect[2] - SCREEN_SIZE[0])
        if self.y + SCREEN_SIZE[1]/2 > stage.img_rect[3]:
            y = self.y - (stage.img_rect[3] - SCREEN_SIZE[1])
        '''

        pygame.draw.circle(self.screen, (0,100,0), (int(1100+self.x/10), int(50+self.y/10)), 3)
        pygame.draw.circle(self.screen, (0,255,0), (int(x), int(y)), 20)
