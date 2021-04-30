import pygame
import random
from Mass import Mass
from Player import Player
from Enemy import Enemy
import math
import time
pygame.init()
# Screen Dimensions
screen_height = 1080
screen_width = 1920
screen = pygame.display.set_mode((screen_width, screen_height))
# colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (66, 66, 245)
green = (32, 178, 170)
lime = (0, 255, 0)
black = (0, 0, 0)
colors = [red, blue, green, lime]

def main():
    clock = pygame.time.Clock()
    pygame.key.get_pressed()
    run = True
    char_rendered = True
    dead = False
    player_speed = 20
    player = Player(char_rendered, 960, 540, 10, player_speed, dead)

    # mass initiation
    mass1 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass2 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass3 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass4 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass5 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass6 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass7 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass8 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass9 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)
    mass10 = Mass(True, random.randint(0, 1920), random.randint(0, 1080), 5)

    mass_list = (mass1, mass2, mass3, mass4, mass5, mass6, mass7, mass8, mass9, mass10)

    enemy_rendered = True
    enemy_dead = False
    if enemy_dead:
        enemy_rendered = False
    enemy_speed = 20
    enemy1 = Enemy(enemy_rendered, 480, 270, 10, enemy_speed, enemy_dead)
    enemy2 = Enemy(enemy_rendered, 1440, 810, 10, enemy_speed, enemy_dead)
    enemy3 = Enemy(enemy_rendered, 480, 810, 10, enemy_speed, enemy_dead)
    enemy4 = Enemy(enemy_rendered, 1440, 270, 10, enemy_speed, enemy_dead)
    enemy_list = (enemy1, enemy2, enemy3, enemy4)

    # used to draw the background and all sprites on the field
    def redraw():
        # sets background to white and redraws every frame
        screen.fill(white)
        # despawns all elements when player dies
        if player.dead:
            mass1.rendered = False
            mass2.rendered = False
            mass3.rendered = False
            mass4.rendered = False
            mass5.rendered = False
            mass6.rendered = False
            mass7.rendered = False
            mass8.rendered = False
            mass9.rendered = False
            mass10.rendered = False
            enemy1.enemy_rendered = False
            enemy2.enemy_rendered = False
            enemy3.enemy_rendered = False
            enemy4.enemy_rendered = False
            player.char_rendered = False

        # Draws all entities individually and redraws them on top of the background every frame

        if mass1.rendered:
            mass1.draw(screen, blue)
        if mass2.rendered:
            mass2.draw(screen, blue)
        if mass3.rendered:
            mass3.draw(screen, blue)
        if mass4.rendered:
            mass4.draw(screen, red)
        if mass5.rendered:
            mass5.draw(screen, red)
        if mass6.rendered:
            mass6.draw(screen, red)
        if mass7.rendered:
            mass7.draw(screen, green)
        if mass8.rendered:
            mass8.draw(screen, green)
        if mass9.rendered:
            mass9.draw(screen, green)
        if mass10.rendered:
            mass10.draw(screen, green)

        if enemy1.enemy_rendered:
            enemy1.enemy_draw(screen, black)
        if enemy2.enemy_rendered:
            enemy2.enemy_draw(screen, black)
        if enemy3.enemy_rendered:
            enemy3.enemy_draw(screen, black)
        if enemy4.enemy_rendered:
            enemy4.enemy_draw(screen, black)

        if player.char_rendered:
            player.player_spr(screen, red)

        pygame.display.update()

    # allows enemies and players to eat mass
    def mass_respawn(mass_number):
        if abs(player.player_x - mass_number.mass_x) <= player.player_radius + mass_number.mass_radius \
                and abs(player.player_y - mass_number.mass_y) <= player.player_radius + mass_number.mass_radius and mass_number.rendered:
            player.player_radius += 10
            Mass.rand_location(mass_number)

        for x in enemy_list:
            if abs(x.enemy_x - mass_number.mass_x) <= x.enemy_radius + mass_number.mass_radius \
                    and abs(x.enemy_y - mass_number.mass_y) <= x.enemy_radius + mass_number.mass_radius and mass_number.rendered:
                x.enemy_radius += 10
                Mass.rand_location(mass_number)

    # allows enemies and players to die
    def death():
        for x in enemy_list:
            if player.player_radius >= x.enemy_radius + 5:
                if abs(player.player_x - x.enemy_x) <= player.player_radius + x.enemy_radius and abs(player.player_y - x.enemy_y) <= player.player_radius + x.enemy_radius and x.enemy_rendered:
                    player.player_radius += x.enemy_radius
                    x.enemy_dead = True
                    x.enemy_rendered = False
            if x.enemy_radius >= player.player_radius + 5:
                if abs(x.enemy_x - player.player_x) <= player.player_radius + x.enemy_radius and abs(x.enemy_y - player.player_y) <= player.player_radius + x.enemy_radius and x.enemy_rendered:
                    player.dead = True

    while run:
        clock.tick(30)

        # allows player to move
        player.player_move(0, 0)

        # allows enemies to move
        enemy1.enemy_move(0, 0)
        enemy2.enemy_move(0, 0)
        enemy3.enemy_move(0, 0)
        enemy4.enemy_move(0, 0)

        # respawns mass when eaten
        for x in mass_list:
            mass_respawn(x)

        #     allows enemies to travel to mass
        for x in enemy_list:
            x.mass_seek(0, 0)

        # sets borders for the screen to keep player sprite on the playing board
        if player.player_x <= player.player_radius:
            player.player_x = player.player_radius
        elif player.player_x >= 1920 - player.player_radius:
            player.player_x = 1920 - player.player_radius
        elif player.player_y <= player.player_radius:
            player.player_y = player.player_radius
        elif player.player_y >= 1080 - player.player_radius:
            player.player_y = 1080 - player.player_radius

        death()
        redraw()

    pygame.quit()


main()
