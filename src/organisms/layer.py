import math
class Layer:
    def __init__(self, nodes_in, size):
        self.size = size
        self.nodes_in = nodes_in # number of nodes in the previous layer
        self.weights = [[1 for node in range(nodes_in)] for i in range(size)] # every node has a list of weights for all ingiong nodes
        self.biases = [0 for node in range(size)] # bias for every node in the layer
    

    def ActivationFunction(x):
        return 1 / (1 + (math.e ** x))
    

    def calc_output(self, inputs):
        outputs = []

        for node in range(self.size):
            output = self.biases[node] # for each node in the current layer, adds its bias first then the weighted input of each ingoing node 
            for input in range(self.nodes_in):
                output += self.weights[node][input] * inputs[input] # multiplies value of each ingoing node with its weight, repeated for each node in the previous layer

            outputs.append(self.ActivationFunction(output))
        
        return outputs	