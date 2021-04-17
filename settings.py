class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        #Screen settings
        self.screen_width = 960
        self.screen_height = 720
        self.bg_color = (51,51,255)

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255, 51, 51)
        self.bullets_allowed = 5

        #Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        
        #Fleet direction
        self.fleet_direction = 1

        #Inisialisasi kecepatan game
        self.speedup_scale = 1.1

        #Point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)