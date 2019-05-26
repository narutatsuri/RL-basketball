import pygame
import numpy as np
from constants import *
from math import sqrt

def check_collision(score, end, ground_rect, right_wall_rect, top_wall_rect, left_wall_rect, ball_rect, hoop_pole_rect, hoop_rect, ball_velocity, score_flag):
    #! Collision Checker
    if ball_rect.colliderect(ground_rect) or ball_rect.colliderect(top_wall_rect):
        ball_velocity[1] = -ball_velocity[1]
    elif ball_rect.colliderect(right_wall_rect) or ball_rect.colliderect(top_wall_rect) or ball_rect.colliderect(left_wall_rect):
        ball_velocity[0] = -ball_velocity[0]
    elif ball_rect.colliderect(hoop_rect):
        if score_flag == False and hoop_rect.top > ball_rect.top and hoop_rect.left <= ball_rect.left + ball_radius <= hoop_pole_rect.right:
            score = True; score_flag = True; end = True
            print("Scored!")
            ball_velocity[0] = 0
        elif hoop_rect.left <= ball_rect.right:
            ball_velocity[0] -= ball_velocity[0]
        else:
            if score_flag == False:
                ball_velocity[1] -= ball_velocity[1]
    elif ball_rect.colliderect(hoop_pole_rect):
        ball_velocity[0] = -ball_velocity[0]
    return ball_velocity, score, end, score_flag

class environment():
    def __init__(self, player_start_position, player_distance_from_hoop):
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        
        self.score_flag = 0
        self.player_position = player_start_position
        self.player_distance_from_hoop = player_distance_from_hoop
        self.ball_position = list((player_start_position[0]+player_width, player_start_position[1]-ball_radius*2))

        self.disp = pygame.display.set_mode((screen_width, screen_height), 0, 32)
        self.disp.fill(screen_color)

    def draw(self, ticks, blit=True):
        self.disp.fill(screen_color)
        #* Draw hoop, ground and player
        self.hoop_rect = pygame.draw.rect(self.disp, hoop_color, (hoop_position[0], hoop_position[1], hoop_width, hoop_height))
        self.hoop_pole_rect = pygame.draw.rect(self.disp, hoop_pole_color, (hoop_pole_position[0], hoop_pole_position[1], hoop_pole_width, hoop_pole_height))
        self.ground_rect = pygame.draw.rect(self.disp, ground_color, (0, screen_height-ground_thickness, screen_width, ground_thickness))
        self.player_rect = pygame.draw.rect(self.disp, player_color, (self.player_position[0], self.player_position[1], player_width, player_height))
        
        #* Walls, just for collision
        self.right_wall_rect = pygame.draw.rect(self.disp, ground_color, (screen_width-ground_thickness, 0, ground_thickness, screen_height))
        self.top_wall_rect = pygame.draw.rect(self.disp, ground_color, (0, 0, screen_width, ground_thickness))
        self.left_wall_rect = pygame.draw.rect(self.disp, ground_color, (0, 0, ground_thickness, screen_height))

        #* Draw ball
        self.ball_rect = pygame.draw.circle(self.disp, ball_color, (int(self.ball_position[0]), int(self.ball_position[1])), ball_radius, 0)
        
        textsurface = self.myfont.render(str(ticks), False, (0, 0, 0))
        self.disp.blit(textsurface,(ground_thickness, ground_thickness))

        if blit == True:
            pygame.display.update()

    def throw(self, speed, angle):
        """Function for throwing the ball. 
        0 < speed < 100, 0 < angle < pi/2(radians)"""

        self.end = False; self.score = False
        self.ball_velocity = [speed * np.cos(np.deg2rad(angle)), -speed * np.sin(np.deg2rad(angle))]
        self.ball_acceleration = [0, gravitational_force]
        self.start_time = pygame.time.get_ticks()
        self.previous_time = self.start_time/1000.
        ticks = 0
        while self.end == False and ticks < 1000:
            ticks += 1
            self.current_time = pygame.time.get_ticks()/1000.
            self.ball_velocity[0] += self.ball_acceleration[0]
            self.ball_velocity[1] += self.ball_acceleration[1] * (self.current_time - self.previous_time)
            self.ball_position[0] += self.ball_velocity[0] * (self.current_time - self.previous_time)
            self.ball_position[1] += self.ball_velocity[1] * (self.current_time - self.previous_time)
            self.previous_time = self.current_time
            self.draw(ticks)
            self.ball_velocity, self.score, self.end, self.score_flag = check_collision(self.score, self.end, self.ground_rect, self.right_wall_rect, self.top_wall_rect, self.left_wall_rect, self.ball_rect, self.hoop_pole_rect, self.hoop_rect, self.ball_velocity, self.score_flag)
        if self.score:
            self.score = 100
        else:
            self.score = -sqrt((self.ball_position[0] - hoop_position[0])**2 + (self.ball_position[1] - hoop_position[1])**2)

        #* Max score: 100, minimum score: -100

        return self.score
