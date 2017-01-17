from Common import *

class Stage:
    def __init__(self):
        SCREEN_SIZE = (1366, 768)  # 本番環境画面サイズ
        self.img_bg = pygame.image.load("test.jpg").convert()
        self.img_rect = self.img_bg.get_rect()
        print (self.img_rect)
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
