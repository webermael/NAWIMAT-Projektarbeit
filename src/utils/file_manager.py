import json

class FileManager:
    '''
    used to load from and to json files
    updates save data of a given dictionary with data from a simulation
    '''
    def __init__(self):
        pass

    # loads a json file into a dictionary
    def load_file(self, path):
        with open(path, "r") as file:
            file_content = json.load(file)
        file.close()
        return file_content
    
    def sim_to_dict(self, loaded_dict, simulation):
        # updates the values of the given save dictionary from before the simulation 
        # only updates networks and generation counter as they are the only things changed by the simulation
        networks = [{
                    "weights" : 
                        [layer.weights for layer in simulation.population.organisms[organism].nn.layers], 
                    "biases" : 
                        [layer.biases for layer in simulation.population.organisms[organism].nn.layers]
                    }
                    for organism in range(len(simulation.population.organisms))
                    ]
        loaded_dict["population"]["organisms"]["networks"] = networks
        loaded_dict["generation_counter"] = simulation.generation_counter
        return loaded_dict
    
    #saves dictionary to json file
    def save_dict(self, path, dict):
        with open(path, "w") as file:
            file = open(path, "w")
        json.dump(dict, file)
        file.close()