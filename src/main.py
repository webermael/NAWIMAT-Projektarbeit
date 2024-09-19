from simulation import Simulation
from utils.gui import LoadWindow, SettingsWindow, SaveWindow
from utils.file_manager import FileManager

def main():
    fm = FileManager()

    running = True
    while running:
        # --- LOAD FILE ---
        load_window = LoadWindow()
        load_window.run()
        if load_window.pressed_quit:
            break
        load_dict = fm.load_file(load_window.loaded_file)

        same_file = True
        while same_file:
            same_file = False
            # --- SETTINGS ---
            settings_window = SettingsWindow(load_dict)
            settings_window.run()
            if settings_window.pressed_quit:
                running = False
                break
            # calculates network layers based on eyes_size
            eyes_size = load_dict["population"]["organisms"]["eyes_size"]
            load_dict["population"]["organisms"]["nn_layer_sizes"] = [2 * (eyes_size ** 2 + eyes_size) + 3, 
                                                                        (1 + eyes_size) * 4, 
                                                                        (1 + eyes_size) * 2, 
                                                                        9]
            if settings_window.start_simulation:
                # --- SIMULATION ---
                simulation = Simulation(load_dict)
                simulation.evolve()
                dict = fm.sim_to_dict(load_dict, simulation)

            # --- SAVING ---
            save_window = SaveWindow()
            save_window.run()
            if save_window.pressed_quit:
                running = False
                break
            elif save_window.saving:
                fm.save_dict(save_window.save_file, dict)
            elif save_window.keeping:
                same_file = True


if __name__ == "__main__":
    main()
