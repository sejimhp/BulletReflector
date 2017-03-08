from Common import *

class Item:
    def __init__(self):
        # アイテムの座標
        self.x = random.uniform(1, 100)
        self.y = random.uniform(1, 100)

    def draw(self, screen, player, stage):
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

        pygame.draw.circle(screen, (0,200,0),\
         (int(1100+self.x/15), int(50+self.y/15)), 10)
        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 20)
