class Settings():
	'''Class to store the games´settings'''
	
	def __init__(self):
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255 ,255)
		
		#Ship settings
		self.ships_limit = 3

		#Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 230, 0, 0
		self.bullets_allowed = 10
		#Super bullet settings
		self.superbullet_width = 15
		self.superbullet_height = 30
		self.superbullet_color = 230, 255, 0
		self.superbullets_allowed = 3

		#Alien settings
		self.fleet_drop_speed = 10
		self.alien_speed_factor = 1

		#How quickly the game speeds up
		self.speedup_scale = 1.1
		#How quicly alien´s value raises
		self.score_scale = 1.5

		self.initialize_dynamic_settings()
	
	def initialize_dynamic_settings(self):
		'''Initialize settings that change throughout the game'''
		self.ship_speed_factor = 2.5
		self.bullet_speed_factor = 1
		self.superbullet_speed_factor = 0.5
		self.fleet_direction = 1 #Changes to -1 to move left
		self.alien_points = 50

	def increase_speed(self):
		'''Increase speed when user levels up'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.superbullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		 


