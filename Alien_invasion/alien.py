import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''Class to represent an alien of the fleet'''
	
	def __init__(self, ai_settings, screen):
		'''Initialize the alien and set starting position'''
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Loads the alien´s image and set it´s rect
		self.image = pygame.image.load('images/ovnip.bmp')
		self.rect = self.image.get_rect()
		
			
		#Store the alien´s exact position
		self.x = float(self.rect.x)
	
	def check_edges(self):
		'''Checks if the alien hits left or right edge'''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self, aliens):
		'''Moves aliens right'''
		self.rect.x += (self.ai_settings.alien_speed_factor
			*self.ai_settings.fleet_direction)

	def blitme(self):
		'''Draw the alien at it´s current position'''
		self.screen.blit(self.image, self.rect)
