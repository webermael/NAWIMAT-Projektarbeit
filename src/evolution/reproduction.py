from random import randint
from organisms.layer import Layer
from organisms.neural_network import NeuralNetwork

 
def reproduction(config, nn1, nn2):
    nn = NeuralNetwork(config.nn_layer_sizes)
    for layer in range(len(nn1.layers)):
        current_layer = Layer(nn1.layers[layer].nodes_in, nn1.layers[layer].size)

        for weight in range(len(nn1.layers[layer].weights)):
            choice = randint(1, 2)
            if choice == 1:
                current_layer.weights[weight] == nn1.layers[layer].weights[weight]
            elif choice == 2:
                current_layer.weights[weight] == nn2.layers[layer].weights[weight]

        for bias in range(len(nn1.layers[layer].biases)):
            choice = randint(1, 2)
            if choice == 1:
                current_layer.biases[bias] == nn1.layers[layer].biases[bias]
            elif choice == 2:
                current_layer.biases[bias] == nn2.layers[layer].biases[bias]

        nn.layers[layer] = current_layer
    return nn