from keras.models import Sequential
from keras.layers import Dense
import numpy as np

class agent():
    def __init__(self, output_num, layer_name):
        self.model = Sequential()

        self.model.add(Dense(1, input_dim=1, kernel_initializer='random_uniform', 
        name=layer_name+"_1"))

        self.model.add(Dense(output_num, input_dim=1, kernel_initializer='random_uniform', 
        activation="sigmoid", name=layer_name+"_2"))

        self.model.compile(optimizer='rmsprop', loss='mse')

    def train(self, data):
        x = np.array([data[0]]); y = np.array([[data[1], data[2]]])
        #print(x, y)
        self.model.fit(x, y, verbose=False)

    def predict(self, x):
        x = np.array(x)
        return self.model.predict(x)