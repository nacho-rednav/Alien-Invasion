import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
	'''Class to manage bullets fired from the ship'''
	
	def __init__(self, ai_settings, screen, ship):
		'''Create a bullet object at the ship´s current position'''
		super().__init__()
		self.screen = screen
		
		#Create a bullet rect at position(0,0) and set correct position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#Store the bullet´s position as a decimal value
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.bullet_speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		'''Move the bulllet up the screen'''
		#Update the decimal position of the bullet
		self.y -= self.bullet_speed_factor
		#Update the rect position
		self.rect.y = self.y
				
	def draw_bullet(self):
		'''Draw the bullert to the screen'''
		pygame.draw.rect(self.screen, self.color, self.rect)
		
class Superbullets(Sprite):
	'''Class to manage Super bullets fired from the ship'''
	
	def __init__(self, ai_settings, screen, ship):
		'''Create a super bullet object at the ship´s current position'''
		super().__init__()
		self.screen = screen

		#Create a super bullet rect at position(0,0) and set correct position
		self.rect = pygame.Rect(0, 0, ai_settings.superbullet_width, 
			ai_settings.superbullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#Store the bullet´s position as a decimal value
		self.y = float(self.rect.y)

		self.color = ai_settings.superbullet_color
		self.superbullet_speed_factor = ai_settings.superbullet_speed_factor

	def update(self):
		'''Move the bulllet up the screen'''
		#Update the decimal position of the bullet
		self.y -= self.superbullet_speed_factor
		#Update the rect position
		self.rect.y = self.y

	def draw_superbullet(self):
		'''Draw the bullert to the screen'''
		pygame.draw.rect(self.screen, self.color, self.rect)