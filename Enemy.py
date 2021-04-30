import pygame
from Player import Player
from Mass import Mass
import random
import math
char_rendered = True
dead = False
player_speed = 20
player = Player(char_rendered, 960, 540, 10, player_speed, dead)
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

class Enemy:
    def __init__(self, enemy_rendered, enemy_x, enemy_y, enemy_radius, enemy_speed, enemy_dead):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self. enemy_radius = enemy_radius
        self.enemy_rendered = enemy_rendered
        self.enemy_dead = enemy_dead
        self.enemy_speed = enemy_speed

    def enemy_draw(self, screen, blue):
        pygame.draw.circle(screen, blue, (self.enemy_x, self.enemy_y), self.enemy_radius)

    def enemy_move(self, enemy_x_change, enemy_y_change):
        if self.enemy_radius > player.player_radius + 5:
            if self.enemy_x > player.player_x:
                enemy_x_change += -self.enemy_speed
            elif self.enemy_x < player.player_x:
                enemy_x_change += self.enemy_speed
            if self.enemy_y > player.player_y:
                enemy_y_change += -self.enemy_speed
            elif self.enemy_y < player.player_y:
                enemy_y_change += self.enemy_speed
        self.enemy_x += enemy_x_change
        self.enemy_y += enemy_y_change

    def mass_seek(self, enemy_x_change, enemy_y_change):
        for x in mass_list:
            distance = math.dist((self.enemy_x, self.enemy_y), (x.mass_x, x.mass_y))
            minimum = 100000000
            if distance <= minimum:
                minimum = distance
                print(minimum)
            if minimum <= distance:
                if self.enemy_x > x.mass_x:
                    enemy_x_change += -self.enemy_speed
                elif self.enemy_x < x.mass_x:
                    enemy_x_change += self.enemy_speed
                if self.enemy_y > x.mass_y:
                    enemy_y_change += -self.enemy_speed
                elif self.enemy_y < x.mass_y:
                    enemy_y_change += self.enemy_speed
                self.enemy_x += enemy_x_change
                self.enemy_y += enemy_y_change
