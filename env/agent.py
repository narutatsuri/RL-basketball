from keras.models import Sequential
from keras.layers import Dense
from util import *
import numpy as np


class agent():
    def __init__(self):
        # Construct model
        self.model = Sequential()
        self.model.add(Dense(1, input_dim=input_num, kernel_initializer="random_normal"))
        self.model.add(Dense(output_num, input_dim=1, activation="sigmoid", kernel_initializer="random_normal"))
        self.model.compile(loss='mse')

    def train(self, 
              data):
        """
        """
        x = np.array([data[0]])
        y = np.array([[data[1], data[2]]])
        
        self.model.fit(x, 
                       y, 
                       verbose=False)

    def predict(self, 
                x):
        """
        """
        return self.model.predict([x])[0]