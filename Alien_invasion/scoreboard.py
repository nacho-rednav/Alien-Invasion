import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    '''A class to report scoring information'''

    def __init__(self, ai_settings, screen, stats):
        '''Initialize scorekeeping attributes'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Font settings for scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #Prepare the initial score, ships and level image
        self.prep_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        '''Turn the score into a rendered image'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        
        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def prep_level(self):
        '''Turn level into a rendered image'''
        self.level_image = self.font.render(str(self.stats.level), True,
            self.text_color, self.ai_settings.bg_color)
        #Position below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.top + 30

    def prep_ships(self):
        '''Show how many ships left'''
        self.ships_image = self.font.render(str(self.stats.ships_left ) + ' SHIPS', True,
            self.text_color, self.ai_settings.bg_color)
        #Position in left corner
        self.ship_rect = self.ships_image.get_rect()
        self.ship_rect.right = 150
        self.ship_rect.top = 20

    def show_score(self):
        '''Shows score and level on screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_image, self.ship_rect)
        