from layer import Layer


class NeuralNetwork:
    def __init__(self, layer_sizes : list[int]):
        self.layers = []
        for layer in range(len(layer_sizes) - 1):
            self.layers.append(Layer(layer_sizes[layer], layer_sizes[layer + 1])) # creates layer objects for all hidden layers and the output layer 
    
    def calc_output(self, inputs):
        for layer in self.layers:
            inputs = layer.calc_output(inputs)
        return inputs
