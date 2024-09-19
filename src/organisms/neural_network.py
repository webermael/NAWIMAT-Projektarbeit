from organisms.layer import Layer


class NeuralNetwork:
    '''
    creates a neural network for organisms
    can calulate an output when given the right amount of inputs
    '''
    def __init__(self, layer_sizes : list[int], weights = False, biases = False):
        self.layers = []
        for layer in range(len(layer_sizes) - 1):
            if weights and biases:
                self.layers.append(Layer(layer_sizes[layer], layer_sizes[layer + 1], weights[layer], biases[layer]))
            else:
                self.layers.append(Layer(layer_sizes[layer], layer_sizes[layer + 1])) # creates layer objects for all hidden layers and the output layer 
    

    def calc_output(self, inputs):
        for layer in self.layers:
            inputs = layer.calc_output(inputs)
        return inputs

    # returns the index of the largest network output
    def calc_greatest(self, inputs):
        values = self.calc_output(inputs)
        return values.index(max(values))
