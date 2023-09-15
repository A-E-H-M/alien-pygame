#Game from Python Crash Course Book
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    
    #Setting the framerate to prevent tearing on the screen.
    FPS = 200
    fpsClock = pygame.time.Clock()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Make a ship, a group of bullets, and a groups of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        #This is at the end of the loop, but just once. It is part of setting the frame rate to prevent tearing.
        fpsClock.tick(FPS)

run_game()
