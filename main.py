from util import *
from env.environment import *
from env.agent import *
from tqdm import tqdm


# Initialize agent
player = agent()

# Initialize record for game. This will accumulate over time
game_record = []
# Player gets batch_size tries with the same parameters
# After batch_size, the environment resets and the agent is updated
for _ in tqdm(range(episodes)):
    
    score_count = 0
    # Play game for batch_size times:
    for count in range(batch_size):
        #* Initialize player pos and height
        player_height =     np.random.randint(player_min_height,
                                            player_max_height)
        hoop_dist =         np.random.randint(player_min_dist, 
                                            player_max_dist)
            
        # Construct environment
        env = environment(player_height,
                          hoop_dist,
                          blit=False)
        # Get model prediction
        player_action = player.predict([hoop_dist, 
                                       player_height])
        speed = player_action[0]
        angle = player_action[1]
        # Throw ball in environment
        score = env.throw(speed * speed_scale, 
                          angle * angle_scale)
        # print("Speed: ", speed, "Angle: ", angle, "Score: ", score)
        # Add attempt to training data
        if score == max_score:
            score_count += 1
            game_record.append([hoop_dist, player_height, speed, angle])
    
    print("Score percentage: ", score_count*100/batch_size, "%", flush=True)
    if len(game_record) != 0:
        # Train agent
        for _ in range(train_epochs):
            player.train(game_record)
        