from simulation import Simulation
from utils.gui import LoadWindow
from utils.gui import SettingsWindow
from utils.file_manager import FileManager
import os.path

def main():
    fm = FileManager()

    while True:
        # --- LOAD FILE ---
        load_window = LoadWindow()
        load_window.run()
        load_dict = fm.load_file(load_window.loaded_file)
        settings_window = SettingsWindow(load_dict)
        settings_window.run()
        eyes_size = load_dict["population"]["organisms"]["eyes_size"]
        load_dict["population"]["organisms"]["nn_layer_sizes"] = [2 * (eyes_size ** 2 + eyes_size) + 3, 
                                                                    (1 + eyes_size) * 4, 
                                                                    (1 + eyes_size) * 2, 
                                                                    9]
        if settings_window.start_simulation:
            simulation = Simulation(load_dict)
            simulation.evolve()
        dict = fm.sim_to_dict(load_dict, simulation)
        fm.save_dict("save.json", dict)
            

if __name__ == "__main__":
    main()
