from Common import *

class Item:
    def __init__(self):
        # アイテムの座標
        self.x = random.uniform(1, 3811)
        self.y = random.uniform(1, 2371)
        self.time = pygame.time.get_ticks()

    """def update(self, item_manager):
        if pygame.time.get_ticks() - self.time > 1000:
            self.time = pygame.time.get_ticks()
    """
    def draw(self, screen):
        x = self.x
        y = self.y

        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 20)
