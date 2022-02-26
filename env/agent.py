from keras.models import Sequential
from keras.layers import Dense
from util.functions import *
from util import *
import numpy as np


class agent():
    def __init__(self):
        # Construct model
        self.model = Sequential()
        self.model.add(Dense(3, input_dim=input_num, 
                             kernel_initializer="random_normal"))
        self.model.add(Dense(output_num, input_dim=3, 
                             activation="sigmoid",
                             kernel_initializer="random_normal"))
        self.model.compile(loss='mse')

    def train(self,
              data):
        """
        """
        X = np.array(list(zip(column(data, 0), column(data, 1))))
        y = np.array(list(zip(column(data, 2), column(data, 3))))
                        
        self.model.fit(X, 
                       y, 
                       verbose=True)

    def predict(self, 
                x):
        """
        """
        return self.model.predict([x])[0]