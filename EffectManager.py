from Common import *

class EffectManager:
	def __init__(self):
		self.time = pygame.time.get_ticks()
		self.effects = []

    # def add(self):
    #    # self.effects.append(Damage())

    def update(self):
        for effect in self.effects:
            effect.update()

	def draw(self):
        for effect in self.effects:
            effect.draw()
