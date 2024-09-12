from simulation import Simulation
from utils.file_manager import FileManager

def main():
    fm = FileManager()
    load_dict = fm.load_file("template.json")

    eyes_size = load_dict["population"]["organisms"]["eyes_size"]
    load_dict["population"]["organisms"]["nn_layer_sizes"] = [2 * (eyes_size ** 2 + eyes_size) + 3, 
                                                                (1 + eyes_size) * 4, 
                                                                (1 + eyes_size) * 2, 
                                                                9]
    simulation = Simulation(load_dict)

    simulation.evolve()
    
    dict = fm.sim_to_dict(load_dict, simulation)
    fm.save_dict("save.json", dict)

if __name__ == "__main__":
    main()
