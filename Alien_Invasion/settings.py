class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_heigh = 600
        self.bg_color = (230,230,230)

        self.ship_speed = 5.5
        self.ship_limit = 3

        #for bullets
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_speed = 7.5
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 5.5
        self.bullet_speed = 3.5
        self.alien_speed = 1.0
        #left -1, right 1
        self.fleet_direction = 1

        self.alien_point = 5
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point*self.score_scale)
        