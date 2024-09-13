import json

class FileManager:
    def __init__(self):
        pass

    def load_file(self, path):
        with open(path, "r") as file:
            file_content = json.load(file)
        file.close()
        return file_content
    
    def sim_to_dict(self, loaded_dict, simulation):
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
    
    def save_dict(self, path, dict):
        with open(path, "w") as file:
            file = open(path, "w")
        json.dump(dict, file)
        file.close()