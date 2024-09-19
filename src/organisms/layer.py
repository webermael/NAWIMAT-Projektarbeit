import math
import random

class Layer:
    '''
    single layer of a neural network
    consists of nodes, which contain weights and biases
    '''
    def __init__(self, nodes_in, size, weights = False, biases = False):
        self.size = size
        self.nodes_in = nodes_in # number of nodes in the previous layer

        # every node has a list of weights for all ingiong nodes
        if weights:
            self.weights = weights
        else:
            self.weights = [[random.uniform(-5, 5) for node in range(nodes_in)] for i in range(size)] 

        # bias for every node in the layer
        if biases:
            self.biases = biases
        else:
            self.biases = [random.uniform(-5, 5) for node in range(size)] 
    

    def activationFunction(self, x): # used on the output of every node to have a cleaner transition between high and low values and keep outputs small 
        return 1 / (1 + (math.e ** x)) # always returns a number between 0 and 1, giving a bigger increase/decrease in value less influence 
    

    def calc_output(self, inputs):
        outputs = []

        for node in range(self.size):
            # for each node in the current layer, adds its bias first then the weighted input of each ingoing node 
            output = self.biases[node] 
            for input in range(self.nodes_in):
                # multiplies value of each ingoing node with its weight, repeated for each node in the previous layer
                output += self.weights[node][input] * inputs[input] 
            outputs.append(self.activationFunction(output))
        
        return outputs	