from Common import *

class Stage:
    def __init__(self):
        self.img_bg = pygame.image.load("test.jpg").convert()
        self.img_rect = self.img_bg.get_rect()
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)

    def update(self):
        return

    def draw(self, player):
        x = 0
        y = 0
        if player.x > SCREEN_SIZE[0]/2:
            x = -(player.x - SCREEN_SIZE[0]/2)
        if player.y > SCREEN_SIZE[1]/2:
            y = -(player.y - SCREEN_SIZE[1]/2)
        if player.x + SCREEN_SIZE[0]/2 > self.img_rect[2]:
            x = -(self.img_rect[2] - SCREEN_SIZE[0])
        if player.y + SCREEN_SIZE[1]/2 > self.img_rect[3]:
            y = -(self.img_rect[3] - SCREEN_SIZE[1])
        self.screen.blit(self.img_bg, (int(x), int(y)))

        # 右上のステージを描画
        pygame.draw.rect(self.screen, (100,100,100,0), Rect(1100,50,self.img_rect[2]/10,self.img_rect[3]/10))
        pygame.draw.rect(self.screen, (0,0,0,0), Rect(1100+int(-x/10),50+int(-y/10),SCREEN_SIZE[0]/10,SCREEN_SIZE[1]/10), 1)
