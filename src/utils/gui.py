import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Slider:
  def __init__(self, value, root, scaleLow, scaleHigh):
    self.frame = tk.Frame(root)
    self.frame.columnconfigure(0, weight=1)
    self.frame.columnconfigure(1, weight=3)
    self.frame.columnconfigure(2, weight=1)
    self.slider = tk.ttk.Scale(
        self.frame,
        from_=scaleLow,
        to=scaleHigh,
        orient="horizontal",
        command=self.slider_changed,
    )
    self.slider.grid(column=1, row=0, sticky='we')
    
    self.label = ttk.Label(self.frame, text=f"{value}:")
    self.label.grid(column=0, row=0, sticky='w')

    self.value_label = ttk.Label(self.frame, text=self.get_current_value())
    self.value_label.grid(column=2, row=0, sticky='e')

    self.frame.pack(expand = True)

  def get_current_value(self):
      return '{: .2f}'.format(self.slider.get())

  def slider_changed(self, event):
      self.value_label.configure(text=self.get_current_value())


class Box:
  def __init__(self, value, root, scaleLow, scaleHigh, startValue):
    self.frame = tk.Frame(root)
    self.frame.columnconfigure(0, weight=1)
    self.frame.columnconfigure(1, weight=1)
    self.current_value = tk.StringVar(value=startValue)
    self.vcmd = (self.frame.register(self.validate), "%P")
    self.box = tk.ttk.Spinbox(
        self.frame,
        width=5,
        from_=scaleLow,
        to=scaleHigh,
        textvariable=self.current_value,
        validate="key",
        validatecommand=self.vcmd,
        wrap=True
    )
    self.box.grid(column=1, row=0, sticky='e')
    
    self.label = ttk.Label(self.frame, text=f"{value}:")
    self.label.grid(column=0, row=0, sticky='w')

    self.frame.pack(padx=5, pady=5)

  def validate(self, input_value):
    return input_value.count(".") in [0, 1] and input_value.replace(".", "").isdigit()

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

    # --- CONTENT ---
    self.lTitle = tk.ttk.Label(self.root, text = "Load File")  
    self.lTitle.grid(column=1, row=1) 

    self.bTemplate = tk.ttk.Button(self.root, text = "Use Template", command = self.template)
    self.bTemplate.grid(column=1, row=2)

    self.bLoadFile = tk.ttk.Button(self.root, text = "Choose File", command = self.load_file)
    self.bLoadFile.grid(column=1, row=3)

    self.loaded_file = ""


  def run(self):
    self.root.mainloop()

  def template(self):
    self.loaded_file = "template.json"
    self.root.destroy()
    
  def load_file(self):
    filetypes = [('JSON files', '*.json')]

    self.loaded_file = filedialog.askopenfilename(
        title='Open a file',
        initialdir='~/',
        filetypes=filetypes)

    if self.loaded_file != "" and self.loaded_file != ():
      self.root.destroy()
    

class SettingsWindow():
  def __init__(self, load_dict):
    # --- SETUP ---
    self.root = tk.Tk()
    self.root.title("Interface")
    self.root.geometry("")

    self.in_dict = load_dict
    self.start_simulation = False
    self.boxes = {}
    tk.Label(self.root, text="Settings").pack()
    for key in self.in_dict.keys():
      if type(self.in_dict[key]) is not dict:
        if key != "generation_counter":
          self.boxes[key] = Box(key, self.root, 0, 100, self.in_dict[key])
      else:
        tk.Label(self.root, text=f"{key}".capitalize()).pack()
        self.boxes[key] = {}
        for sub_key in self.in_dict[key].keys():
          if type(self.in_dict[key][sub_key]) is not dict:
            self.boxes[key][sub_key] = Box(sub_key, self.root, 0, 100, self.in_dict[key][sub_key])
          else:
            tk.Label(self.root, text=f"{sub_key}".capitalize()).pack()
            self.boxes[key][sub_key] = {}
            for sub_sub_key in self.in_dict[key][sub_key].keys():
              if sub_sub_key not in ["networks", "nn_layer_sizes"]:
                if not (self.in_dict["generation_counter"] > 0 and sub_sub_key == "eyes_size"):
                  self.boxes[key][sub_key][sub_sub_key] = Box(sub_sub_key, self.root, 0, 100, self.in_dict[key][sub_key][sub_sub_key])
  
    self.bStart = tk.ttk.Button(self.root, text = "Start", command = self.startSimulation)
    self.bStart.pack(expand = True)

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
          self.in_dict[key] = float(self.boxes[key].box.get())
        case int():
          self.in_dict[key] = int(float(self.boxes[key].box.get()))
        case dict():
          for sub_key in self.boxes[key].keys():
            match self.in_dict[key][sub_key]:
              case float():
                self.in_dict[key][sub_key] = float(self.boxes[key][sub_key].box.get())
              case int():
                self.in_dict[key][sub_key] = int(float(self.boxes[key][sub_key].box.get()))
              case dict():
                for sub_sub_key in self.boxes[key][sub_key].keys():
                  match self.in_dict[key][sub_key][sub_sub_key]:
                    case float():
                      self.in_dict[key][sub_key][sub_sub_key] = float(self.boxes[key][sub_key][sub_sub_key].box.get())
                    case int():
                      self.in_dict[key][sub_key][sub_sub_key] = int(float(self.boxes[key][sub_key][sub_sub_key].box.get()))
    self.root.destroy()
    self.start_simulation = True

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

    # --- CONTENT ---
    self.lTitle = tk.ttk.Label(self.root, text = "Save File")  
    self.lTitle.grid(column=1, row=1) 

    self.bSave = tk.ttk.Button(self.root, text = "Save", command = self.save_file)
    self.bSave.grid(column=1, row=2)

    self.bRerun = tk.ttk.Button(self.root, text = "Rerun", command = self.rerun)
    self.bRerun.grid(column=1, row=3)

    self.save_file = ""
    self.saving = False


  def run(self):
    self.root.mainloop()

  def save_file(self):
    filetypes = [('JSON files', '*.json')]

    self.save_file = filedialog.askopenfilename(
        title='Choose a file',
        initialdir='~/',
        filetypes=filetypes)
    if self.save_file != "" and self.save_file != ():
      print(self.save_file)
      self.saving = True
      self.root.destroy()

  def rerun(self):
    self.saving = False
    self.root.destroy()
