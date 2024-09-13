from random import randint
from organisms.layer import Layer
from evolution.mutation import mutation
from organisms.neural_network import NeuralNetwork

 
def reproduction(inputs, nn1, nn2):
    nn = NeuralNetwork(inputs["organisms"]["nn_layer_sizes"])
    for layer in range(len(nn.layers)):
        current_layer = Layer(nn.layers[layer].nodes_in, nn.layers[layer].size)

        for weights in range(len(nn.layers[layer].weights)):
            choice = randint(1, 2)
            for node_weight in range(len(nn.layers[layer].weights[weights])):
                if choice == 1:
                    current_layer.weights[weights][node_weight] = mutation(inputs["mutations"], nn1.layers[layer].weights[weights][node_weight])
                elif choice == 2:
                    current_layer.weights[weights][node_weight] = mutation(inputs["mutations"], nn2.layers[layer].weights[weights][node_weight])

        for bias in range(len(nn.layers[layer].biases)):
            choice = randint(1, 2)
            if choice == 1:
                current_layer.biases[bias] = mutation(inputs["mutations"], nn1.layers[layer].biases[bias])
            elif choice == 2:
                current_layer.biases[bias] = mutation(inputs["mutations"], nn2.layers[layer].biases[bias])

        nn.layers[layer] = current_layer
    return nn