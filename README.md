# Basketball-AI
Reinforcement Learning agent learns to shoot basketball.

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
