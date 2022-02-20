
"""Constants used in the environment."""
#? 100 pixels = 1 meter

#? Training parameters
batch_size = 1
episodes = 100000
data_loop = 3

#? Colors
white = (255, 255, 255)
aqua= (0, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
silver = (192,192,192)
light_green = (152, 251, 152)
orange = (255, 165, 0)

#? Screen
screen_width = 1000
screen_height = 800
screen_color = white
font_size = 32

#? PATHs
font_dir = "misc/Raleway-Black.ttf"

#? Game parameters
max_ticks = 500
max_score = 100
speed_scale = 50
angle_scale = 90

#? Ground
ground_thickness = 20
ground_color = red

#?Hoop
hoop_pole_height = 300
hoop_pole_width = 10
hoop_pole_color = blue
hoop_pole_pos = (900, 
                      screen_height-ground_thickness-hoop_pole_height)
hoop_width = 40
hoop_height = 3
hoop_color = red
hoop_pos = (hoop_pole_pos[0]-hoop_width, 
                 hoop_pole_pos[1])

#? Shooter
player_width = 30
player_color = green

#? Ball
ball_radius = 15
ball_color = orange
gravitational_force = 0.098

#?Player
player_min_dist = 100
player_max_dist = hoop_pole_pos[0]-hoop_width-player_width
player_min_height = 160
player_max_height = 200

#? Training model
input_num = 2
output_num = 2