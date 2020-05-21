# Reinforcement Learning on Basketball
Q Learning on a basketball shooter game.

## Environment Specifics
### Inputs(Parameters) 
* Distance from hoop 
* Height of hoop 
### Outputs 
* Shoot angle 
* Shoot velocity 
### Rewards 
* Proportional to ball's nearest distance from hoop
### Model Specifications
 * Optimization function
    - rmsprop
 * Loss function
    - MSE(mean squared error)
 * Activation
    - Sigmoid on 2nd layer
 * Initialization
    - random_uniform
## Dependencies
 - Python3
 - Pygame
 - Tensorflow (Backend)
 - Keras
 - Numpy
 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
