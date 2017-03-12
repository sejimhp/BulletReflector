from Common import *

class EffectManager:
	def __init__(self):
		self.effects = []

	def update(self):
		for effect in self.effects:
			effect.update()
			if effect.valid():
				self.effects.remove(effect)

	def draw(self, screen, stage, player):
		for effect in self.effects:
			effect.draw(screen, stage, player)
