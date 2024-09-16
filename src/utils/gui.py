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

class LoadWindow():
  def __init__(self):
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

    self.lTitle = tk.ttk.Label(self.root, text = "Load File")  
    self.lTitle.grid(column=1, row=1) 

    self.bStart = tk.ttk.Button(self.root, text = "Use Template", command = self.template)
    self.bStart.grid(column=1, row=2)

    self.bStart = tk.ttk.Button(self.root, text = "Choose File", command = self.load_file)
    self.bStart.grid(column=1, row=3)

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
  def __init__(self):
    # Window
    self.root = tk.Tk()
    self.root.title("Interface")
    self.root.geometry("300x400")

    # Layout setup
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

    # self.slider = tk.ttk.Scale(
    #     self.content_frame,
    #     from_=0,
    #     to=100,
    #     orient="horizontal",
    #     command=self.printValue
    # )
    # self.slider.pack()

    slider1 = Slider("Slider 1", self.content_frame, 0, 100)

  def printValue(self, event):
      print(self.slider.get())

  def run(self):
    self.root.mainloop()
# class Settings MAX:
#     # self.scales = {
#     #   self.scaleRowLength = Scale(self.settings, 1, 5000)    
#     #   self.scaleColumnLength = Scale(self.settings, 1, 5000)
#     #   self.scalePopulation = Scale(self.settings, 10, 1000)
#     #   self.scaleGeneration = Scale(self.settings, 1, 1000)
#     #   }
    
#     self.scrollbar = tk.ttk.Scrollbar(self.settings, orient='vertical', command=self.scales.yview)# .yview is a problem yet
#     self.scrollbar.grid(row=0, column=1, sticky=tk.NS)
#     self.scales['yscrollcommand'] = self.scrollbar.set

#     self.settings.mainloop()
    
#   def getScaleValue(self):# command for getting values from scales
#     value1 = self.scaleRowLength.get()# Var names are all wrong
#     value2 = self.scaleColumnLenght.get()
#     value3 = self.scalePopulation.get()
#     value4 = self.scaleGeneration.get()
#     self.settings.destroy()# closes the window
#     #start the sim

