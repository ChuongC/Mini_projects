import pygame
import sys
from time import sleep

from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):
        pygame.init()

        # control frame rate
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                self.settings.screen_heigh))
        
        self.stats = GameStats(self)
        self.score_b = Scoreboard(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        pygame.display.set_caption("Alien Invasion")

        self.game_active = False
        self.play_button = Button(self,"Play")

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                #get rid of the old bullet
                self._update_bullet()
                self._update_alien()

            self._updating_screen()

            self.clock.tick(60) #60times per sec

    def _check_events(self):
        #watch keyboard or mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            # continuous moving right
            elif event.type ==pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            print("Before reset:", self.stats.ship_life)
            self.stats.reset_stats()
            print("After reset:", self.stats.ship_life)
            self.score_b.prep_score()
            self.score_b.prep_level()
            self.score_b.prep_ships()

            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

            sleep(0.5)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False      
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._kill_alien()

    def _kill_alien(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.score_b.prep_score()
            self.score_b.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #increase level
            self.stats.level +=1
            self.score_b.prep_level()

        

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    
    def _ship_hit(self):
        if self.stats.ship_life > 0:

            self.stats.ship_life -= 1
            self.score_b.prep_ships()
            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()


            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_heigh:
                self._ship_hit()
                break
    
    def _update_alien(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!")
            self._ship_hit()
        
        self._check_aliens_bottom()


    def _create_alien(self, x_position, y_position):
        #make an alien
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _create_fleet(self):
        #Make a fleet of alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_heigh - 3*alien_height):
            #incre row
            while current_x < (self.settings.screen_width - alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width
            
            #finish a row; reset x value; incre y
            current_x = alien_width 
            current_y += 2*alien_height

    def _updating_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        self.score_b.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        #make the most recently drawn visible
        pygame.display.flip()

if __name__ == '__main__':
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()

                

