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
    self.box = tk.ttk.Spinbox(
        self.frame,
        from_=scaleLow,
        to=scaleHigh,
        textvariable=self.current_value,
        wrap=True
    )
    self.box.grid(column=1, row=0, sticky='we')
    
    self.label = ttk.Label(self.frame, text=f"{value}:")
    self.label.grid(column=0, row=0, sticky='w')

    self.frame.pack(expand = True)


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
    self.root.destroy()
    

class SettingsWindow():
  def __init__(self, load_dict):
    # --- SETUP ---
    # window
    self.root = tk.Tk()
    self.root.title("Interface")
    self.root.geometry("300x400")

    # layout setup
    self.main_frame = tk.Frame(self.root)
    self.main_frame.pack(fill="both", expand=1)

    self.scroll_frame = tk.Frame(self.main_frame)
    self.scroll_frame.pack(fill="y", side="right")

    self.canvas = tk.Canvas(self.main_frame)
    self.canvas.pack(side="left", fill="both", expand=1)

    # Scrollbar
    self.scrollbar = tk.ttk.Scrollbar(
        self.scroll_frame,
        orient="vertical",
        command=self.canvas.yview
    )
    self.scrollbar.pack(side="right", fill="y")

    # canvas config
    self.canvas.configure(yscrollcommand=self.scrollbar.set)
    self.canvas.bind("<Configure>",
                lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all"))) 

    # frame inside canvas
    self.content_frame = tk.Frame(self.canvas)

    # add window -> content gets displayed
    self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

    self.start_simulation = False
    # --- CONTENT ---
    # self.sliders = {}
    # for key in load_dict.keys():
    #   if type(load_dict[key]) is not dict:
    #     self.sliders[key] = Slider(key, self.content_frame, 0, 100)
    #   else:
    #     self.sliders[key] = {}
    #     for sub_key in load_dict[key].keys():
    #       if type(load_dict[key][sub_key]) is not dict:
    #         self.sliders[key][sub_key] = Slider(sub_key, self.content_frame, 0, 100)
    #       else:
    #         self.sliders[key][sub_key] = {}
    #         for sub_sub_key in load_dict[key][sub_key].keys():
    #           self.sliders[key][sub_key][sub_sub_key] = Slider(sub_sub_key, self.content_frame, 0, 100)

    
    self.boxes = {}
    for key in load_dict.keys():
      if type(load_dict[key]) is not dict:
        self.boxes[key] = Box(key, self.content_frame, 0, 100, 42)
      else:
        self.boxes[key] = {}
        for sub_key in load_dict[key].keys():
          if type(load_dict[key][sub_key]) is not dict:
            self.boxes[key][sub_key] = Box(sub_key, self.content_frame, 0, 100, 42)
          else:
            self.boxes[key][sub_key] = {}
            for sub_sub_key in load_dict[key][sub_key].keys():
              self.boxes[key][sub_key][sub_sub_key] = Box(sub_sub_key, self.content_frame, 0, 100, 42)

    self.bStart = tk.ttk.Button(self.content_frame, text = "Start", command = self.startSimulation)
    self.bStart.pack(expand = True)

  def run(self):
    self.root.mainloop()

  def startSimulation(self):
    self.root.destroy()
    self.start_simulation = True


class SaveWindow():
  def __init__(self):
    pass   
