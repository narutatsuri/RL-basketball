from util import *
from env.environment import *
from env.agent import *
from tqdm import tqdm


# Initialize agent
player = agent()

# Player gets batch_size tries with the same parameters
# After batch_size, the environment resets and the agent is updated
for _ in tqdm(range(episodes)):
    #* Initialize player pos and height
    player_height =     np.random.randint(player_min_height,
                                          player_max_height)
    hoop_dist =         np.random.randint(player_min_dist, 
                                          player_max_dist)
    # Initialize record for game
    game_record = {}
    
    # Play game for batch_size times:
    for count in range(batch_size):
        # Construct environment
        env = environment(player_height,
                          hoop_dist)
        # Get model prediction
        player_action = player.predict([hoop_dist, 
                                       player_height])
        speed = player_action[0] 
        angle = player_action[1]
        # Throw ball in environment
        score = env.throw(speed * speed_scale, 
                          angle * angle_scale)
        print("Speed: ", speed, "Angle: ", angle, "Score: ", score)
        # Add attempt to training data
        game_record[(hoop_dist, player_height, speed, angle)] = score
    
    # Train agent
    #player.train(game_record)
        