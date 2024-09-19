import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from utils.interface_values import interface_values
import os.path


class Box:
  def __init__(self, value, root, range_from, range_to, range_step, startValue):
    self.frame = tk.Frame(root)
    self.frame.columnconfigure(0, weight=1)
    self.frame.columnconfigure(1, weight=1)
    self.current_value = tk.StringVar(value=startValue)
    self.vcmd = (self.frame.register(self.validate), "%P")
    self.box = tk.ttk.Spinbox(
        self.frame,
        width=5,
        from_=range_from,
        to=range_to,
        values=[round(x * range_step, 2) for x in range(int(range_from / range_step), int(range_to / range_step) + 1)],
        textvariable=self.current_value,
        validate="key",
        validatecommand=self.vcmd,
        wrap=True
    )
    self.box.grid(column=1, row=0, sticky='e', padx=50)
    
    self.label = ttk.Label(self.frame, text=f"{value}:")
    self.label.grid(column=0, row=0, sticky='w', padx=50)

    self.frame.pack(padx=5, pady=2, fill="x")

  def validate(self, input_value):
    return input_value.count(".") in [0, 1] and input_value.replace(".", "").isdigit() or input_value == ""

class LoadWindow():
  def __init__(self):
    # --- SETUP ---
    self.root = tk.Tk()
    self.root.title("Simulation")
    self.root.geometry("300x400")
    self.root.columnconfigure(0, weight=1)
    self.root.columnconfigure(1, weight=3)
    self.root.columnconfigure(2, weight=1)
    self.root.rowconfigure(0, weight=1)
    self.root.rowconfigure(1, weight=1)
    self.root.rowconfigure(2, weight=1)
    self.root.rowconfigure(3, weight=1)
    self.root.rowconfigure(4, weight=1)
    self.root.rowconfigure(5, weight=1)

    # --- CONTENT ---
    self.lTitle = tk.ttk.Label(self.root, text = "Load File", font = ("Helvetica", 20))  
    self.lTitle.grid(column=1, row=1) 

    self.bTemplate = tk.ttk.Button(self.root, text = "Use Template", command = self.template)
    self.bTemplate.grid(column=1, row=2)

    self.bLoadFile = tk.ttk.Button(self.root, text = "Choose File", command = self.load_file)
    self.bLoadFile.grid(column=1, row=3)

    self.bQuit = tk.ttk.Button(self.root, text = "Quit", command = self.quit)
    self.bQuit.grid(column=1, row=4)

    self.loaded_file = ""
    self.pressed_quit = False


  def run(self):
    self.root.mainloop()

  def template(self):
    local_path = os.path.abspath(os.path.dirname(__file__))
    self.loaded_file = os.path.join(local_path, "template.json")
    self.root.destroy()
    
  def load_file(self):
    filetypes = [('JSON files', '*.json')]

    self.loaded_file = filedialog.askopenfilename(
        title='Open a file',
        initialdir='~/',
        filetypes=filetypes)

    if self.loaded_file != "" and self.loaded_file != ():
      self.root.destroy()

  def quit(self):
    self.pressed_quit = True
    self.root.destroy()
    

class SettingsWindow():
  def __init__(self, load_dict):
    # --- SETUP ---
    self.root = tk.Tk()
    self.root.title("Interface")
    self.root.geometry("")
    self.left_frame = tk.Frame(self.root)
    self.right_frame = tk.Frame(self.root)
    self.frame_switch = False

    self.in_dict = load_dict
    self.start_simulation = False
    self.boxes = {}
    tk.Label(self.root, text="Settings", font=("Helvetica", 20), pady=20).pack()
    for key in self.in_dict.keys():
      if key == "population":
        self.frame_switch = True
      if type(self.in_dict[key]) is not dict:
        if key != "generation_counter":
          self.boxes[key] = Box(interface_values[key][0],
                                (self.right_frame if self.frame_switch else self.left_frame), 
                                interface_values[key][1],
                                interface_values[key][2],
                                interface_values[key][3],
                                self.in_dict[key])
      else:
        tk.Label((self.right_frame if self.frame_switch else self.left_frame), text=f"{key}".capitalize(), font=("Helvetica", 16)).pack()
        self.boxes[key] = {}
        for sub_key in self.in_dict[key].keys():
          if type(self.in_dict[key][sub_key]) is not dict:
            self.boxes[key][sub_key] = Box(interface_values[key][sub_key][0],
                                           (self.right_frame if self.frame_switch else self.left_frame), 
                                           interface_values[key][sub_key][1],
                                           interface_values[key][sub_key][2],
                                           interface_values[key][sub_key][3],
                                           self.in_dict[key][sub_key])
          else:
            label = sub_key
            if sub_key == "danger":
              label = "fire"
            tk.Label((self.right_frame if self.frame_switch else self.left_frame), text=f"{label}".capitalize(), font=("Helvetica", 14)).pack()
            self.boxes[key][sub_key] = {}
            for sub_sub_key in self.in_dict[key][sub_key].keys():
              if sub_sub_key not in ["networks", "nn_layer_sizes"]:
                if not (self.in_dict["generation_counter"] > 0 and sub_sub_key == "eyes_size"):
                  self.boxes[key][sub_key][sub_sub_key] = Box(interface_values[key][sub_key][sub_sub_key][0],
                                                              (self.right_frame if self.frame_switch else self.left_frame),
                                                              interface_values[key][sub_key][sub_sub_key][1],
                                                              interface_values[key][sub_key][sub_sub_key][2],
                                                              interface_values[key][sub_key][sub_sub_key][3],
                                                              self.in_dict[key][sub_key][sub_sub_key])
  
    self.bQuit = tk.ttk.Button(self.root, text = "Quit", command = self.quit)
    self.bQuit.pack(side = "bottom", expand = True, pady=20)

    self.bStart = tk.ttk.Button(self.root, text = "Start", command = self.startSimulation)
    self.bStart.pack(side = "bottom", expand = True, pady=20)

    self.left_frame.pack(side = "left", expand = True)
    self.right_frame.pack(side = "left", expand = True)


    self.pressed_quit = False

  def run(self):
    self.root.mainloop()

  def to_number(self, input_string):
    num = float(input_string)
    if num.is_integer():
      return int(num)
    else:
      return num

  def startSimulation(self):  
    for key in self.boxes.keys():
      match self.in_dict[key]:
        case float():
          if self.boxes[key].box.get() != "":
            self.in_dict[key] = float(self.boxes[key].box.get())
        case int():
          if self.boxes[key].box.get() != "":
            self.in_dict[key] = int(float(self.boxes[key].box.get()))
        case dict():
          for sub_key in self.boxes[key].keys():
            match self.in_dict[key][sub_key]:
              case float():
                if self.boxes[key][sub_key].box.get() != "":
                  self.in_dict[key][sub_key] = float(self.boxes[key][sub_key].box.get())
              case int():
                if self.boxes[key][sub_key].box.get() != "":
                  self.in_dict[key][sub_key] = int(float(self.boxes[key][sub_key].box.get()))
              case dict():
                for sub_sub_key in self.boxes[key][sub_key].keys():
                  if self.boxes[key][sub_key][sub_sub_key].box.get() != "":
                    match self.in_dict[key][sub_key][sub_sub_key]:
                      case float():
                        self.in_dict[key][sub_key][sub_sub_key] = float(self.boxes[key][sub_key][sub_sub_key].box.get())
                      case int():
                        self.in_dict[key][sub_key][sub_sub_key] = int(float(self.boxes[key][sub_key][sub_sub_key].box.get()))
    self.root.destroy()
    self.start_simulation = True

  def quit(self):
    self.pressed_quit = True
    self.root.destroy()

  
class SaveWindow():
  def __init__(self):
    # --- WINDOW ---
    self.root = tk.Tk()
    self.root.title("Save")
    self.root.geometry("300x400")
    self.root.columnconfigure(0, weight=1)
    self.root.columnconfigure(1, weight=3)
    self.root.columnconfigure(2, weight=1)
    self.root.rowconfigure(0, weight=1)
    self.root.rowconfigure(1, weight=1)
    self.root.rowconfigure(2, weight=1)
    self.root.rowconfigure(3, weight=1)
    self.root.rowconfigure(4, weight=1)
    self.root.rowconfigure(5, weight=1)
    self.root.rowconfigure(6, weight=1)

    # --- CONTENT ---
    self.lTitle = tk.ttk.Label(self.root, text = "Save File", font = ("Helvetica", 20))  
    self.lTitle.grid(column=1, row=1) 

    self.bSave = tk.ttk.Button(self.root, text = "Save", command = self.save_file)
    self.bSave.grid(column=1, row=2)

    self.bSettings = tk.ttk.Button(self.root, text = "Settings", command = self.settings)
    self.bSettings.grid(column=1, row=3)

    self.bLoad = tk.ttk.Button(self.root, text = "Load new File", command = self.load)
    self.bLoad.grid(column=1, row=4)

    self.bQuit = tk.ttk.Button(self.root, text = "Quit", command = self.quit)
    self.bQuit.grid(column=1, row=5)

    self.save_file = ""
    self.keeping = False
    self.saving = False
    self.loading = False
    self.pressed_quit = False


  def run(self):
    self.root.mainloop()

  def save_file(self):
    filetypes = [('JSON files', '*.json')]

    self.save_file = filedialog.asksaveasfilename(
        title='Choose a file',
        initialdir='~/',
        filetypes=filetypes)
    if self.save_file != "" and self.save_file != ():
      self.save_file += ".json"
      self.saving = True
      self.root.destroy()

  def settings(self):
    self.keeping = True
    self.root.destroy()

  def load(self):
    self.loading = True
    self.root.destroy()

  def quit(self):
    self.pressed_quit = True
    self.root.destroy()
