import pygame
screen_height = 1080
screen_width = 1920
screen = pygame.display.set_mode((screen_width, screen_height))
red = (255, 0, 0)


class Player:
    def __init__(self, char_rendered, player_x, player_y, player_radius, player_speed, dead):
        self.player_x = player_x
        self.player_y = player_y
        self.player_radius = player_radius
        self.char_rendered = char_rendered
        self.dead = dead
        self.player_speed = player_speed
    def player_spr(self, screen, red):
        pygame.draw.circle(screen, red, (self.player_x, self.player_y), self.player_radius)

    def player_move(self, player_x_change, player_y_change):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_x_change += self.player_speed
                if event.key == pygame.K_LEFT:
                    player_x_change += -self.player_speed
                if event.key == pygame.K_UP:
                    player_y_change += -self.player_speed
                if event.key == pygame.K_DOWN:
                    player_y_change += self.player_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_y_change = 0
        self.player_x += player_x_change
        self.player_y += player_y_change
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_RIGHT]:
        #     self.player_x += 1
        # if keys[pygame.K_LEFT]:
        #     self.player_x += -1
        # if keys[pygame.K_UP]:
        #     self.player_y += -1
        # if keys[pygame.K_DOWN]:
        #     self.player_y += 1

        self.player_spr(screen, red)

