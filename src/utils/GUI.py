import tkinter as tk
from tkinter import ttk

class Startpage:
  def __init__(self):
    # setup
    self.root = tk.Tk()
    self.root.title("Simulation")
    self.root.geometry("300x400")
    # Config(self.root)
    self.root.columnconfigure(0, weight=1)
    self.root.columnconfigure(1, weight=3)
    self.root.columnconfigure(2, weight=1)
    self.root.rowconfigure(0, weight=1)
    self.root.rowconfigure(1, weight=1)
    self.root.rowconfigure(2, weight=1)
    self.root.rowconfigure(3, weight=1)
    self.root.rowconfigure(4, weight=1)

    self.lTitle = tk.ttk.Label(self.root, text = "SimEvolator")  
    self.lTitle.grid(column=1, row=1) 

    self.bStart = tk.ttk.Button(self.root, text = "Start!", command = self.start)
    self.bStart.grid(column=1, row=2)

    self.bSettings = tk.ttk.Button(self.root, text = "Settings", command = self.settings)
    self.bSettings.grid(column=1, row=3)

  def run(self):
    self.root.mainloop()

  def start(self, simulation):
    self.root.destroy()
    simulation.evolve()

  def settings(self):
    self.root.destroy()
    Settings()

  # widgets
    
class Settings:
  def __init__(self, config):
    #configs
    self.settings = tk.Tk()
    Config(self.settings)
    
    #widgets
    # self.scales = {
    #   self.scaleRowLength = Scale(self.settings, 1, 5000)    
    #   self.scaleColumnLength = Scale(self.settings, 1, 5000)
    #   self.scalePopulation = Scale(self.settings, 10, 1000)
    #   self.scaleGeneration = Scale(self.settings, 1, 1000)
    #   }
    
    self.scrollbar = tk.ttk.Scrollbar(self.settings, orient='vertical', command=self.scales.yview)# .yview is a problem yet
    self.scrollbar.grid(row=0, column=1, sticky=tk.NS)
    self.scales['yscrollcommand'] = self.scrollbar.set

    self.settings.mainloop()
    
  def getScaleValue(self):# command for getting values from scales
    value1 = self.scaleRowLength.get()# Var names are all wrong
    value2 = self.scaleColumnLenght.get()
    value3 = self.scalePopulation.get()
    value4 = self.scaleGeneration.get()
    self.settings.destroy()# closes the window
    #start the sim

# class Config:# maybe the class name is problematic
#   def __init__(self,root):
#     # root = tk.Tk() and root.mainloop() have to be directly in the specific class
#     self.geometry = "800x600"
#     root.geometry(self.geometry)
#     root.resizable(width = False, heigth = False)
    
#     self.title = "Simulation"
#     root.title(self.title)

class Scale:
  def __init__(self, root, scaleLow, scaleHigh):
    self.scale = tk.ttk.Scale(root, from_ = scaleLow, to = scaleHigh)
    self.scale.pack(expand = True) # not really a solution


startpage = Startpage()
startpage.run()
