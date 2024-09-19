from random import random
from evolution.mutation import mutation
 
def reproduction(inputs, nn1, nn2):
    # creates a list with weights/biases which are copied from parents
    weights = [[[
            mutation(inputs["mutations"], nn1.layers[layer].weights[weight][node_weight]) if random() < 0.5
            else mutation(inputs["mutations"], nn2.layers[layer].weights[weight][node_weight])
            # has a 50/50 chance to take a given value from either parent
            for node_weight in range(len(nn1.layers[layer].weights[weight]))]
            # iterates through every weight of a given node
            for weight in range(len(nn1.layers[layer].weights))]
            # iterates through every node of a layer
            for layer in range(len(nn1.layers))
            ]
    biases = [[
            mutation(inputs["mutations"], nn1.layers[layer].biases[bias]) if random() < 0.5
            else mutation(inputs["mutations"], nn2.layers[layer].biases[bias]) 
            for bias in range(len(nn1.layers[layer].biases))]
            for layer in range(len(nn1.layers))
            ]
    return weights, biases
    