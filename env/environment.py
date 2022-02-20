import pygame
import numpy as np
from util import *


class environment():
    """
    
    """
    def __init__(self, 
                 player_height,
                 hoop_dist):
        # Initialize pygame
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.Font(font_dir, 
                                       font_size)
        
        # Initialize variables
        self.player_pos = (hoop_pole_pos[0]-hoop_dist, 
                           screen_height-ground_thickness-player_height)
        self.player_height = player_height
        self.ball_pos = [self.player_pos[0]+player_width, 
                         self.player_pos[1]-ball_radius*2]
        # Initialize display
        self.disp = pygame.display.set_mode((screen_width, 
                                             screen_height), 
                                            0, 
                                            32)

    @staticmethod
    def calculate_score(score,
                        ball_pos, 
                        hoop_pos):
        """
        Calculates final reward.
        INPUTS:     
        OUTPUTS:    Int for score
        """
        
        # Max score: 100, minimum score: -100
        if score:
            return max_score
        else:
            return -np.sqrt((ball_pos[0] - hoop_pos[0])**2 + (ball_pos[1] - hoop_pos[1])**2)

    def check_collision(self,
                        ball_v):
        """
        INPUTS:     
        OUTPUTS:    
        """
        score = False; end = False
        # If the ball hits either four walls, reverse corresponding axis speed
        if self.ball_rect.colliderect(self.ground_rect):
            ball_v[1] = -ball_v[1]
            self.ball_pos[1] = screen_height-ground_thickness-ball_radius
        if self.ball_rect.colliderect(self.top_wall_rect):
            ball_v[1] = -ball_v[1]
            self.ball_pos[1] = ground_thickness+ball_radius
        if self.ball_rect.colliderect(self.right_wall_rect):
            ball_v[0] = -ball_v[0]
            self.ball_pos[0] = screen_width-ground_thickness-ball_radius
        if self.ball_rect.colliderect(self.left_wall_rect):
            ball_v[0] = -ball_v[0]
            self.ball_pos[0] = ground_thickness+ball_radius
        # If the ball hits the hoop
        if self.ball_rect.colliderect(self.hoop_rect):
            if self.hoop_rect.top > self.ball_rect.top and self.hoop_rect.left <= self.ball_rect.left + ball_radius <= self.hoop_pole_rect.right:
                score = True; end = True
                print("Scored!")
                ball_v[0] = 0
            elif self.hoop_rect.left <= self.ball_rect.right:
                ball_v[0] = -ball_v[0]
        elif self.ball_rect.colliderect(self.hoop_pole_rect):
            ball_v[0] = -ball_v[0]
            
        return ball_v, score, end

    def draw(self, 
             ticks, 
             blit=True):
        """
        Draws the environment. Blitting updates the display.
        INPUTS:     Int for time, Boolean for blit
        OUTPUTS:    None
        """
        # Fill screen with default color
        self.disp.fill(screen_color)
        # Draw hoop, ground and player
        self.hoop_rect =        pygame.draw.rect(self.disp, 
                                                 hoop_color, 
                                                 (hoop_pos[0], 
                                                  hoop_pos[1], 
                                                  hoop_width, 
                                                  hoop_height))
        self.hoop_pole_rect =   pygame.draw.rect(self.disp, 
                                                 hoop_pole_color, 
                                                 (hoop_pole_pos[0], 
                                                  hoop_pole_pos[1], 
                                                  hoop_pole_width, 
                                                  hoop_pole_height))
        self.ground_rect =      pygame.draw.rect(self.disp, 
                                                 ground_color, 
                                                 (0, 
                                                  screen_height-ground_thickness, 
                                                  screen_width, 
                                                  ground_thickness))
        self.player_rect =      pygame.draw.rect(self.disp, 
                                                 player_color, 
                                                 (self.player_pos[0], 
                                                  self.player_pos[1], 
                                                  player_width, 
                                                  self.player_height))
        # Draw walls for detecting collision
        self.right_wall_rect =  pygame.draw.rect(self.disp, 
                                                 ground_color, 
                                                 (screen_width-ground_thickness, 
                                                  0, 
                                                  ground_thickness, 
                                                  screen_height))
        self.top_wall_rect =    pygame.draw.rect(self.disp, 
                                                 ground_color, 
                                                 (0, 
                                                  0, 
                                                  screen_width, 
                                                  ground_thickness))
        self.left_wall_rect =   pygame.draw.rect(self.disp, 
                                                 ground_color, 
                                                 (0, 
                                                  0, 
                                                  ground_thickness, 
                                                  screen_height))
        # Draw ball 
        #!pos is approximated to integer
        self.ball_rect = pygame.draw.circle(self.disp, 
                                            ball_color, 
                                            [int(self.ball_pos[0]), 
                                             int(self.ball_pos[1])], 
                                            ball_radius)
        # Draw text
        textsurface = self.myfont.render(str(ticks), 
                                         False, 
                                         [0, 
                                          0, 
                                          0])
        self.disp.blit(textsurface,
                       [ground_thickness, 
                        ground_thickness])
        
        # Update screen if blit = True
        if blit == True:
            pygame.display.update()

    def throw(self, 
              speed, 
              angle):
        """
        Function for throwing the ball. 
        INPUTS:     Int for speed (0 < speed < 100), Float for angle (0 < angle < pi/2(radians))
        OUTPUTS:    Float for score
        """
        end = False
        # Compute ball v and a
        ball_v = [speed * np.cos(np.deg2rad(angle)), 
                  -speed * np.sin(np.deg2rad(angle))]
        ball_a = [0, 
                  gravitational_force]
        
        ticks = 0
        while end == False and ticks < max_ticks:
            ticks += 1
            # Update ball velocity
            ball_v[0] += ball_a[0]
            ball_v[1] += ball_a[1]
            #Update ball pos
            self.ball_pos[0] += ball_v[0]
            self.ball_pos[1] += ball_v[1]
            # Draw screen
            self.draw(ticks)
            ball_v, score, end = self.check_collision(ball_v)
        # Calculate score
        score = environment.calculate_score(score,
                                            self.ball_pos, 
                                            hoop_pos)

        return score
