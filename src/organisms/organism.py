#from src.organisms.sensors import Sensor
#from src.organisms.neural_network import NeuralNetwork

class Organism:
    def __init__(self, config, ):
        self.position = (0, 0)
        self.vitality = 100 # current state of wellbeing, used to reduce lifetime more/less
        self.lifetime = 80 # how long the organism will live
        self.alive = True
        #self.nn = NeuralNetwork(config)

    def move(self, world):
        pass

