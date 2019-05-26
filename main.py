from constants import *
from environment import *
from agent import *
from tqdm import tqdm

"""
---Simulation environment for shooting basketball.---

    Reinforcement learning project for learning the best angle 
    and speed to shoot a basketball depending on the distance 
    from the hoop and height of the hoop.


    ~TODO~
    1. Check if converging.
    2. Think of a better reward function
    3. Is sigmoid better than tanh? Check!
"""

batch_size = 1
episodes = 100000
data_loop = 3

#? Player and Agent
#? Player: Receives input and gives output
#? Agent: Receives input, player output and gives score
# 
#? Gameflow:
#? 1. Player outputs throwing parameters
#? 2. Parameters are executed in environment, and a score is given
#? 3. Agent reveices score and learns the mapping between input, player output and score. 
#?    Basically, how well the outputs of the player were.
#? 4. 

player = agent(2, "player")
scorer = {}

#* Player gets "batch_size" tries with the same parameters. 
#* After "batch_size", the environment's reset and the agent is updated.
for _ in range(episodes):
    #* Initial parameters
    player_distance_from_hoop = np.random.randint(100, hoop_pole_position[0]-hoop_width-player_width)
    player_position = (hoop_pole_position[0]-player_distance_from_hoop, screen_height-ground_thickness-player_height)

    for count in range(batch_size):
        env = environment(player_position, player_distance_from_hoop)
        (power, angle) = (player.predict([player_distance_from_hoop])[0][0], player.predict([player_distance_from_hoop])[0][1])
        original_power = power; original_angle = angle
        power *= 2000; angle *= 90
        score = env.throw(power, angle)
        print("Power: ", power, "Angle: ", angle, "Score: ", score)
        scorer[(player_distance_from_hoop, original_power, original_angle)] = score
    
    for index, value in enumerate(scorer.values()):
        if value > 0:
            for _ in range(data_loop):
                player.train(list(scorer.keys())[index])

        