"""Constants used in the environment."""
#! 100 pixels = 1 meter

import numpy as np

# ! Colors
white = (255, 255, 255)
aqua= (0, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
silver = (192,192,192)
light_green = (152, 251, 152)
orange = (255, 165, 0)

#! Screen
screen_width = 1000
screen_height = 800
screen_color = white

#! Ground
ground_thickness = 20
ground_color = black

#!Hoop
hoop_pole_height = 300
hoop_pole_width = 10
hoop_pole_color = blue
hoop_pole_position = (900, screen_height-ground_thickness-hoop_pole_height)
hoop_width = 40
hoop_height = 3
hoop_color = red
hoop_position = (hoop_pole_position[0]-hoop_width, hoop_pole_position[1])

#! Shooter
player_width = 30
player_color = green

#! Ball
ball_radius = 15
ball_color = orange
gravitational_force = 980

#!Player
player_height = 175